# YouTube Transcript API Microservice

This is a tiny, open-source Python microservice built with FastAPI and `youtube-transcript-api`. It provides a reliable, 100% free way to extract YouTube transcripts without needing API keys or dealing with YouTube's bot-blocking measures.

## How to deploy this for FREE on Render.com

Render.com provides free hosting for small web services perfect for this API.

1. Create a new GitHub repository and upload these 3 files (`main.py`, `requirements.txt`, `render.yaml`, `README.md`) to it.
2. Go to [Render.com](https://render.com/) and create a free account.
3. Click **New +** and select **Web Service**.
4. Connect your GitHub account and select the repository you just created.
5. Render will automatically detect it's a Python app.
6. Make sure the following settings are configured:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** `Free`
7. Click **Create Web Service**.

Render will build and deploy the API. Once it's live, you will get a URL like `https://your-api-name.onrender.com`.

## How to use this in your Supabase project

Once your Python API is live on Render, you just need to point your Supabase Edge Function to it!

In `supabase/functions/process-video/index.ts`, you can simply make a `fetch` request to your new API:

```typescript
const videoId = "LXb3EKWsInQ";
const apiUrl = `https://your-api-name.onrender.com/transcript/${videoId}`;

const response = await fetch(apiUrl);
const data = await response.json();

if (data.success) {
    console.log(data.fullText); // This goes straight to OpenRouter!
}
```
