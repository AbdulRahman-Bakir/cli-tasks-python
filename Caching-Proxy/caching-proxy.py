import argparse
import os
import sys
import json
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler


def parse_args():
    parser = argparse.ArgumentParser(description="Returns resposnes from cache instead of touching the original server if they are there")
    parser.add_argument("--port", type=int, default=3000)
    parser.add_argument("--origin", default="https://dummyjson.com")
    parser.add_argument("--clear-cache", action="store_true")
    return parser.parse_args()

def load_cache() -> dict:
    if os.path.exists("cache.json"):
        with open("cache.json", "r") as file:
            return json.load(file)
    return {}

def save_cache(cache):
    with open("cache.json", "w") as file:
        json.dump(cache, file)

def clear_cache():
    if os.path.exists("cache.json"):
        os.remove("cache.json")
        print("Cache cleared.")
    else:
        print("Cache is already cleared.")
        
class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = f"{self.origin}{self.path}"
        cache = load_cache()
        if self.path in cache:
            entry = cache[self.path]
            self.send_entry(entry, "HIT")
            return
        try:
            response = requests.get(url, timeout=10)
        except requests.RequestException as e:
            self.send_error(502, "Bad Gateway", f"Origin unreachable: {e}")
            return
        entry = {"status": response.status_code, "content-type":response.headers["Content-Type"], "body": response.text}
        cache[self.path] = entry
        save_cache(cache)
        self.send_entry(entry, "MISS")
    
    def send_entry(self, entry, cache_status):
        self.send_response(entry["status"])
        self.send_header("Content-Type", entry["content-type"])
        self.send_header("X-Cache", cache_status)
        self.end_headers()
        self.wfile.write(entry["body"].encode())        
        


def run_server(port, origin):
    server = HTTPServer(("localhost", port), ProxyHandler)
    ProxyHandler.origin = origin
    server.serve_forever()

if __name__ == "__main__":
    args = parse_args()
    if args.clear_cache:
        clear_cache()
        sys.exit()
    
    print(f"Running on http://localhost:{args.port} -> {args.origin}")
    run_server(args.port, args.origin)
    