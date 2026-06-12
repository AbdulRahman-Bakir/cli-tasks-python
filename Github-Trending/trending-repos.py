import argparse
from datetime import datetime, timedelta
import requests
import sys
from tabulate import tabulate

DAYS = {'day':1, 'week':7, 'month':30, 'year':365}
API_URL = "https://api.github.com/search/repositories"

def parse_args():
    parser = argparse.ArgumentParser(description="Show trending Github repos.")
    parser.add_argument("--duration", choices=DAYS.keys(), default="week")
    parser.add_argument("--limit", type=int, default=10)
    
    return parser.parse_args()

def fetch_repos(duration, limit):
    since = (datetime.now() - timedelta(days=DAYS[duration])).strftime("%Y-%m-%d")
    params = {"q":f"created:>{since}", "sort":"stars", "order":"desc", "per_page":limit}
    try:
        r = requests.get(API_URL, params=params, timeout=10)
        r.raise_for_status()
        return r.json()["items"]
    except Exception as e:
        raise Exception(f"An error happens: {e}")




if __name__ == "__main__":
    args = parse_args()
    if (args.limit > 100 or args.limit <1):
        print("limit should be between 1 and 100")
        sys.exit(1)
    repos= fetch_repos(args.duration, args.limit)
    rows= []
    for i, repo in enumerate(repos, start=1):
        rows.append([
            i, 
            repo["full_name"],
            repo["stargazers_count"],
            repo["language"],
            (repo["description"] or "")[:60]
        ])
    headers = ["#", "Repository", "Stars", "Language", "Description"]
    print(tabulate(rows, headers=headers, tablefmt="github"))
    print()