#!/usr/bin/env python3

import subprocess

import re

serial_numbers = [
    # --- GPC modules ---
    "GPC2413-0017-B6-X",
    "GPC2414-0018-C2-X",
    "GPC2225-0020-A1-X",
    "GPC2225-0020-A3-X",
    "GPC2225-0020-A2-X",
    "GPC2324-0006-A2-X",
    "GPC2233-0017-A5-X",
    "GPC2238-0020-B1-X",
    "GPC2230-0006-C6-X",
    "GPC2225-0009-C2-X",
    "GPC2225-0003-B0-X",
    "GPC2324-0006-A0-X",
    "GPC2324-0006-A1-X",
    "GPC2225-0003-B2-X",
    "GPC2225-0003-B3-X",
    "GPC2225-0003-B6-X",
    "GPC2324-0006-A6-X",
    "GPC2238-0020-B4-X",
    "GPC2238-0020-B5-X",
    "GPC2230-0006-C2-X",
    "GPC2230-0006-C5-X",
    "GPC2233-0017-A3-X",
    "GPC2233-0017-A4-X",
    "GPC2225-0008-A0-X",
    "GPC2225-0008-A1-X",

    # --- 20USBHX modules ---
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
    "20USBHX2002681",
    "20USBHX2002682",
    "20USBHX2002690",
    "20USBHX2002694",
    "20USBHX2002695",
    "20USBHX2002783",
    "20USBHX2002697",
    "20USBHX2002698",
    "20USBHX2002784",
    "20USBHX2002785",
    "20USBHX2002786",
    "20USBHX2002940",
    "20USBHX2002942",
    "20USBHX2002943",
    "20USBHX2002938",
    "20USBHX2002939",
    "20USBHX2002944",

]

NOISE_THRESHOLD = 600

failed_serials = []

category_C_errors = []

skip_pattern = re.compile(

    r"Skipping\s+(?P<file>\S+)\s+—\s+mean\s+=\s+(?P<mean>\d+\.?\d*)"

)

for i, serial in enumerate(serial_numbers, start=1):

    print(f"[{i}/{len(serial_numbers)}] Running for {serial}")

    cmd = [

        "python",

        "plot_multi_inputnoise.py",

        "--serial_number",

        serial,

    ]

    try:

        result = subprocess.run(

            cmd,

            capture_output=True,

            text=True,

            check=True

        )

        output = result.stdout + result.stderr

        print(output)

        for match in skip_pattern.finditer(output):

            filename = match.group("file")

            mean_value = float(match.group("mean"))

            if mean_value < NOISE_THRESHOLD:

                category_C_errors.append({

                    "serial": serial,

                    "file": filename,

                    "mean": mean_value,

                })

                print(

                    f"🚩 CATEGORY C ERROR: {serial} | "

                    f"{filename} | mean = {mean_value}"

                )

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

print(f"\n🚩 Category C input noise errors mean < {NOISE_THRESHOLD}: {len(category_C_errors)}")

if category_C_errors:

    for err in category_C_errors:

        print(f"{err['serial']} | {err['file']} | mean = {err['mean']}")

else:

    print("None")

print("\nDone.")