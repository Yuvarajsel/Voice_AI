from openai import OpenAI
#from IPython.display import Audio
import base64

client = OpenAI(
    api_key="sk-8apyBxiOWjuhV0ZNOigdoQ",
    base_url="https://apidev.navigatelabsai.com"
)

ssml_text = """
<speak>
  Your 
  <emphasis level="moderate">one time password</emphasis> 
  is
  <break time="400ms"/>

  <prosody rate="slow">
    <emphasis level="strong">
      <say-as interpret-as="digits">4821</say-as>
    </emphasis>
  </prosody>

  <break time="600ms"/>

  It expires in 
  <emphasis level="moderate">
    <say-as interpret-as="time">30s</say-as>
  </emphasis>.
</speak>
"""

response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=ssml_text
)

with open("otp_audio.mp3", "wb") as f:
    f.write(response.content)

print("Audio generated successfully.")
#Audio("otp_audio.mp3", autoplay=True)