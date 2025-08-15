# Lyrics Scraper API

A Flask-based API that fetches song information from Spotify and lyrics from Genius API.

## Features

- Fetch song information from Spotify using track URLs
- Get song lyrics from Genius API
- Clean, modular project structure
- Production-ready for cloud deployment

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /lyrics?track_url=<spotify_track_url>` - Get song info and lyrics

## Environment Variables

Set these environment variables in your deployment platform:

```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
GENIUS_ACCESS_TOKEN=your_genius_access_token
```

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your API credentials
6. Run: `python main.py`

## Deployment to Render

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variables in Render dashboard
5. Deploy!

The app will be automatically deployed using the `Procfile` configuration.
