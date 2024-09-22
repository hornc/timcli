# TIMcli
Simple PSX TIM image format cli tool to view basic info and modify VRAM offsets.

This simple Python tool does not convert between image formats. It was designed to display basic
info about pre-existing TIM images, and modify the VRAM offsets from default 0,0 or between
video modes and other layouts. It does not have any external Python dependencies, just standard libraries.

It was also an excercise in confirming I understood the TIM file format, and allows
debug code to be easily hacked in Python for quick testing and troubleshooting.

Has only been tested on Linux, and not yet with 16 or 24bit images, although it should work
on other platforms and with all valid TIM images.

I am happy to make or accept changes to fix compaitibilty issues and make this more widely useful.

For TIM image conversions from other formats you might want to use Lameguy64's C++ tool: [IMG2TIM](https://github.com/Lameguy64/img2tim), or
try the [Gimp TIM plugin](https://github.com/hornc/psxdev/tree/master/psxdev-gimp-2.0.0) which I have tried
to bring up to date with recent versions of Gimp, but probably needs some more attention to be fully
functional.

### For future versions?
* Palette adjustmets, re-writing etc


## Installation

    $ pip install .

## Usage

### Help

    $ timcli -h

```
usage: timcli [-h] [-d] [-org ORG ORG] [-plt PLT PLT] [-o OUTPUT] file

PSX TIM image file format command line utility.

positional arguments:
  file                  TIM file to process

options:
  -h, --help            show this help message and exit
  -d, --debug           turn on debug output
  -org ORG ORG          VRAM <x y> offset of the image (Default: 640 0)
  -plt PLT PLT          VRAM <x y> offset of the CLUT (Default: 0 480)
  -o OUTPUT, --output OUTPUT
                        output file to write to
```

### TIM file info

    $ timcli texture64_320x240-NTSC.tim

```
TIM: texture64_320x240-NTSC.tim

     File size:    2112 bytes
          Size: w:   64 h:  64
     Bit depth:       4 (color indices)
  Image origin: x:  640 y:   0
Palette origin: x:    0 y: 480
```

### Image / CLUT offset rewrite

    $ timcli texture64_320x240-NTSC.tim -o texture64_320x256-PAL.tim -org 320 0 -plt 320 256

This copies `texture64_320x240-NTSC.tim` to a new file `texture64_320x256-PAL.tim` with a modified image VRAM location of X:320, Y:0
and a CLUT (palette) location of X: 320, Y: 256, which is something you might want to do if you are reusing a TIM image with double-buffered
NTSC VRAM locations to a VRAM configuration which works for a double-buffered PAL mode.

Copyright 2024 Charles Horn, [MIT licence](LICENSE)
