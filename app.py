#!/usr/bin/env python3
"""
Lovebird API - Random lovebird image service
Similar to cataas.com but for lovebirds!
"""
from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
import os
import random
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Image directory
IMAGES_DIR = Path(__file__).parent / 'images'

def get_random_image():
    """Get a random image from the images directory"""
    images = list(IMAGES_DIR.glob('*.jpg')) + list(IMAGES_DIR.glob('*.png'))
    
    if not images:
        return None
    
    return random.choice(images)

@app.route('/')
def index():
    """API documentation"""
    return jsonify({
        'name': 'Lovebird API',
        'description': 'Random lovebird images API 🦜',
        'endpoints': {
            '/': 'This documentation',
            '/bird': 'Get a random lovebird image',
            '/bird/random': 'Get a random lovebird image (alias)',
            '/bird?json=true': 'Get image info in JSON format',
            '/health': 'Health check',
            '/count': 'Get total number of images'
        },
        'example': 'https://your-domain.com/bird'
    })

@app.route('/bird')
@app.route('/bird/random')
def random_bird():
    """Return a random lovebird image"""
    
    # Check if JSON response is requested
    json_response = request.args.get('json', 'false').lower() == 'true'
    
    image_path = get_random_image()
    
    if not image_path:
        return jsonify({'error': 'No images available'}), 404
    
    if json_response:
        # Return JSON with image info
        return jsonify({
            'file': image_path.name,
            'url': f'/bird/{image_path.name}',
            'size': image_path.stat().st_size
        })
    
    # Return the image file
    return send_file(
        image_path,
        mimetype='image/jpeg',
        as_attachment=False,
        download_name=image_path.name
    )

@app.route('/bird/<filename>')
def specific_bird(filename):
    """Return a specific bird image by filename"""
    image_path = IMAGES_DIR / filename
    
    if not image_path.exists():
        return jsonify({'error': 'Image not found'}), 404
    
    return send_file(
        image_path,
        mimetype='image/jpeg',
        as_attachment=False
    )

@app.route('/health')
def health():
    """Health check endpoint"""
    image_count = len(list(IMAGES_DIR.glob('*.jpg'))) + len(list(IMAGES_DIR.glob('*.png')))
    
    return jsonify({
        'status': 'healthy',
        'images_available': image_count
    })

@app.route('/count')
def count():
    """Return the number of available images"""
    image_count = len(list(IMAGES_DIR.glob('*.jpg'))) + len(list(IMAGES_DIR.glob('*.png')))
    
    return jsonify({
        'count': image_count
    })

if __name__ == '__main__':
    # Create images directory if it doesn't exist
    IMAGES_DIR.mkdir(exist_ok=True)
    
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
