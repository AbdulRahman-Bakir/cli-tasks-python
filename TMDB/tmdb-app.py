import requests
import argparse
import os 
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

TOKEN = os.getenv("TMDB_API_KEY")
BASE_URL= "https://api.themoviedb.org/3"
ENDPOINTS={
    "playing":"/movie/now_playing",
    "popular":"/movie/popular",
    "top":"/movie/top_rated",
    "upcoming":"/movie/upcoming"
}

def parse_args():
    parser = argparse.ArgumentParser(description="Showing Movies details by movie type")
    parser.add_argument("--type", choices=ENDPOINTS.keys(), default="popular")
    return parser.parse_args()

def fetch_movies(type):
    url = f"{BASE_URL}{ENDPOINTS[type]}"
    headers = {
        "Authorization":f"Bearer {TOKEN}",
        "Accept":"application/json"
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"An error happened: {e}")
    
    


if __name__ == "__main__":
    args = parse_args()
    data = fetch_movies(args.type)
    rows = []
    for i, movie in enumerate(data["results"]):
        rows.append([
            i,
            movie['title'],
            movie["release_date"],
            movie["vote_average"],
            (movie["overview"] or "")[:60]
        ])
    headers = ["#", "Title", "Release", "Rating", "Overview"]
    print(tabulate(rows, headers=headers, tablefmt="github"))