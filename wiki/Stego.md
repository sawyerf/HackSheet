<img height="100px" src="https://user-images.githubusercontent.com/28403617/172732375-620951b9-2edf-4ed6-952b-0199a7ce0721.svg#gh-light-mode-only" />
<img height="100px" src="https://user-images.githubusercontent.com/28403617/172732374-0737b581-3054-42e7-b3ba-b15b4a75253e.svg#gh-dark-mode-only" />

---

- [Brute force](#brute-force)
- [Compare 2 Images](#compare-2-images)
- [Exif or meta-data](#exif-or-meta-data)
- [Hidden data](#hidden-data)
- [Web tools](#web-tools)

## Exif or meta-data
```bash
exiftool image.png
strings image.png
zipinfo archive.zip
exiv2 image.jpg
```

## Hidden data
```bash
binwalk image.jpg
steghide info image.jpg
zsteg -a file
stegsolve.jar # link in web tools section
```

### Extract hidden data
```bash
binwalk -e image.jpg
steghide extract -sf image.jpg
zsteg -E file.png
foremost -v file
```

## Compare 2 Images
```bash
compare -metric mae image1.png image2.png difference.png
```
[source](https://www.imagemagick.org/script/compare.php)

## Brute force
### Images
```bash
stegcracker image.jpg
```

### Zip
```bash
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt archive.zip
```

## Web tools

- [Unicode steganography](https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder)
- [Dcode](https://www.dcode.fr/)
- [Unhide images inside other images](https://incoherency.co.uk/image-steganography/#unhide)
- [Reverse search image](https://tineye.com/)
- [Steganographic Decoder](https://futureboy.us/stegano/decinput.html)
- [Npiet](https://www.bertnase.de/npiet/npiet-execute.php)
- [stegsolve](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve)
