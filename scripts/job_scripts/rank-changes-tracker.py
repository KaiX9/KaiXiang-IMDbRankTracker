import json
import os

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def save_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def track_changes(current_data, previous_data):
    changes = []
    previous_ranks = {movie['title']: movie['rank'] for movie in previous_data}
    current_titles = {movie['title'] for movie in current_data}
    previous_titles = {movie['title'] for movie in previous_data}

    if len(previous_data) > 0:
        # Checking for movies that are new to the list
        new_movies = current_titles - previous_titles
        for movie in current_data:
            if (movie['title'] in new_movies):
                changes.append({
                    'title': movie['title'],
                    'current_rank': movie['rank'],
                    'previous_rank': None,
                    'change': 'New entry to Top 250 list'
                })
        removed_movies = previous_titles - current_titles

        # Checking for movies that have left the list
        for movie in previous_data:
            if (movie['title'] in removed_movies):
                changes.append({
                    'title': movie['title'],
                    'current_rank': None,
                    'previous_rank': movie['rank'],
                    'change': 'Removed from Top 250 list'
                })
    
    # Comparing movies that remain on the list
    for movie in current_data:
        title = movie['title']
        current_rank = movie['rank']
        previous_rank = previous_ranks.get(title)
        if previous_rank:
            change = current_rank - previous_rank
            if (change == 0):
                changeStr = "No change in rank"
            elif (change < 0):
                changeStr = f"Rank moved up by {abs(change)}"
            elif (change > 0):
                changeStr = f"Rank moved down by {change}"
            changes.append({
                'title': title,
                'current_rank': current_rank,
                'previous_rank': previous_rank,
                'change': changeStr
            })
    return changes

# Getting the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constructing paths to the respective JSON files
current_data_path = os.path.join(script_dir, '../../data/imdb_top_250_movies.json')
previous_data_path = os.path.join(script_dir, '../../data/imdb_top_250_movies_previous.json')
changes_path = os.path.join(script_dir, '../../data/imdb_rank_changes.json')

current_data = load_json(current_data_path)
previous_data = load_json(previous_data_path)

changes = track_changes(current_data, previous_data)

save_json(changes, changes_path)
save_json(current_data, previous_data_path)