import os
from typing import List, Optional, Dict
from twitter_api_client import TwitterClient
from datetime import datetime
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterAINewsCollector:
    """Collects AI-related news from Twitter using the Twitter API."""
    
    def __init__(self):
        """Initialize the Twitter client with authentication."""
        load_dotenv()  # Load environment variables
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        if not self.bearer_token:
            raise ValueError("TWITTER_BEARER_TOKEN not found in environment variables")
        self.client = TwitterClient(bearer_token=self.bearer_token)

    def fetch_ai_news(self, max_results: int = 100) -> Optional[List[Dict]]:
        """
        Fetch recent AI-related tweets.
        
        Args:
            max_results (int): Maximum number of tweets to fetch (default: 100)
            
        Returns:
            Optional[List[Dict]]: List of tweets or None if an error occurs
        """
        try:
            query = """
                (artificial intelligence OR #AI OR #MachineLearning OR #DeepLearning)
                -is:retweet 
                lang:en 
                is:verified
                has:links
            """
            
            results = self.client.search_tweets(query=query.strip(), count=max_results, lang="en")
            
            if not results:
                logger.warning("No tweets found matching the criteria")
                return None
                
            logger.info(f"Successfully fetched tweets")
            return results
            
        except Exception as e:
            logger.error(f"Error fetching tweets: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    collector = TwitterAINewsCollector()
    tweets = collector.fetch_ai_news(max_results=10)
    
    if tweets:
        for tweet in tweets:
            print(f"Tweet: {tweet.get('text', '')}\n")
