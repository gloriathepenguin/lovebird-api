# 🦜 Lovebird API

A simple REST API that serves random lovebird (牡丹鹦鹉) images - inspired by cataas.com

## Features

- Random lovebird image endpoint
- JSON metadata support
- CORS enabled
- Lightweight and fast
- Easy to deploy

## API Endpoints

### `GET /`
API documentation

### `GET /bird` or `GET /bird/random`
Returns a random lovebird image

**Example:**
```
https://your-domain.com/bird
```

### `GET /bird?json=true`
Returns JSON with image metadata

**Response:**
```json
{
  "file": "lovebird_01.jpg",
  "url": "/bird/lovebird_01.jpg",
  "size": 123456
}
```

### `GET /bird/<filename>`
Get a specific image by filename

### `GET /health`
Health check endpoint

### `GET /count`
Get total number of available images

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

3. Test it:
```bash
curl http://localhost:5000/bird --output test.jpg
```

## Deployment Options

### Option 1: Railway (Recommended - Free tier available)

1. Create account at [railway.app](https://railway.app)
2. Install Railway CLI:
```bash
npm install -g @railway/cli
```

3. Login and deploy:
```bash
railway login
railway init
railway up
```

4. Your API will be live at: `https://your-app.railway.app/bird`

### Option 2: Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Create `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

3. Deploy:
```bash
vercel --prod
```

### Option 3: Your Own VPS

1. Copy files to your server:
```bash
scp -r lovebird-api user@your-server:/var/www/
```

2. On server, install dependencies:
```bash
cd /var/www/lovebird-api
pip install -r requirements.txt
```

3. Run with gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

4. (Optional) Set up nginx reverse proxy

## Adding Real Lovebird Images

**⚠️ Important:** Currently the API uses placeholder images. To add real lovebird photos:

1. Download lovebird images from:
   - [Pixabay](https://pixabay.com/images/search/lovebird/)
   - [Unsplash](https://unsplash.com/s/photos/lovebird)
   - [Pexels](https://www.pexels.com/search/lovebird/)

2. Replace files in `images/` folder with your lovebird photos

3. Name them: `lovebird_01.jpg`, `lovebird_02.jpg`, etc.

4. Supported formats: `.jpg`, `.png`

## Tech Stack

- **Python 3.9+**
- **Flask** - Web framework
- **Flask-CORS** - CORS support
- **Gunicorn** - Production server

## License

MIT License - Feel free to use for any purpose!

---

Made with 💚 for lovebird lovers
