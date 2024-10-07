import schedule
import time
import os

def run_all_jobs():
    # Getting the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Constructing the paths to the job scripts
    imdb_scraping_path = os.path.join(script_dir, '../job_scripts/imdb-scraping.py')
    rank_changes_tracker_path = os.path.join(script_dir, '../job_scripts/rank-changes-tracker.py')
    
    # Run the job scripts
    os.system(f'python {imdb_scraping_path}')
    os.system(f'python {rank_changes_tracker_path}')

schedule.every().day.at("00:00").do(run_all_jobs)

while True:
    schedule.run_pending()
    time.sleep(5)