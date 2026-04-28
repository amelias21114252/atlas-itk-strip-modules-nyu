#!/usr/bin/env python3
"""
Run plot_multi_IV.py for all SN20USBML* folders.

Usage:
    python run_all_plot_multi_IV.py
    includes timestamp
"""

import os
import glob
import argparse
import subprocess
import sys


def find_serial_folders(base_dir="."):
    """
    Find folders like:
        SN20USBML1235761
        SN20USBML1235852
    """
    pattern = os.path.join(base_dir, "SN20USBML*")
    serial_dirs = [os.path.basename(p) for p in glob.glob(pattern) if os.path.isdir(p)]
    return sorted(serial_dirs)


def main():
    parser = argparse.ArgumentParser(
        description="Run plot_multi_IV.py for SN20USBML* folders"
    )
    parser.add_argument("--base_dir", default=".", help="Directory with SN folders")
    parser.add_argument("--script", default="plot_multi_IV.py")
    parser.add_argument("--do_amac_offset", action="store_true")
    parser.add_argument("--do_logY", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"❌ Script not found: {args.script}")
        sys.exit(1)

    serial_folders = find_serial_folders(args.base_dir)

    if not serial_folders:
        print("❌ No SN20USBML* folders found")
        sys.exit(1)

    print("\nFound serial folders:")
    for s in serial_folders:
        print(f"  {s}")
    print()

    for serial in serial_folders:
        input_pattern = os.path.join(args.base_dir, serial, "*.json")

        if not glob.glob(input_pattern):
            print(f"⚠️ Skipping {serial} (no JSON files)")
            continue

        cmd = ["python", args.script, "-i", input_pattern]

        if args.do_amac_offset:
            cmd.append("--do_amac_offset")
        if args.do_logY:
            cmd.append("--do_logY")

        print("=" * 80)
        print("Running:", " ".join(cmd))
        print("=" * 80)

        subprocess.run(cmd)

    print("\n✅ All modules processed.")


if __name__ == "__main__":
    main()