from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
import uvicorn
import os

app = FastAPI(title="YouTube Transcript API")

# Allow requests from your main application (or everywhere for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "YouTube Transcript API is running."}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    try:
        # Fetch the transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine the text into a single string for easy processing by OpenRouter
        full_text = " ".join([item['text'] for item in transcript_list])
        
        # Return the original array and the full combined string
        return {
            "success": True,
            "video_id": video_id,
            "entries": transcript_list,
            "fullText": full_text
        }
        
    except Exception as e:
        error_msg = str(e)
        print(f"Error fetching transcript for {video_id}: {error_msg}")
        raise HTTPException(status_code=400, detail=error_msg)

if __name__ == "__main__":
    # Render specifies the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
