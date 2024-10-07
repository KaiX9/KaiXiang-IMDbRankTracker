# IMDb Top 250 Movies Rank Tracker

## Overview
This project scrapes IMDb's Top 250 Movies, tracks any changes in the movie ranks compared to the previous day and stores the data in JSON format.

## Directory
- `data/`: Contains JSON files for current and previous rankings, and rank changes.
- `scripts/`: Contains Python scripts for jobs like scraping and tracking rank changes, and also a scheduler script to run them.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Documentation.

## Additional Info
1. Data in JSON format stored in 'data' directory will automatically be created and saved if there are no existing data.
2. When running project, just have to run job-scheduler.py and all the other necessary jobs will run daily at 12AM.