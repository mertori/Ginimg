# GiniMG - Gini IMG

GiniMG is a **local, privacy-first image compressor, converter, batch processor, and resizer** built with Python and Pillow.

It is designed to work on:

- Termux / Android
- Windows
- Linux
- macOS
- WSL
- Raspberry Pi and other Python-supported systems

All image processing happens locally on your device. Images do not need to be uploaded to an online compression service.

---

## ✨ Features

- 🖼️ Image compression
- 🔄 Image format conversion
- 📦 Batch processing
- 📁 File and directory input
- 🔁 Recursive directory processing
- 🎯 Target-size compression
- ⚙️ Quality control from 1–100
- 📏 Maximum width / height resizing
- 🔐 EXIF and common metadata removal by default
- 📝 Custom output filenames
- 🛡️ Source-file protection
- 🚫 Prevents larger compressed files by default
- 👀 Dry-run mode
- 💻 Interactive terminal UI
- ⌨️ Full CLI support
- 🌐 Cross-platform
- 🔒 Local/offline processing

### Supported output formats

- JPEG
- PNG
- WebP
- AVIF
- Original format

Input support includes common image formats such as:

- JPG / JPEG
- PNG
- WebP
- AVIF
- BMP
- GIF
- TIFF

---

# 📥 Installation

There are two main ways to get GiniMG:

1. **Clone the Git repository**
2. **Download the repository as ZIP**

The recommended development/user workflow is Git.

---

# 🚀 Method 1 — Git Clone

First make sure Git is installed.

Check:

```bash
git --version
```

Then clone the repository:

```bash
git clone https://github.com/Ginimg/Ginimg.git
```

Enter the project:

```bash
cd Ginimg
```

> If your GitHub repository uses a different URL, replace the clone URL with your repository's actual HTTPS or SSH URL.

---

## Git clone using SSH

If you have already configured an SSH key with GitHub:

```bash
git clone git@github.com:Ginimg/Ginimg.git
```

Then:

```bash
cd Ginimg
```

---

# 📦 Method 2 — Download ZIP

You can also download the repository as a ZIP from GitHub.

After extracting it:

```bash
cd Ginimg
```

Then continue with the platform-specific setup below.

---

# 📱 Termux / Android

## 1. Install Termux

Install a current Termux version from a trusted source such as F-Droid or the official Termux project distribution.

Open Termux and update packages:

```bash
pkg update
pkg upgrade
```

Install Git and Python:

```bash
pkg install git python
```

Verify:

```bash
git --version
python --version
```

---

## 2. Clone GiniMG

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
```

---

## 3. Create a virtual environment

GiniMG should **not** install its Python dependencies globally.

Create the environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should see something similar to:

```text
(.venv) $
```

---

## 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 5. Run GiniMG

Interactive mode:

```bash
python image_tool.py
```

No arguments are required.

GiniMG will open its terminal UI and guide you through the process.

---

## 6. Android shared storage

To access Android shared storage:

```bash
termux-setup-storage
```

Allow the requested Android permission.

You can then access shared storage through:

```text
~/storage/shared/
```

For example:

```bash
python image_tool.py ~/storage/shared/Pictures
```

---

## 7. Leave the virtual environment

```bash
deactivate
```

When using GiniMG again:

```bash
cd ~/Ginimg
source .venv/bin/activate
python image_tool.py
```

---

# 🪟 Windows

## 1. Install Git

Install Git for Windows and verify:

```powershell
git --version
```

## 2. Install Python

Install Python 3.10 or newer.

Verify:

```powershell
python --version
```

---

## 3. Clone GiniMG

```powershell
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
```

---

## 4. Create the virtual environment

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or in Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

---

## 5. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 6. Run

```powershell
python image_tool.py
```

Deactivate:

```powershell
deactivate
```

---

# 🐧 Linux

Install Git and Python using your distribution's package manager.

For Ubuntu / Debian:

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

Verify:

```bash
git --version
python3 --version
```

Clone:

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
```

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run:

```bash
python image_tool.py
```

Deactivate:

```bash
deactivate
```

---

# 🍎 macOS

Check Git:

```bash
git --version
```

