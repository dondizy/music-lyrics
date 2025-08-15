"""
Main Flask application for the Lyrics Fetcher API.
"""
import os
import sys
from flask import Flask, jsonify, request

# Debug imports
print(f"🐍 Python version: {sys.version}")
print(f"📁 Current directory: {os.getcwd()}")
print("📦 Importing application modules...")

try:
    from app.lyrics import get_lyrics
    print("✅ lyrics module imported")
except ImportError as e:
    print(f"❌ Error importing lyrics: {e}")
    raise

try:
    from app.spotify import get_song_info
    print("✅ spotify module imported")
except ImportError as e:
    print(f"❌ Error importing spotify: {e}")
    raise

try:
    from config.settings import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, GENIUS_ACCESS_TOKEN
    print("✅ settings module imported")
except ImportError as e:
    print(f"❌ Error importing settings: {e}")
    raise

app = Flask(__name__)
print("✅ Flask app created successfully")


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Lyrics Fetcher API"}), 200


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route("/lyrics", methods=["GET"])
def lyrics():
    track_url = request.args.get("track_url")
    if not track_url:
        return jsonify({"error": "Track URL is required"}), 400

    try:
        track_id = track_url.split("/track/")[1].split("?")[0]
    except IndexError:
        return jsonify({"error": "Invalid Track URL"}), 400
    if not track_id:
        return jsonify({"error": "Track ID is required"}), 400

    try:
        song_info = get_song_info(track_id)
        lyrics = get_lyrics(song_info["artist"], song_info["name"])
        return jsonify({"song_info": song_info, "lyrics": lyrics})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
