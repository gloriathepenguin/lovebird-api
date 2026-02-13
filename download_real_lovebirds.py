#!/usr/bin/env python3
"""
Download real lovebird images from Pixabay
"""
import requests
import os
import time

# Real lovebird image URLs from Pixabay (extracted from search results)
LOVEBIRD_URLS = [
    "https://cdn.pixabay.com/photo/2022/07/24/04/32/fischers-lovebird-7340954_1280.jpg",
    "https://cdn.pixabay.com/photo/2021/12/29/17/37/bird-6902371_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/09/13/09/12/parakeet-7451440_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962790_1280.jpg",
    "https://cdn.pixabay.com/photo/2014/04/05/11/38/parrot-316441_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/09/13/09/12/parakeets-7451439_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/50/lovebirds-6962741_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/04/08/23/04/lovebirds-5019097_1280.jpg",
    "https://cdn.pixabay.com/photo/2023/09/10/00/49/lovebird-8244066_1280.jpg",
    "https://cdn.pixabay.com/photo/2019/06/01/21/16/fischer-4245059_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962793_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962798_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962744_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962740_1280.jpg",
    "https://cdn.pixabay.com/photo/2014/04/05/11/38/parrot-314677_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/09/13/09/12/budgerigar-7607156_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/50/lovebirds-6962745_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/08/06/01/02/lovebird-7367776_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/11/04/19/22/lovebird-5713336_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962739_1280.jpg",
    "https://cdn.pixabay.com/photo/2022/01/24/07/56/lovebird-6962749_1280.jpg",
    "https://cdn.pixabay.com/photo/2014/04/05/11/38/parrot-316442_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/06/03/16/26/pet-2531165_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/11/07/05/39/lovebirds-5718158_1280.jpg",
    "https://cdn.pixabay.com/photo/2019/05/06/15/34/lovebirds-4340003_1280.jpg",
    "https://cdn.pixabay.com/photo/2015/08/14/19/21/budgies-904644_1280.jpg",
    "https://cdn.pixabay.com/photo/2018/08/08/05/47/lovebirds-3693635_1280.jpg",
    "https://cdn.pixabay.com/photo/2015/02/09/17/57/rainbow-630771_1280.jpg",
    "https://cdn.pixabay.com/photo/2018/05/22/15/22/couple-3420155_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/04/27/20/38/lovebirds-5099577_1280.jpg",
]

def download_images():
    """Download lovebird images"""
    os.makedirs('images', exist_ok=True)
    
    print(f"Downloading {len(LOVEBIRD_URLS)} lovebird images...")
    print("="*60)
    
    for i, url in enumerate(LOVEBIRD_URLS, 1):
        try:
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                filename = f"images/lovebird_{i:02d}.jpg"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                size_kb = len(response.content) / 1024
                print(f"✓ {i:2d}/30: Downloaded {filename} ({size_kb:.1f} KB)")
            else:
                print(f"✗ {i:2d}/30: Failed (HTTP {response.status_code})")
            
            # Be respectful to Pixabay's servers
            time.sleep(0.3)
            
        except Exception as e:
            print(f"✗ {i:2d}/30: Error - {e}")
    
    print("="*60)
    print(f"Done! Check the 'images/' folder")
    print(f"\nTo start the API:")
    print(f"  python3 app.py")

if __name__ == "__main__":
    download_images()
