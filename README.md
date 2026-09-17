# Image Toolkit

**Image Toolkit** is a local, privacy-first image compressor, converter, batch processor, and resizer built with Python and Pillow.

It is designed to work on **Termux/Android, Windows, Linux, macOS**, and other platforms with a supported Python installation.

## What makes it useful?

- Interactive terminal UI when you simply run `python image_tool.py`
- Full CLI for scripting and automation
- JPEG, PNG, WebP, and AVIF output
- Keep original format
- Quality control from 1–100
- Target-size compression
- Target-size presets: **100 KB, 200 KB, 500 KB, 1 MB**
- Custom target sizes such as `750KB` or `2MB`
- Target-size mode searches for the **highest quality that fits**
- Automatic dimension reduction when necessary
- Never upscales
- Batch processing
- Recursive directory processing
- Multiple input files/directories
- EXIF/metadata removal by default
- Optional metadata preservation
- Safe output handling
- Does not overwrite source files by default
- Existing output gets a numbered filename unless `--overwrite`
- Larger compressed files are discarded by default
- Dry-run mode
- Detailed per-file and batch summaries
- Local processing; images are not uploaded to a compression website

---

# 1. Requirements

You need:

- Python **3.10 or newer** recommended
- `pip`
- `venv` support
- Pillow, installed inside the project's virtual environment

The application itself is Python-based, so the same project can be used across supported operating systems.

> **Important:** This project intentionally uses a virtual environment. Do not install the project's Python requirements globally unless you specifically know why you want to.

---

# 2. Download / extract the project

After downloading `image-toolkit-final.zip`, extract it.

You should have:

```text
image-toolkit/
├── image_tool.py
├── image_tool/
├── input/
├── output/
├── tests/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

Open a terminal inside the `image-toolkit` directory.

---

# 3. Termux / Android installation

## 3.1 Install Termux

Use a current Termux installation from a trusted source such as F-Droid or the official Termux project distribution.

Then open Termux.

## 3.2 Install Python

```bash
pkg update
pkg upgrade
pkg install python
```

Check:

```bash
python --version
```

## 3.3 Enter the project

If the project is in your Termux home directory:

```bash
cd ~/image-toolkit
```

If it is somewhere else, use that directory.

## 3.4 Create the virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should now see something similar to:

```text
(.venv) $
```

## 3.5 Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3.6 Run

Interactive UI:

```bash
python image_tool.py
```

CLI help:

```bash
python image_tool.py --help
```

## 3.7 Android shared storage

If you want to access files in Android shared storage:

```bash
termux-setup-storage
```

Termux will ask for storage permission.

Your shared storage is normally accessible through:

```text
~/storage/shared/
```

The project's default paths are:

```text
~/workspace/storage/shared/imageCompressor
~/workspace/storage/shared/imageCompressed
```

You can also supply an Android shared-storage directory explicitly:

```bash
python image_tool.py ~/storage/shared/Pictures
```

When finished:

```bash
deactivate
```

---

# 4. Windows installation

## 4.1 Install Python

Install Python 3.10+ from the official Python distribution for Windows.

During installation, enable the option that adds Python to `PATH`.

Verify:

```powershell
python --version
```

If `python` is unavailable, try:

```powershell
py --version
```

## 4.2 Open the project directory

PowerShell example:

```powershell
cd C:\path\to\image-toolkit
```

## 4.3 Create a virtual environment

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

If you are using Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

## 4.4 Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4.5 Run

```powershell
python image_tool.py
```

CLI:

```powershell
python image_tool.py --help
```

Deactivate:

```powershell
deactivate
```

---

# 5. Linux installation

This applies to common Linux distributions such as Ubuntu, Debian, Fedora, Arch, and similar systems.

First check:

```bash
python3 --version
```

If Python is not installed, install Python and the virtual-environment package using your distribution's package manager.

For Ubuntu/Debian, for example:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Then:

```bash
cd ~/image-toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python image_tool.py
```

Deactivate:

```bash
deactivate
```

---

# 6. macOS installation

Check Python:

```bash
python3 --version
```

If needed, install a current Python 3 release using the official Python installer or your preferred package manager.

Then:

```bash
cd ~/image-toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python image_tool.py
```

Deactivate:

```bash
deactivate
```

---

# 7. Other supported devices / operating systems

The application is a Python program and can generally run anywhere that provides:

1. Python 3.10+
2. `venv`
3. `pip`
4. A supported Pillow build

Examples include:

- Windows
- Linux
- macOS
- Termux / Android
- Linux-based servers
- WSL
- Raspberry Pi and similar Linux systems

The exact Python installation command differs by platform.

---

# 8. Interactive terminal UI

Running:

```bash
python image_tool.py
```

without arguments opens the interactive UI.

Example:

```text
╔════════════════════════════════════════════════════╗
║              IMAGE TOOLKIT v1.0.0                 ║
║       Local • Private • Compression Tool          ║
╚════════════════════════════════════════════════════╝

What would you like to do?

  1. Compress images
  2. Convert image format
  3. Compress to target size
  4. Batch compress
  5. Batch convert
  6. Resize images
  7. Advanced options
  8. Exit

Choice:
```

The UI asks for the input, format, quality/target size, privacy options, filename behavior, output directory, and safety settings.

Invalid input is requested again rather than silently choosing a wrong value.

---

# 9. Target-size presets

Interactive target-size mode provides:

```text
Target file size

  1. 100 KB
  2. 200 KB
  3. 500 KB
  4. 1 MB
  5. Custom size
