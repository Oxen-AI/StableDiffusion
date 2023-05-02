from diffusers import StableDiffusionPipeline
import torch

def load_model(name: str):
    pipe = StableDiffusionPipeline.from_pretrained(name, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    return pipe

def generate(model, prompt: str, num_images_per_prompt=1):
    images = model(
        prompt,
        num_images_per_prompt=num_images_per_prompt
    ).images
    print(f"generated {len(images)} images")
    return images
