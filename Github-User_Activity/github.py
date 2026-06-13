import os 
import requests
import sys
import json 
import time
from python_dotenv import load_dotenv
load_dotenv()
CACHE_FILE = "cache.json"
CACHE_TTL = 60

def get_github_token():
    return os.environ.get('GITHUB_TOKEN', None)


def handle_github_response(response):
    response_dict = {}
    counter = 1
    repo_name = None
    commits_number = None
    string = None
    if isinstance(response, list):
        for event in response:
            if event['type'] == "PushEvent":
                commits_number = len(event['payload']['commits'])
                repo_name = event['repo']['name']
                string =  f"Pushed {commits_number} commits to {repo_name}"
            elif event['type'] == "CreateEvent":
                repo_name = event['repo']['name']
                string =  f"Created {repo_name}"
            elif event['type'] == "DeleteEvent":
                repo_name = event['repo']['name']
                string =  f"Deleted in {repo_name}"
            elif event['type'] == "ForkEvent":
                repo_name = event['repo']['name']
                string =  f"Forked {repo_name}"
            elif event['type'] == "MemberEvent":
                repo_name = event['repo']['name']
                collaborator = event['payload']['member']['login']
                string =  f"Added {collaborator} to {repo_name}"
            elif event['type'] == "PullRequestEvent":
                action = event['payload']['action']
                repo_name = event['repo']['name']
                string =  f"{action} pull request in {repo_name}"
            else:
                string = "Other event"
            response_dict[f'event_{counter}'] = {
                "event_type": event['type'],
                "event": string
            }
            counter += 1
        return response_dict
    else:
        return response
            
def get_arguments():
    if len(sys.argv) < 2:
        print("Error: GitHub username is required.\nUsage: python script.py <username> [event_type]")
        sys.exit(1)

    username = sys.argv[1]  # Required argument
    event_type = sys.argv[2] if len(sys.argv) > 2 else None  # Optional argument

    return username, event_type
            

def get_github_events():
    try:    
        github_token = get_github_token()
        github_username,_ = get_arguments()
            
        if github_token is None:
            raise Exception('GITHUB_TOKEN not found')
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as file:
                cache = json.load(file)
                if time.time() - cache['timestamp'] < CACHE_TTL:
                    return cache['data']
        
        url = f"https://api.github.com/users/{github_username}/events"      
        headers = {
            "accept":"application/vnd.github.v3+json",
            "Authorization": f"Bearer {github_token}"
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            acivities = response.json()
            final = handle_github_response(acivities)
            with open (CACHE_FILE, "w") as file:
                cache = {
                    "timestamp": time.time(),
                    "data":final
                }
                json.dump(cache, file)
            return final
        elif response.status_code == 404:
            raise Exception('User not found')
        else:
            raise Exception(response.json())
        
        
    except Exception as e:
        return e
    
if __name__ == "__main__":
    result = get_github_events()
    username , event_type = get_arguments()
    print(f"GitHub activity for {username}")
    for event_key, event_data in result.items():  # Unpack tuple
        if event_type is not None:
            if event_data['event_type'] == event_type:
                print(f"- {event_data['event']}")
        else:
            print(f"- {event_data['event']}")  # Print all events if no filter
