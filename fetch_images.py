#!/usr/bin/env python3
"""
Fetch lovebird images from Unsplash API
"""
import requests
import os
import time

# Using Unsplash Source API (no auth needed for basic usage)
UNSPLASH_SOURCE = "https://source.unsplash.com/800x600/?lovebird,parrot"
UNSPLASH_RANDOM = "https://api.unsplash.com/photos/random"

# Alternative: Picsum for testing (random images)
PICSUM_URL = "https://picsum.photos/800/600"

def download_images(count=30):
    """Download images using Unsplash source"""
    os.makedirs('images', exist_ok=True)
    
    print(f"Downloading {count} lovebird images...")
    
    for i in range(1, count + 1):
        try:
            # Using Unsplash Source (redirects to actual image)
            # Each request gets a different random image
            url = f"https://source.unsplash.com/800x600/?lovebird,parrot&sig={i}"
            
            response = requests.get(url, timeout=10, allow_redirects=True)
            
            if response.status_code == 200:
                filename = f"images/lovebird_{i:02d}.jpg"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"✓ Downloaded {filename}")
            else:
                print(f"✗ Failed to download image {i}: {response.status_code}")
            
            # Be nice to the API
            time.sleep(0.5)
            
        except Exception as e:
            print(f"✗ Error downloading image {i}: {e}")
    
    print(f"\nDone! Downloaded images to ./images/")

if __name__ == "__main__":
    download_images(30)
