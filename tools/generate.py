
import argparse
import os
from diffoxen.model.stable_diffusion import load_model, generate


def main():
    parser = argparse.ArgumentParser(prog='Generate an image from stable diffusion')
    
    parser.add_argument('-p', '--prompt', required=True)
    parser.add_argument('-m', '--model', required=True)
    parser.add_argument('-n', '--num_images_per_prompt', type=int, default=1)
    parser.add_argument('-o', '--output', required=True)
    args = parser.parse_args()

    model = load_model(args.model)
    images = generate(
        model,
        args.prompt,
        num_images_per_prompt=args.num_images_per_prompt
    )

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for i, image in enumerate(images):
        filename = os.path.join(args.output, f"img_{i}.png")
        print(f"Saving {filename}")
        image.save(filename)

if __name__ == "__main__":
    main()
