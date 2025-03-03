import pandas as pd
from geopy.distance import geodesic

# Load dataset and rank weekend places
def rank_weekend_places(city_name, dataset_path="travel_dataset.csv"):
    df = pd.read_csv(dataset_path)

    # Filter by city
    filtered_df = df[df['Nearest City'].str.contains(city_name, case=False, na=False)]

    # Normalize factors
    filtered_df['Normalized Rating'] = filtered_df['Rating'] / filtered_df['Rating'].max()
    filtered_df['Normalized Reviews'] = filtered_df['Reviews'] / filtered_df['Reviews'].max()
    filtered_df['Normalized Distance'] = 1 - (filtered_df['Distance (km)'] / filtered_df['Distance (km)'].max())
    filtered_df['Normalized Duration'] = 1 - (filtered_df['Travel Duration (hrs)'] / filtered_df['Travel Duration (hrs)'].max())

    # Compute final score
    filtered_df['Score'] = (
        (filtered_df['Normalized Rating'] * 0.4) +
        (filtered_df['Normalized Reviews'] * 0.3) +
        (filtered_df['Normalized Distance'] * 0.2) +
        (filtered_df['Normalized Duration'] * 0.1)
    )

    # Rank and return top places
    ranked_places = filtered_df.sort_values(by=['Score'], ascending=False)
    return ranked_places[['Place Name', 'Nearest City', 'Rating', 'Reviews', 'Distance (km)', 'Travel Duration (hrs)', 'Score']].head(5)

# Calculate distance between places
def calculate_distance(place_lat, place_lon, city_lat, city_lon):
    return geodesic((city_lat, city_lon), (place_lat, place_lon)).km

# Fetch city coordinates (Mock function, replace with API call if needed)
def get_coordinates(city_name):
    city_coordinates = {
        "Delhi": (28.7041, 77.1025),
        "Mumbai": (19.0760, 72.8777),
        "Bangalore": (12.9716, 77.5946)
    }
    return city_coordinates.get(city_name, (None, None))

# Add distance column based on city coordinates
def add_distance_column(df, city_name):
    city_lat, city_lon = get_coordinates(city_name)
    if city_lat is None or city_lon is None:
        raise ValueError(f"Could not find coordinates for city: {city_name}")

    df["Distance"] = df.apply(lambda row: calculate_distance(row["Latitude"], row["Longitude"], city_lat, city_lon), axis=1)
    return df

# Rank places based on ratings, popularity, and distance
def rank_places(df):
    df["Rating_Score"] = df["Rating"] / df["Rating"].max()
    df["Popularity_Score"] = df["Popularity"] / df["Popularity"].max()
    df["Distance_Score"] = 1 - (df["Distance"] / df["Distance"].max())

    # Compute final ranking score
    df["Rank_Score"] = (0.4 * df["Rating_Score"]) + (0.4 * df["Popularity_Score"]) + (0.2 * df["Distance_Score"])
    
    return df.sort_values(by="Rank_Score", ascending=False)[["Place", "Distance", "Rating", "Popularity", "Rank_Score"]].head(10)

# Get top weekend places for a city
def get_weekend_places(city_name, df):
    df = add_distance_column(df, city_name)
    return rank_places(df)

# Example Dataset
data = {
    "Place": ["Lonavala", "Alibaug", "Matheran"],
    "Latitude": [18.7481, 18.6411, 19.0245],
    "Longitude": [73.4072, 72.8728, 73.1413],
    "Rating": [4.5, 4.2, 4.3],
    "Popularity": [85, 78, 80]
}
df = pd.DataFrame(data)

# Run for a city
city = "Mumbai"
top_places = get_weekend_places(city, df)
print("\n🏆 **Top Weekend Destinations:**")
print(top_places)
