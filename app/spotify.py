"""
Spotify API integration module.
Handles fetching song information from Spotify using track IDs.
"""
from typing import TypedDict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


class SongInfo(TypedDict):
    name: str
    artist: str
    album: str
    release_date: str
    duration_ms: int
    popularity: int


def get_song_info(track_id: str) -> SongInfo:
    """
    Fetches song information from Spotify using the track ID.

    Args:
        track_id (str): The Spotify track ID.

    Returns:
        SongInfo: A dictionary containing song information such as name, artist, album, and release date.
    """
    # Set up Spotify client credentials using environment variables
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Fetch track details
    track_info = sp.track(track_id)

    # Extract relevant information
    if track_info is None:
        raise ValueError(f"No track information found for track ID: {track_id}")

    song_info: SongInfo = {
        "name": track_info["name"],
        "artist": ", ".join(artist["name"] for artist in track_info["artists"]),
        "album": track_info["album"]["name"],
        "release_date": track_info["album"]["release_date"],
        "duration_ms": track_info["duration_ms"],
        "popularity": track_info["popularity"],
    }

    return song_info
