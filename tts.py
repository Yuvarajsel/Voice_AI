import threading
import queue
import numpy as np
import sounddevice as sd
from pynput import keyboard
from openai import OpenAI
import time

# 🔐 Add your keys
client = OpenAI(
    api_key="sk-8apyBxiOWjuhV0ZNOigdoQ",
    base_url="https://apidev.navigatelabsai.com/"
)

audio_queue = queue.Queue()
current_text = ""
lock = threading.Lock()

samplerate = 24000
channels = 1

# Debounce control
typing_timer = None
DELAY = 0.6  # seconds after stopping typing

# 🎧 Audio Playback
def audio_player():
    with sd.OutputStream(samplerate=samplerate,
                         channels=channels,
                         dtype="int16") as stream:
        while True:
            chunk = audio_queue.get()
            if chunk is None:
                break
            stream.write(chunk)

# 🎙️ Streaming TTS
def generate_tts_stream(text):
    try:
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text,
            response_format="pcm",
        ) as response:

            for audio_chunk in response.iter_bytes(chunk_size=4096):
                audio_np = np.frombuffer(audio_chunk, dtype=np.int16)
                audio_queue.put(audio_np)

    except Exception as e:
        print("TTS error:", e)

# 🧠 Called after user stops typing
def trigger_speech():
    global current_text
    with lock:
        text_snapshot = current_text.strip()
        current_text = ""

    if text_snapshot:
        threading.Thread(
            target=generate_tts_stream,
            args=(text_snapshot,),
            daemon=True
        ).start()

# ⌨️ Keyboard Listener
def on_press(key):
    global current_text, typing_timer

    try:
        char = key.char
    except AttributeError:
        return

    with lock:
        current_text += char

    # Reset debounce timer
    if typing_timer:
        typing_timer.cancel()

    typing_timer = threading.Timer(DELAY, trigger_speech)
    typing_timer.start()

# ▶️ Start audio thread
player_thread = threading.Thread(target=audio_player, daemon=True)
player_thread.start()

print("Start typing... It will speak automatically when you pause.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()