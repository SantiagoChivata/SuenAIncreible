from suenaincreible.generators.images import generate_image
from suenaincreible.generators.audio import generate_audio
from suenaincreible.generators.video import create_video
from suenaincreible.utils.sheets import get_dreams

def main():
    # Obtener sueños desde Google Sheets
    dreams = get_dreams()

    for i, dream in enumerate(dreams):
        print(f"Procesando sueño {i+1}: {dream}")

        # Generar imagen
        image_path = generate_image(dream, output_path=f"outputs/image_{i+1}.png")

        # Generar narración
        audio_path = generate_audio(dream, output_path=f"outputs/audio_{i+1}.mp3")

        # Crear video
        video_path = create_video(image_path, audio_path, output_path=f"outputs/video_{i+1}.mp4")

        print(f"Video generado: {video_path}")

if __name__ == "__main__":
    main()