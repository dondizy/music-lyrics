"""
Lyrics fetching module using Genius API.
Handles searching and retrieving song lyrics.
"""
import os
import lyricsgenius
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_lyrics(artist_name: str, song_title: str) -> list:
    """
    Fetches lyrics for a given song and artist using the Genius API.
    
    Args:
        artist_name (str): The name of the artist
        song_title (str): The title of the song
        
    Returns:
        list: A list of lyrics lines or error message
    """
    try:
        # Initialize Genius client with access token
        genius = lyricsgenius.Genius(access_token=os.getenv("GENIUS_ACCESS_TOKEN"))
        
        # Search for the song
        song = genius.search_song(song_title, artist_name)
        
        if song:
            # Split lyrics into lines and filter out empty lines
            lyrics = song.lyrics.split('\n')
            lyrics = [line for line in lyrics if line.strip()]
            return lyrics
        else:
            return ["Lyrics not found."]
    except Exception as e:
        return [f"An error occurred: {e}"]
