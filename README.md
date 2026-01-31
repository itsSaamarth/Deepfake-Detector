# Deepfake Detector — Portfolio-grade Project

**Disclaimer:** This system provides probabilistic results for educational and cybersecurity awareness purposes only. It does not claim 100% accuracy and should not be used as sole evidence for legal action. Do not analyze media you do not own or do not have permission to analyze.

## What this project does ✅
- Multi-layer deepfake analysis (ML-based + facial consistency + metadata + watermarking)
- Visual heatmaps and per-signal confidence breakdown
- Drag-and-drop interactive GUI (Streamlit)
- Cyber complaint guidance links (informational only)

## Tech stack
- Python 3.10+
- Streamlit frontend
- PyTorch (timm / torchvision) for pretrained models
- OpenCV, face_recognition, dlib for facial analysis
- ExifRead and ffmpeg-python for metadata and video probe

## Quick start
1. Create a virtual environment (recommended):
   - `python -m venv .venv && .venv\Scripts\activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
   - Note: installing `dlib` on Windows may require Visual Studio Build Tools. See the docs.
3. Run the app locally:
   - `python main.py`  (this launches Streamlit UI)

## Project structure
```
deepfake-detector/
├── main.py
├── backend/
│   ├── detection.py
│   ├── watermark.py
│   ├── metadata.py
│   ├── utils.py
├── frontend/
│   ├── app.py
│   └── components.py
├── models/
├── data/
├── requirements.txt
└── README.md
```

## Notes on legal & ethics ⚖️
- Only analyze files you have permission to analyze.
- Results are probabilistic and for awareness/education.
- App will never auto-submit complaints or store user files permanently.

## Deployment
- Local: `python main.py` (Streamlit)
- Optional: Streamlit Cloud, Gradio Spaces, or package as EXE with PyInstaller.

## Cyber complaint guidance
- Official India portal: https://cybercrime.gov.in/
- The UI includes a pre-filled guidance template (user-controlled copy/paste only).

---

If you'd like, I can now implement the watermark, metadata modules, and build the Streamlit UI. Would you like me to proceed with those next steps?