Check Python:

```bash
python3 --version
```

Clone:

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
```

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run:

```bash
python image_tool.py
```

Deactivate:

```bash
deactivate
```

---

# 🐧 Windows Subsystem for Linux (WSL)

Inside WSL:

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

Then:

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python image_tool.py
```

---

# 🍓 Raspberry Pi / Other Linux Devices

Install:

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

Clone:

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
```

Create the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run:

```bash
python image_tool.py
```

---

# 🖥️ Interactive Terminal UI

Running:

```bash
python image_tool.py
```

without command-line arguments launches the interactive interface.

Example:

```text
╔════════════════════════════════════════════════════╗
║              GiniMG - Gini IMG                   ║
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

The UI guides the user through:

- Input path
- File/directory selection
- Recursive processing
- Output format
- Compression quality
- Target size
- EXIF/metadata handling
- Filename behavior
- Output directory
- Overwrite behavior
- Larger-output handling
- Dry-run mode

---

# 🎯 Target-Size Compression

GiniMG can automatically determine the compression quality required to reach a target file size.

Interactive presets:

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

sets:

```text
Target: 200 KB
```

The tool searches for the **highest quality that produces an output at or below the target**.

---

## CLI target-size examples

```bash
python image_tool.py --format webp --target-size 100KB
```

```bash
python image_tool.py --format webp --target-size 200KB
```

```bash
python image_tool.py --format webp --target-size 500KB
```

```bash
python image_tool.py --format webp --target-size 1MB
```

Custom:

```bash
python image_tool.py --format webp --target-size 750KB
```

`--quality` and `--target-size` cannot be used together.

---

# 🧠 How target-size compression works

For lossy formats such as JPEG, WebP, and AVIF:

1. GiniMG encodes the image at different quality levels.
2. It uses a binary-search strategy.
3. It finds the highest quality that fits the requested target.
4. If quality 1 is still too large, it reduces the image dimensions.
5. It repeats the search.
6. If the target still cannot be reached, it reports that honestly.

Example:

```text
[OK] photo.jpg -> photo_compressed.webp
2.40 MB -> 198.32 KB
91.94% saved
target=OK
q=73
1920x1280
```

If impossible:

```text
target=NOT REACHED
```

GiniMG does not falsely claim that a target was achieved.

---

# ⚙️ Quality Compression

Quality ranges from:

```text
1 - 100
```

Example:

```bash
python image_tool.py --format webp --quality 80
```

Default quality:

```text
80
```

The default is configurable and is not a fixed compression level.

---

# 🔄 Format Conversion

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

# 📦 Batch Processing

Process a directory:

```bash
python image_tool.py ~/Pictures --format webp --quality 80
```

Multiple files:

```bash
python image_tool.py photo1.jpg photo2.png photo3.webp
```

Recursive processing:

```bash
python image_tool.py ~/Pictures --recursive --format webp
```

---

# 📏 Resize

Maximum width:

```bash
python image_tool.py --max-width 1920
```

Maximum height:

```bash
python image_tool.py --max-height 1080
```

Both:

```bash
python image_tool.py --max-width 1920 --max-height 1080
```

GiniMG never upscales an image.

---

# 🔐 Privacy and Metadata

GiniMG removes EXIF and common image metadata by default.

This helps reduce accidental exposure of information that can be stored inside image metadata.

Default:

```text
EXIF: Remove
```

To request metadata preservation:

```bash
python image_tool.py --keep-exif
```

Metadata behavior depends on the input and output format and the capabilities of the installed Pillow build.

For privacy-sensitive workflows, the default metadata-removal behavior is recommended.

---

# 🛡️ Output Safety

GiniMG does not overwrite the source image by default.

If the destination already exists:

```text
photo_compressed.webp
photo_compressed_1.webp
photo_compressed_2.webp
```

Use:

```bash
python image_tool.py --overwrite
```

if replacing an existing destination is explicitly desired.

---

# 📈 Larger Output Protection

If compression produces a file larger than the original, GiniMG discards it by default.

Example:

```text
[SKIP LARGER]
```

To keep the larger output:

```bash
python image_tool.py --allow-larger
```

