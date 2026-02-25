
A comprehensive repository for hands-on practice with **Voice AI** concepts, developed as part of the Navigate Labs training program. This project showcases the integration of Speech-to-Text (STT), Text-to-Speech (TTS), and functional tool calling to build intelligent voice-driven applications.

---

## 🚀 Key Features

*   **Real-time Streaming TTS**: Dynamic audio playback with low-latency streaming using OpenAI's `gpt-4o-mini-tts`.
*   **SSML Mastery**: Advanced voice customization using Speech Synthesis Markup Language for expressive and natural speech.
*   **ASR Benchmarking**: Comparative analysis of state-of-the-art Automatic Speech Recognition models (**Whisper-1** vs. **Wav2Vec2**).
*   **Voice-Enabled Tools**: A smart traffic assistant that fetches real-time route data using voice commands and the **OpenRouteService API**.
*   **Metrics-Driven Evaluation**: Quantifiable performance assessment using **WER** (Word Error Rate), **CER** (Character Error Rate), and **RTF** (Real Time Factor).

---

## 📂 Project Structure

```bash
Voice_AI/
├── ASR_Evaluation.ipynb           # Comparative analysis of Whisper and Wav2Vec2
├── TTS&SST_Using_Route_API.ipynb  # End-to-end voice navigation assistant
├── sslm.py                       # SSML implementation for natural speech
├── tts.py                         # Real-time streaming TTS from keyboard input
├── otp_audio.mp3                  # Sample generated audio output
└── README.md                      # Professional documentation
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites
*   Python 3.8 or higher
*   OpenAI API Key
*   OpenRouteService API Key (for navigation features)

### 2. Install Dependencies
```bash
pip install openai requests numpy sounddevice pynput jiwer librosa transformers torch torchaudio soundfile
```

> [!NOTE]
> For `sounddevice`, you may need system-level audio libraries (e.g., `libportaudio2` on Linux/Ubuntu).

---

## 📖 Module Overviews

### 🤖 Voice Navigation Assistant
*   **File**: `TTS&SST_Using_Route_API.ipynb`
*   **Flow**: Speech Input → Whisper STT → Intent Detection → Traffic Tool (ORS) → gpt-4o-mini-tts → Voice Output.
*   **Functionality**: Automatically calculates distance and travel time between locations via voice commands.

### 🎧 Real-Time Streaming TTS
*   **File**: `tts.py`
*   **Usage**: Run the script and start typing. The assistant will stream voice output automatically when you pause.
*   **Tech**: Uses `threading` and `queue` for seamless, non-blocking audio generation and playback.

### 🎼 SSML & Voice Customization
*   **File**: `sslm.py`
*   **Usage**: Demonstrates complex speech patterns like emphasis, breaks, and digit interpretation (e.g., for OTP delivery).

### 📊 ASR Model Benchmarking
*   **File**: `ASR_Evaluation.ipynb`
*   **Models**: OpenAI Whisper-1 vs. Facebook Wav2Vec2.
*   **Metrics**: Provides detailed tables comparing WER, CER, and RTF to determine model efficiency for specific use cases.

---

## 🔒 Security & Best Practices

> [!WARNING]
> Do not share your API keys publicly. 

It is highly recommended to use environment variables or Colab Secrets instead of hardcoding keys:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL")
)
```

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions or want to add more Voice AI features, please open a pull request or file an issue.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Developed as part of the Navigate Labs AI training program.*
