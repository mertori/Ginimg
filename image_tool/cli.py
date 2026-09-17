from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from .config import DEFAULT_INPUT, DEFAULT_OUTPUT
from .discovery import common_root, discover_inputs
from .engine import process_image
from .naming import build_output_name, unique_path


def parse_size(value):
    text = value.strip().upper().replace(" ", "")
    units = [("GB", 1024**3), ("MB", 1024**2), ("KB", 1024), ("B", 1)]
    for unit, multiplier in units:
        if text.endswith(unit):
            number = text[:-len(unit)].strip()
            try:
                amount = float(number)
            except ValueError:
                raise argparse.ArgumentTypeError("Invalid target size.")
            if amount <= 0:
                raise argparse.ArgumentTypeError("Target size must be positive.")
            return int(amount * multiplier)
    raise argparse.ArgumentTypeError("Use B, KB, MB, or GB (e.g. 200KB).")


def human_size(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.2f} {unit}"
        n /= 1024


def ask(prompt, default=None):
    suffix = f" [{default}]" if default is not None else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value if value else (str(default) if default is not None else "")


def ask_yes_no(prompt, default=True):
    suffix = "[Y/n]" if default else "[y/N]"
    value = input(f"{prompt} {suffix}: ").strip().lower()
    if not value:
        return default
    return value in {"y", "yes"}


def choose(title, options, default=1):
    print(f"\n{title}")
    print("─" * 48)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        value = input(f"\nChoice [{default}]: ").strip()
        if not value:
            return default
        if value.isdigit() and 1 <= int(value) <= len(options):
            return int(value)
        print("Please enter a valid choice.")


def interactive():
    print("""
╔════════════════════════════════════════════════════╗
║              IMAGE TOOLKIT v1.0.0                 ║
║       Local • Private • Compression Tool          ║
╚════════════════════════════════════════════════════╝
""")

    action = choose("What would you like to do?", [
        "Compress images",
        "Convert image format",
        "Compress to target size",
        "Batch compress",
        "Batch convert",
        "Resize images",
        "Advanced options",
        "Exit",
    ], 1)

    if action == 8:
        return 0

    batch = action in {4, 5}
    target_mode = action == 3
    conversion = action in {2, 5}
    resize_only = action == 6

    source_choice = choose("Input source", [
        "Enter file path",
        "Enter directory path",
        "Use default input directory",
    ], 3 if batch else 1)

    if source_choice == 1:
        source = ask("Enter file path")
        inputs = [source]
        recursive = False
    elif source_choice == 2:
        source = ask("Enter directory path")
        inputs = [source]
        recursive = ask_yes_no("Process subdirectories?", False)
    else:
        inputs = [str(DEFAULT_INPUT)]
        recursive = ask_yes_no("Process subdirectories?", False)

    if conversion or not resize_only:
        fmt_choice = choose("Output format", [
            "Original",
            "JPEG",
            "PNG",
            "WebP",
            "AVIF",
        ], 3)
        formats = ["original", "jpeg", "png", "webp", "avif"]
        output_format = formats[fmt_choice - 1]
    else:
        output_format = "original"

    quality = 80
    target_size = None

    if target_mode:
        target_choice = choose("Target file size", [
            "100 KB",
            "200 KB",
            "500 KB",
            "1 MB",
            "Custom size",
        ], 2)
        presets = [100 * 1024, 200 * 1024, 500 * 1024, 1024 * 1024]
        if target_choice <= 4:
            target_size = presets[target_choice - 1]
        else:
            while True:
                raw = ask("Enter target size (e.g. 200KB, 1MB)")
                try:
                    target_size = parse_size(raw)
                    break
                except argparse.ArgumentTypeError as exc:
                    print(f"Invalid size: {exc}")
        print(f"Target size: {human_size(target_size)}")
    elif not resize_only:
        while True:
            raw = ask("Quality (1-100)", 80)
            try:
                quality = int(raw)
                if 1 <= quality <= 100:
                    break
            except ValueError:
                pass
            print("Quality must be an integer from 1 to 100.")

    max_width = None
    max_height = None
    if resize_only or action == 7:
        while True:
            raw = ask("Maximum width in pixels (0 = no limit)", 0)
            try:
                max_width = int(raw)
                if max_width >= 0:
                    max_width = max_width or None
                    break
            except ValueError:
                pass
            print("Enter a non-negative integer.")
        while True:
            raw = ask("Maximum height in pixels (0 = no limit)", 0)
            try:
                max_height = int(raw)
                if max_height >= 0:
                    max_height = max_height or None
                    break
            except ValueError:
                pass
            print("Enter a non-negative integer.")

    remove_exif = ask_yes_no("Remove EXIF/metadata?", True)
    filename_mode = "compressed"
    if not resize_only:
        filename_choice = choose("Output filename", [
            "filename_compressed",
            "Keep original filename",
        ], 1)
        filename_mode = "compressed" if filename_choice == 1 else "original"

    output = ask("Output directory", DEFAULT_OUTPUT)
    overwrite = ask_yes_no("Overwrite existing output files?", False)
    allow_larger = ask_yes_no("Keep output if it is larger than the source?", False)
    dry_run = ask_yes_no("Dry run only (do not write files)?", False)

    print("\n────────────────────────────────────────────────")
    print("Configuration")
    print("────────────────────────────────────────────────")
    print(f"Input       : {', '.join(inputs)}")
    print(f"Output      : {output}")
    print(f"Format      : {output_format}")
    print(f"Mode        : {'Target size' if target_mode else 'Quality/resize'}")
    if target_size:
        print(f"Target      : {human_size(target_size)}")
    else:
        print(f"Quality     : {quality}")
    print(f"EXIF        : {'Remove' if remove_exif else 'Keep'}")
    print(f"Recursive   : {'Yes' if recursive else 'No'}")
    print(f"Overwrite   : {'Yes' if overwrite else 'No'}")
    print("────────────────────────────────────────────────")

    if not ask_yes_no("Start processing?", True):
        print("Cancelled.")
        return 0

    return run_processing(
        inputs, output, output_format, quality, target_size,
        max_width, max_height, remove_exif, filename_mode,
        recursive, overwrite, allow_larger, dry_run, "_compressed"
    )


