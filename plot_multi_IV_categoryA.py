#!/usr/bin/env python3
"""
Run plot_multi_IV.py for all SN20USBML* folders.

Usage:
    python run_all_plot_multi_IV.py
    python run_all_plot_multi_IV.py --do_logY
"""

import os
import glob
import argparse
import subprocess
import sys
import json


CURRENT_LIMIT = 600


def find_serial_folders(base_dir="."):
    pattern = os.path.join(base_dir, "SN20USBML*")
    serial_dirs = [
        os.path.basename(p)
        for p in glob.glob(pattern)
        if os.path.isdir(p)
    ]
    return sorted(serial_dirs)


def find_current_values(data, path=""):
    """
    Recursively search JSON for values whose key contains 'current'.
    Returns list of tuples:
        (json_path, current_value)
    """
    found = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key

            if "current" in key.lower():
                if isinstance(value, (int, float)):
                    found.append((new_path, value))

                elif isinstance(value, list):
                    for i, item in enumerate(value):
                        if isinstance(item, (int, float)):
                            found.append((f"{new_path}[{i}]", item))

            found.extend(find_current_values(value, new_path))

    elif isinstance(data, list):
        for i, item in enumerate(data):
            found.extend(find_current_values(item, f"{path}[{i}]"))

    return found


def check_category_a_errors(serial, json_files):
    """
    Check if any current value is above CURRENT_LIMIT.
    """
    errors = []

    for json_file in json_files:
        try:
            with open(json_file, "r") as f:
                data = json.load(f)

            current_values = find_current_values(data)

            for json_path, current in current_values:
                if current > CURRENT_LIMIT:
                    errors.append({
                        "serial": serial,
                        "file": json_file,
                        "path": json_path,
                        "current": current
                    })

        except Exception as e:
            print(f"⚠️ Could not read {json_file}: {e}")

    return errors


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

    all_category_a_errors = []

    for serial in serial_folders:
        input_pattern = os.path.join(args.base_dir, serial, "*.json")
        json_files = sorted(glob.glob(input_pattern))

        if not json_files:
            print(f"⚠️ Skipping {serial} (no JSON files)")
            continue

        category_a_errors = check_category_a_errors(serial, json_files)

        if category_a_errors:
            print("\n" + "!" * 80)
            print(f"🚨 CATEGORY A ERROR FOUND FOR {serial}")
            print(f"Reason: Current above {CURRENT_LIMIT}")
            print("!" * 80)

            for err in category_a_errors:
                print(f"Serial:  {err['serial']}")
                print(f"File:    {err['file']}")
                print(f"Path:    {err['path']}")
                print(f"Current: {err['current']}")
                print("-" * 80)

            all_category_a_errors.extend(category_a_errors)

        cmd = ["python", args.script, "-i", input_pattern]

        if args.do_amac_offset:
            cmd.append("--do_amac_offset")
        if args.do_logY:
            cmd.append("--do_logY")

        print("=" * 80)
        print("Running:", " ".join(cmd))
        print("=" * 80)

        subprocess.run(cmd)

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    if all_category_a_errors:
        print(f"🚨 Total Category A errors: {len(all_category_a_errors)}")

        error_serials = sorted(set(err["serial"] for err in all_category_a_errors))
        print("\nModules with Category A errors:")
        for serial in error_serials:
            count = sum(err["serial"] == serial for err in all_category_a_errors)
            print(f"  {serial}: {count} current value(s) above {CURRENT_LIMIT}")

    else:
        print(f"✅ No Category A errors found. No current values above {CURRENT_LIMIT}.")

    print("\n✅ All modules processed.")


if __name__ == "__main__":
    main()