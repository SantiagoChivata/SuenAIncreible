from TTS.api import TTS

def generate_audio(text, output_path="outputs/narration.mp3"):
    """Genera un archivo de audio a partir de texto."""
    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path
