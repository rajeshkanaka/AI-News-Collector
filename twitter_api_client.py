import requests
from typing import Optional, Dict, List

class TwitterClient:
    """Simple Twitter API client for searching tweets."""
    
    def __init__(self, bearer_token: str):
        """Initialize the client with authentication token."""
        self.bearer_token = bearer_token
        self.base_url = "https://api.twitter.com/2"
        self.headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }

    def search_tweets(self, query: str, count: int = 10, lang: str = "en") -> Optional[List[Dict]]:
        """Search for tweets using Twitter API v2."""
        endpoint = f"{self.base_url}/tweets/search/recent"
        params = {
            "query": f"{query} lang:{lang}",
            "max_results": count,
            "tweet.fields": "created_at,text",
        }
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("data", [])
        except Exception as e:
            print(f"Error searching tweets: {str(e)}")
            return None
