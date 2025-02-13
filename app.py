import os
import re
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from youtube_transcript_api import YouTubeTranscriptApi
import gradio as gr

from dotenv import load_dotenv
load_dotenv()
from src.utils.youtube_utils import extract_video_id, get_transcript
from src.utils.text_utils import split_text
from src.models.openai_langchain import summarize_openai

def get_transcript_only(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL", ""

    # Try getting the transcript in English, fallback to auto-generated Spanish if unavailable
    transcript = get_transcript(video_id, language='en')
    if "Error" in transcript:
        transcript = get_transcript(video_id, language='es')

    if transcript.startswith("Error"):
        return transcript, ""

    return transcript, ""

def summarize_transcript(transcript):
    if not transcript:
        return "No transcript available to summarize"

    chunks = split_text(transcript)
    summaries = []
    for chunk in chunks:
        summary = summarize_openai(chunk)
        summaries.append(summary)

    full_summary = " ".join(summaries)
    return full_summary

with gr.Blocks() as app:
    gr.HTML('<link rel="stylesheet" href="/static/styles.css">')
    gr.Markdown("# 🎬 VidSummarizer Pro: Summarize YouTube Videos with AI")
    with gr.Row():
        video_url = gr.Textbox(label="YouTube Video URL")
    with gr.Row():
        get_transcript_btn = gr.Button("Get Transcript", size="sm")
        summarize_btn = gr.Button("Summarize", size="sm")
    with gr.Row():
        transcript_output = gr.Textbox(label="Transcript", lines=15)
        summary_output = gr.Textbox(label="Summary", lines=15)

    get_transcript_btn.click(get_transcript_only, inputs=[video_url], outputs=[transcript_output, summary_output])
    summarize_btn.click(summarize_transcript, inputs=[transcript_output], outputs=[summary_output])

app.launch()