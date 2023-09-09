# ImageMetamorph

ImageMetamorph is a versatile command-line tool for effortlessly converting image formats and resolutions. Whether you need to change the format of your images or adjust their resolution, ImageMetamorph simplifies the process with ease.

## Features

- **Format Conversion:** Convert your images from a wide range of input formats to output formats of your choice.

- **Resolution Adjustment:** Resize your images by specifying the desired width and height.

## Supported Input Image Formats

ImageMetamorph supports a variety of input image formats, including:

- JPEG (Joint Photographic Experts Group)
- PNG (Portable Network Graphics)
- GIF (Graphics Interchange Format)
- BMP (Bitmap Image File)
- TIFF (Tagged Image File Format)
- WebP (Web Picture format)
- ICO (Windows Icon)
- ... and more.

## Supported Output Image Formats

ImageMetamorph provides flexibility when it comes to output image formats. You can convert your images to popular formats like:

- JPEG (Joint Photographic Experts Group)
- PNG (Portable Network Graphics)
- GIF (Graphics Interchange Format)
- BMP (Bitmap Image File)
- TIFF (Tagged Image File Format)
- WebP (Web Picture format)
- ICO (Windows Icon)
- ... and more.


## Installation
First download the github repo using git
```bash
git clone https://github.com/independent-coder/ImageMetamorph.git
```
Then download the latest version of [Python](https://www.python.org/downloads/)
Lastly download the pillow library
```bash
pip install pillow
```


## Usage

Here's how you can use ImageMetamorph from the command line:

```bash
python image_metamorph.py input_image.jpg output_image png --resolution 800 600
```
input_image.jpg is the path to your input image.

output_image is the desired output filename (without extension).

png is the desired output extension (you can use other extensions like jpg, gif, etc.).

--resolution is an optional argument where you can specify the desired image resolution as width and height. If not provided, the image will retain its original resolution.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/independent-coder/ImageMetamorph/blob/main/LICENSE) file for details.
