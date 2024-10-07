from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import json
import os

# Setting up of web driver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# Maximize the window
driver.maximize_window()

# Launch URL
driver.get('https://www.imdb.com/chart/top/')
time.sleep(10)
detail_view_icon = driver.find_element(By.ID, 'list-view-option-detailed')
detail_view_icon.click()
time.sleep(5)

movies = []
rows = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')
print(len(rows))
for row in rows:
    row_data = row.find_element(By.CSS_SELECTOR, '.sc-59c7dc1-3.dVCPce.dli-parent')
    if (row_data):
        titleString = row_data.find_element(By.XPATH, './/h3[contains(@class, "ipc-title__text")]').text
        titleParts = titleString.split('. ', 1)
        rank = int(titleParts[0])
        title = titleParts[1]
        director = row_data.find_element(By.XPATH, '//a[contains(@class, "ipc-link ipc-link--base dli-director-item")]').text
        year = row_data.find_element(By.CSS_SELECTOR, "span.sc-ab348ad5-8.cSWcJI.dli-title-metadata-item").text
        movies.append({
            'rank': rank,
            'title': title,
            'director': director,
            'year': int(year)
        })

# Getting the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constructing the path to JSON file
file_path = os.path.join(script_dir, '../../data/imdb_top_250_movies.json')
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w') as f:
    json.dump(movies, f, indent=4)
    print(f"Data written to {file_path}")