from google.cloud import speech


def transcribe_audio(audio_bytes):
    client = speech.SpeechClient()

    # Loads the audio into memory
    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,  # Adjust this value if necessary
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    # Gather the transcription and return it
    transcripts = [result.alternatives[0].transcript for result in response.results]
    return transcripts


# EOF