```

For example:

```text
Choice: 2
```

means:

```text
Target: 200 KB
```

The compressor then searches for the **highest quality that produces an output at or below 200 KB**.

The CLI supports the same feature:

```bash
python image_tool.py --format webp --target-size 200KB
```

Other examples:

```bash
python image_tool.py --format webp --target-size 100KB
python image_tool.py --format webp --target-size 500KB
python image_tool.py --format webp --target-size 1MB
python image_tool.py --format webp --target-size 750KB
```

Do not combine:

```text
--quality
```

with:

```text
--target-size
```

because target-size mode determines quality automatically.

---

# 10. How target-size compression works

For lossy formats such as JPEG, WebP, and AVIF:

1. The image is encoded at different quality levels.
2. The tool uses binary search.
3. It looks for the highest quality that fits the requested target.
4. If even quality 1 is too large, dimensions are progressively reduced.
5. The tool retries the quality search.
6. If the target still cannot be reached, it reports:

```text
target=NOT REACHED
```

It never falsely reports that the target was achieved.

For example:

```text
[OK] photo.jpg -> photo_compressed.webp |
2.40 MB -> 198.32 KB |
91.94% saved |
target=OK | q=73 | 1920x1280
```

---

# 11. Quality mode

Example:

```bash
python image_tool.py --format webp --quality 80
```

Quality range:

```text
1 - 100
```

Higher quality generally means larger output.

The default quality is:

```text
80
```

This is a default, **not a fixed quality**.

---

# 12. Format conversion

WebP:

```bash
python image_tool.py --format webp --quality 80
```

JPEG:

```bash
python image_tool.py --format jpeg --quality 80
```

PNG:

```bash
python image_tool.py --format png
```

AVIF:

```bash
python image_tool.py --format avif --quality 70
```

Original format:

```bash
python image_tool.py --format original
```

---

# 13. Filename behavior

Default:

```text
photo.jpg
        ↓
photo_compressed.webp
```

With:

```bash
--filename original
```

the result becomes:

```text
photo.jpg
        ↓
photo.webp
```

The extension follows the selected output format.

Custom suffix:

```bash
python image_tool.py --format webp --suffix _optimized
```

Result:

```text
photo_optimized.webp
```

---

# 14. Batch processing

Directory:

```bash
python image_tool.py ~/Pictures --format webp --quality 80
```

Multiple files:

```bash
python image_tool.py photo1.jpg photo2.png photo3.webp
```

Recursive directory processing:

```bash
python image_tool.py ~/Pictures --recursive --format webp
```

---

# 15. Resize

Maximum width:

```bash
python image_tool.py --max-width 1920
```

Maximum dimensions:

```bash
python image_tool.py --max-width 1920 --max-height 1080
```

The tool does not upscale smaller images.

---

# 16. Privacy / EXIF

EXIF and common image metadata are removed by default.

This is intentional because image metadata can contain information such as camera information, timestamps, and sometimes location-related data.

Default behavior:

```text
EXIF: Remove
```

To request metadata preservation:

```bash
python image_tool.py --keep-exif
```

Metadata behavior can vary between image formats and Pillow codecs.

For privacy-sensitive processing, keep the default metadata-removal behavior.

---

# 17. Output safety

The source image is not overwritten by default.

If:

```text
photo_compressed.webp
```

already exists, the tool creates:

```text
photo_compressed_1.webp
```

then:

```text
photo_compressed_2.webp
```

and so on.

To allow overwriting an existing destination:

```bash
python image_tool.py --overwrite
```

If the compressed output is larger than the original, it is discarded by default.

To keep larger outputs:

```bash
python image_tool.py --allow-larger
```

---

# 18. Dry run

Preview operations without writing files:

```bash
python image_tool.py --format webp --quality 80 --dry-run
```

Example:

```text
[DRY RUN] photo.jpg -> photo_compressed.webp
```

---

# 19. AVIF note

AVIF support depends on the Pillow build and available image codec support on the platform.

If AVIF encoding is unavailable, the tool will report an encoding error.

JPEG, PNG, and WebP are generally the simpler choices when maximum cross-platform codec compatibility is required.

---

# 20. Running tests

Inside the virtual environment:

```bash
python -m pytest
```

If pytest is not installed, install it separately inside the virtual environment if you want to run the tests:

```bash
python -m pip install pytest
```

The runtime application itself only requires the dependency listed in `requirements.txt`.

---

# 21. Recommended daily workflow

### Termux

```bash
cd ~/image-toolkit
source .venv/bin/activate
python image_tool.py
```

### Windows PowerShell

```powershell
cd C:\path\to\image-toolkit
.venv\Scripts\Activate.ps1
python image_tool.py
```

### Linux / macOS

```bash
cd ~/image-toolkit
source .venv/bin/activate
python image_tool.py
```

When finished:

```bash
deactivate
```

---

# 22. CLI quick reference

```text
python image_tool.py
python image_tool.py --help

python image_tool.py IMAGE
python image_tool.py DIRECTORY

python image_tool.py --format webp --quality 80
python image_tool.py --format jpeg --quality 70

python image_tool.py --format webp --target-size 100KB
python image_tool.py --format webp --target-size 200KB
python image_tool.py --format webp --target-size 500KB
python image_tool.py --format webp --target-size 1MB

python image_tool.py --recursive
python image_tool.py --max-width 1920
python image_tool.py --max-height 1080

python image_tool.py --filename original
python image_tool.py --overwrite
python image_tool.py --allow-larger
python image_tool.py --dry-run
python image_tool.py --keep-exif
```

---

# 23. Privacy architecture

The intended processing flow is:

```text
Your device
    │
    ▼
Image Toolkit
    │
    ├── Read image
    ├── Correct EXIF orientation
    ├── Remove metadata by default
    ├── Resize if requested
    ├── Compress / convert
    └── Write output
    │
    ▼
Your device
```

There is no requirement for an online image-compression service.

---

# 24. License

MIT License. See `LICENSE`.

## Version

1.0.0
