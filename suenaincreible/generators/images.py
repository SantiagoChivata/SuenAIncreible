from diffusers import StableDiffusionPipeline

def generate_image(prompt, output_path="outputs/image.png"):
    """Genera una imagen basada en un prompt y la guarda en el disco."""
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe.to("cuda")  # Usa GPU para mejor rendimiento
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
