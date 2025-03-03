# Data_Engineering

1️ Installation of Dependencies
Before running the script, ensure you have Python 3.8 or higher installed. If not, download it from Python Official Site.

Install Required Python Libraries
Run the following command in your terminal (Command Prompt/PowerShell for Windows, or Terminal for macOS/Linux):

pip install pandas geopy
 pandas - For data processing
 geopy - To calculate distance between places

2️ Dataset Preparation
Ensure your dataset (travel_dataset.csv) contains at least the following columns:

Place Name	Nearest City	Rating	Reviews	Distance (km)	Travel Duration (hrs)	Latitude	Longitude
Lonavala	Mumbai	4.5	2500	85.3	2.5	18.7481	73.4072
Alibaug	Mumbai	4.2	1800	120.2	3.0	18.6411	72.8728
Matheran	Mumbai	4.3	2200	100.5	2.0	19.0245	73.1413

3️ Running the Script
Once the dependencies are installed and dataset is ready, execute the script as follows:

 Running for a Specific City
Use the following command to rank the top weekend destinations for a city:

python weekend_ranker.py
The script will prompt you to enter a city name.
 It will then rank the best weekend getaways based on multiple factors.
 Finally, it will display the top 5 places sorted by rank.


