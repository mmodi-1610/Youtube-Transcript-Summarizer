from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.transcript import get_transcript
from app.summarizer import summarize_with_together

app = FastAPI()

# 👇 Add this section to allow requests from your Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["chrome-extension://<your-extension-id>"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Summarizer running"}

@app.get("/summarize")
def summarize(video_id: str):
    text = get_transcript(video_id)
    summary = summarize_with_together(text)
    return {"video_id": video_id, "summary": summary}
