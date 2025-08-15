#!/bin/bash
# Startup script for debugging
echo "🚀 Starting Lyrics Scraper API..."
echo "📁 Current directory: $(pwd)"
echo "🐍 Python version: $(python --version)"
echo "📦 Installed packages:"
pip list | grep -E "(flask|gunicorn|spotipy|lyricsgenius)"
echo "🧪 Testing app import..."
python -c "from main import app; print('✅ App imported successfully')"
echo "🌐 Starting with gunicorn..."
exec gunicorn main:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
