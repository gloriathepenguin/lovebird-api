#!/usr/bin/env python3
"""
Download lovebird images from Pixabay
"""
import requests
import os
import time

# Pixabay API (public domain images)
# You can get a free API key from https://pixabay.com/api/docs/
# For now, using direct image URLs from search results

def download_from_urls():
    """Download images from curated list"""
    
    # These are example URLs - we'll use a web scraper approach instead
    base_url = "https://pixabay.com/api/"
    
    # Alternative: Download from Pexels (no API key needed for some endpoints)
    pexels_query = "lovebird parrot"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    print("Downloading lovebird images...")
    
    # Using Lorem Picsum as fallback (will replace with actual lovebird images)
    # In production, you'd use Pixabay API key or scrape properly
    
    # For demo, let's create placeholder structure
    # You'll need to manually add images or use Pixabay API key
    
    os.makedirs('images', exist_ok=True)
    print(f"Created images directory")
    print("Please add lovebird images to the 'images/' folder")
    print("You can download from:")
    print("- https://pixabay.com/images/search/lovebird/")
    print("- https://unsplash.com/s/photos/lovebird")
    print("- https://www.pexels.com/search/lovebird/")

if __name__ == "__main__":
    download_from_urls()