def run_processing(inputs, output, output_format, quality, target_size,
                   max_width, max_height, remove_exif, filename_mode,
                   recursive, overwrite, allow_larger, dry_run, suffix):
    files = discover_inputs(inputs, recursive)

    if not files:
        print("\nNo supported image files found.")
        print("Supported: JPG, JPEG, PNG, WebP, AVIF, BMP, GIF, TIFF.")
        return 1

    output_root = Path(output).expanduser()
    root = common_root(files)
    results = []
    failures = 0

    print(f"\nFound {len(files)} image(s).\n")

    for source in files:
        try:
            try:
                relative_parent = source.resolve().parent.relative_to(root)
            except ValueError:
                relative_parent = Path()

            destination_dir = output_root / relative_parent
            name = build_output_name(source, output_format, filename_mode, suffix)
            destination = destination_dir / name

            if destination.exists() and not overwrite:
                destination = unique_path(destination)

            original_size = source.stat().st_size

            if dry_run:
                print(f"[DRY RUN] {source} -> {destination}")
                results.append(("dry", source, original_size, None))
                continue

            info = process_image(
                source, destination,
                output_format=output_format,
                quality=quality,
                target_bytes=target_size,
                max_width=max_width,
                max_height=max_height,
                remove_exif_flag=remove_exif,
            )
            output_size = info["size"]

            if output_size > original_size and not allow_larger:
                destination.unlink(missing_ok=True)
                print(
                    f"[SKIP LARGER] {source.name}: "
                    f"{human_size(output_size)} > {human_size(original_size)}"
                )
                results.append(("larger", source, original_size, output_size))
                continue

            saved = original_size - output_size
            percent = (saved / original_size * 100) if original_size else 0
            note = ""
            if target_size is not None:
                note = " | target=" + ("OK" if info["target_reached"] else "NOT REACHED")
                if info["quality"] is not None:
                    note += f" | q={info['quality']}"
                note += f" | {info['width']}x{info['height']}"

            print(
                f"[OK] {source.name} -> {destination.name} | "
                f"{human_size(original_size)} -> {human_size(output_size)} | "
                f"{percent:.2f}% saved{note}"
            )
            results.append(("ok", source, original_size, output_size))
        except Exception as exc:
            failures += 1
            print(f"[ERROR] {source}: {exc}")

    processed = sum(1 for r in results if r[0] == "ok")
    total_in = sum(r[2] for r in results if r[0] in {"ok", "larger"})
    total_out = sum(r[3] or 0 for r in results if r[0] == "ok")

    print("\n════════════════════════════════════════════════")
    print("Summary")
    print("════════════════════════════════════════════════")
    print(f"Files found : {len(files)}")
    print(f"Processed   : {processed}")
    print(f"Failed      : {failures}")
    if total_in:
        saved = total_in - total_out
        print(f"Input size  : {human_size(total_in)}")
        print(f"Output size : {human_size(total_out)}")
        print(f"Saved       : {human_size(max(saved, 0))}")
        print(f"Reduction   : {max(saved, 0) / total_in * 100:.2f}%")

    return 1 if failures else 0


def build_parser():
    p = argparse.ArgumentParser(
        description="Privacy-first local image compressor and converter."
    )
    p.add_argument("inputs", nargs="*", help="Files and/or directories.")
    p.add_argument("-o", "--output", default=str(DEFAULT_OUTPUT))
    p.add_argument("-f", "--format",
                   choices=["original", "jpeg", "png", "webp", "avif"],
                   default="original")
    p.add_argument("-q", "--quality", type=int, default=None)
    p.add_argument("--target-size", type=parse_size)
    p.add_argument("--max-width", type=int)
    p.add_argument("--max-height", type=int)
    p.add_argument("--remove-exif", dest="remove_exif",
                   action="store_true", default=True)
    p.add_argument("--keep-exif", dest="remove_exif", action="store_false")
    p.add_argument("--filename", choices=["compressed", "original"],
                   default="compressed")
    p.add_argument("--suffix", default="_compressed")
    p.add_argument("--recursive", action="store_true")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--allow-larger", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--version", action="version", version=__version__)
    return p


def main(argv=None):
    # No arguments = interactive terminal UI.
    if argv is None:
        import sys
        if len(sys.argv) == 1:
            return interactive()

    args = build_parser().parse_args(argv)

    if args.quality is not None and args.target_size is not None:
        print("Error: --quality and --target-size are mutually exclusive.")
        return 2

    quality = args.quality if args.quality is not None else 80
    if not 1 <= quality <= 100:
        print("Error: quality must be between 1 and 100.")
        return 2

    if args.max_width is not None and args.max_width <= 0:
        print("Error: --max-width must be positive.")
        return 2
    if args.max_height is not None and args.max_height <= 0:
        print("Error: --max-height must be positive.")
        return 2

    inputs = args.inputs or [str(DEFAULT_INPUT)]
    return run_processing(
        inputs, args.output, args.format, quality, args.target_size,
        args.max_width, args.max_height, args.remove_exif,
        args.filename, args.recursive, args.overwrite, args.allow_larger,
        args.dry_run, args.suffix
    )