---

# 👀 Dry Run

Preview the operation without creating output files:

```bash
python image_tool.py --format webp --quality 80 --dry-run
```

Example:

```text
[DRY RUN] photo.jpg -> photo_compressed.webp
```

---

# 📝 Filename Options

Default:

```text
photo.jpg
↓
photo_compressed.webp
```

Keep the original base filename:

```bash
python image_tool.py --format webp --filename original
```

Result:

```text
photo.jpg
↓
photo.webp
```

Custom suffix:

```bash
python image_tool.py --format webp --suffix _optimized
```

Result:

```text
photo_optimized.webp
```

The output extension follows the selected format.

---

# 💻 CLI Usage

Show help:

```bash
python image_tool.py --help
```

Show version:

```bash
python image_tool.py --version
```

Compress:

```bash
python image_tool.py photo.jpg --format webp --quality 80
```

Convert:

```bash
python image_tool.py photo.png --format jpeg --quality 85
```

Target 200 KB:

```bash
python image_tool.py photo.jpg --format webp --target-size 200KB
```

Recursive batch:

```bash
python image_tool.py ~/Pictures --recursive --format webp --quality 80
```

Resize:

```bash
python image_tool.py ~/Pictures --recursive --max-width 1920
```

Dry run:

```bash
python image_tool.py ~/Pictures --recursive --format webp --dry-run
```

---

# 🔄 Updating GiniMG with Git

If you cloned the repository:

```bash
cd Ginimg
git pull
```

Then activate the environment:

```bash
source .venv/bin/activate
```

Update dependencies:

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python image_tool.py
```

---

# 🌿 Checking Git Status

```bash
git status
```

View recent commits:

```bash
git log --oneline
```

View remote repository:

```bash
git remote -v
```

---

# 🌐 Using a Different Branch

List branches:

```bash
git branch -a
```

Switch branch:

```bash
git switch main
```

Update:

```bash
git pull
```

---

# 🧪 Tests

Inside the virtual environment:

```bash
python -m pytest
```

If pytest is not installed:

```bash
python -m pip install pytest
```

The runtime application itself only requires the packages listed in `requirements.txt`.

---

# 📂 Project Structure

```text
Ginimg/
│
├── image_tool.py
├── image_tool/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── discovery.py
│   ├── engine.py
│   ├── formats.py
│   ├── metadata.py
│   ├── naming.py
│   └── validation.py
│
├── input/
│   └── .gitkeep
│
├── output/
│   └── .gitkeep
│
├── tests/
│   ├── test_naming.py
│   └── test_size_parser.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

The internal Python package currently uses the `image_tool` module name for compatibility with the implementation.

---

# 🔒 Local / Privacy-First Architecture

GiniMG is designed around local processing:

```text
Your device
     │
     ▼
   GiniMG
     │
     ├── Read image
     ├── Correct orientation
     ├── Remove metadata
     ├── Resize if requested
     ├── Compress / convert
     └── Write output
     │
     ▼
Your device
```

There is no requirement to upload images to a third-party compression service.

---

# ⚠️ AVIF Support

AVIF support depends on the Pillow build and available codec support on the platform.

Try:

```bash
python image_tool.py --format avif --quality 70
```

If AVIF encoding is unavailable, GiniMG will report the underlying encoding error.

JPEG, PNG, and WebP generally provide broader codec compatibility.

---

# 🧰 Recommended Environment

Use a virtual environment:

```bash
python -m venv .venv
```

Activate:

### Linux / macOS / Termux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Then:

```bash
python -m pip install -r requirements.txt
```

This keeps GiniMG's Python dependencies isolated from the system Python installation.

---

# 🔑 Quick Start

## Termux / Linux / macOS

```bash
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python image_tool.py
```

## Windows PowerShell

```powershell
git clone https://github.com/Ginimg/Ginimg.git
cd Ginimg
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python image_tool.py
```

---

# 📜 License

MIT License.

See [`LICENSE`](LICENSE).

---

# GiniMG

**Local. Private. Simple.**

Compress, convert, resize, and batch-process your images without sending them to an online service.

## Version

`1.0.0`
