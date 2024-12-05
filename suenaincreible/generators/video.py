import subprocess

def create_video(image_path, audio_path, output_path="outputs/video.mp4"):
    """Combina una imagen y un audio en un video."""
    cmd = [
        "ffmpeg",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_path
    ]
    subprocess.run(cmd)
    return output_path