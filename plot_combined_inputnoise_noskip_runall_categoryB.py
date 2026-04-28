#!/usr/bin/env python3

import subprocess
import re
import json

HIGH_THRESHOLD = 1000

failed_serials = []
category_B_errors = []

serial_numbers = [
    # --- paste your full serial list here ---
    "20USBHX2002657",
    "20USBHX2002683",
    "20USBHX2002629",
    "20USBHX2002630",
    "20USBHX2002603",
    "20USBHX2002631",
    "20USBHX2002652",
    "20USBHX2002653",
    "20USBHX2003562",
    "20USBHX2002654",
    "20USBHX2002656",
    "20USBHX2002684",
    "20USBHX2003551",
    "20USBHX2002685",
    "20USBHX2002686",
    "20USBHX2002687",
    "20USBHX2002688",
    "20USBHX2002709",
    "20USBHX2002710",
    "20USBHX2002711",
    "20USBHX2002712",
    "20USBHX2002713",
    "20USBHX2002677",
    "20USBHX2002678",
    "20USBHX2002679",
    "20USBHX2002680",
    "20USBHX2002655",
    "20USBHX2002691",
    "20USBHX2002692",
    "20USBHX2002693",
    "20USBHX2002689",
]

high_pattern = re.compile(
    r"HIGH INPUT NOISE.*?\n"
    r"\s+count = (?P<count>\d+).*?\n"
    r"\s+min = (?P<min>\d+\.?\d*), max = (?P<max>\d+\.?\d*).*?\n"
    r"\s+channels = (?P<channels>\[.*?\]).*?\n"
    r"\s+values\s+= (?P<values>\[.*?\])",
    re.DOTALL,
)


def fmt_values(values):
    return [round(float(v), 1) for v in values]


def parse_output_for_errors(output, serial):
    blocks = output.split("🚨 FILE:")

    for block in blocks[1:]:
        lines = block.strip().split("\n")

        if not lines:
            continue

        filename = lines[0].strip()
        high_match = high_pattern.search(block)

        if high_match:
            high_count = int(high_match.group("count"))
            high_channels = json.loads(high_match.group("channels"))
            high_values = json.loads(high_match.group("values"))

            category_B_errors.append({
                "serial": serial,
                "file": filename,
                "count": high_count,
                "channels": high_channels,
                "high_values": high_values,
            })

            print(f"\n🚩 CATEGORY B: {serial} | {filename}")
            print(f"   high_values = {fmt_values(high_values)}")
            print(f"   high_channels = {high_channels}")


def main():
    for i, serial in enumerate(serial_numbers, start=1):
        print(f"\n[{i}/{len(serial_numbers)}] Running for {serial}")

        cmd = [
            "python",
            "plot_combined_inputnoise_noskip_categoryC.py",
            "--serial_number",
            serial,
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
            )

            output = result.stdout + result.stderr
            print(output)

            parse_output_for_errors(output, serial)

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed for {serial} return code {e.returncode}")
            print(e.stdout)
            print(e.stderr)
            failed_serials.append(serial)

    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    print(f"\nTotal serials checked: {len(serial_numbers)}")

    print(f"\n❌ Failed serials: {len(failed_serials)}")
    if failed_serials:
        for serial in failed_serials:
            print(serial)
    else:
        print("None")

    print(f"\n🚩 Category B input noise errors > {HIGH_THRESHOLD}:")
    if category_B_errors:
        for err in category_B_errors:
            print(
                f"{err['serial']} | {err['file']} | "
                f"high_values = {fmt_values(err['high_values'])}"
            )
    else:
        print("None")

    bad_modules = sorted(set(err["serial"] for err in category_B_errors))

    print(f"\n🚩 Modules with input noise > {HIGH_THRESHOLD}:")
    if bad_modules:
        for serial in bad_modules:
            print(serial)
    else:
        print("None")

    print("\nDone.")


if __name__ == "__main__":
    main()