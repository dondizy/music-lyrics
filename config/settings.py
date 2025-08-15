"""
Configuration settings for the lyrics scraper application.
Loads environment variables from .env file.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Genius API credentials
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")
