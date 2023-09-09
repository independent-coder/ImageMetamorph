from PIL import Image
import os
import argparse


def convert_image(input_path, output_filename, output_extension, resolution=None):
    try:
        # Open the image
        image = Image.open(input_path)

        # Set the resolution if provided
        if resolution:
            image = image.resize(resolution)

        # Build the output path with the desired extension
        output_path = f"{output_filename}.{output_extension.lower()}"

        # Save the image
        image.save(output_path)
        print(f"Image converted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Extension Converter")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("output_filename", help="Name of the output file (without extension)")
    parser.add_argument("output_extension", help="Desired output image extension (e.g., 'png', 'jpg')")
    parser.add_argument("--resolution", nargs=2, type=int, metavar=("width", "height"),
                        help="Desired image resolution (width and height)")

    args = parser.parse_args()

    convert_image(args.input_image, args.output_filename, args.output_extension, args.resolution)
