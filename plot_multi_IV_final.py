#!/usr/bin/env python3
'''
Plot IV curves of ITk barrel modules after module thermocycling.

Usage:
    python plot_multi_IV_final.py -i 'BNL/ML/*/*.json'
'''

import matplotlib as mplt
mplt.use('Agg')

from glob import glob
import numpy as np
import os
import json
import collections
import argparse
import datetime
import matplotlib.pyplot as plt
from pprint import pprint

mplt.rc("text", usetex=True)
mplt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})


HIGH_CURRENT_THRESHOLD_NA = 300.0

category_A_high_current = []
category_D_incomplete = []
category_E_script_data = []

modules_checked = set()
modules_not_working = set()


def clean_sn(serial):
    serial = str(serial)
    return serial[2:] if serial.startswith("SN") else serial


def with_sn(serial):
    serial = str(serial)
    return serial if serial.startswith("SN") else f"SN{serial}"


def main():
    parser = argparse.ArgumentParser(description='Plot IV curves after thermal cycling')
    parser.add_argument('-i', '--input', help='Path to IV JSON files', default="")
    parser.add_argument('--do_amac_offset', dest='do_amac_offset', action='store_true')
    parser.add_argument('--do_logY', dest='do_logY', action='store_true')
    args = parser.parse_args()

    if not args.input:
        print("Please provide input path with -i")
        raise SystemExit(1)

    l_input_files = glob(args.input)
    do_amac_offset = args.do_amac_offset
    do_logY = args.do_logY

    if not l_input_files:
        msg = f"No JSON files found for input pattern: {args.input}"
        print(msg)
        add_category_E("UNKNOWN", msg)
        write_error_summary()
        raise SystemExit(1)

    l_module_names = get_module_names(l_input_files)

    print('\nJSON output data files to consider:')
    pprint(l_input_files)

    print('\nModule names parsed to make plots:')
    pprint(l_module_names)

    if not l_module_names:
        msg = "No valid module names could be parsed from the JSON files."
        print(msg)
        add_category_E("UNKNOWN", msg)
        write_error_summary()
        raise SystemExit(1)

    for module_name in l_module_names:
        modules_checked.add(clean_sn(module_name))
        mk_single_plot(module_name, l_input_files, do_amac_offset, do_logY)

    write_error_summary()


def mk_single_plot(in_name, l_input_files, do_amac_offset, do_logY):
    module_clean = clean_sn(in_name)
    module_display = with_sn(module_clean)

    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)
    print(f'Making plot for {module_display}')

    l_input_files_amac = []
    skipped_msgs = []

    for f in l_input_files:
        try:
            with open(f, 'r') as jf:
                data = json.load(jf)

            file_component = data.get("component", data.get("serial_number"))

            if clean_sn(file_component) == module_clean:
                l_input_files_amac.append(f)

        except Exception as e:
            basename = os.path.basename(f)
            msg = f"{basename} — failed to parse JSON: {str(e)}"
            skipped_msgs.append(msg)
            add_category_E(module_clean, msg)
            print(f"\033[91m⚠ SKIPPED: {msg}\033[0m")

    d_unsorted = {}

    for input_file in l_input_files_amac:
        try:
            input_dict = json_to_dict(input_file)
            timestamp = input_dict.get('timestamp', input_dict.get('date', '1970-01-01T00:00:00Z'))
            sort_key = f"{timestamp}_{os.path.basename(input_file)}"
            d_unsorted[sort_key] = input_file

        except Exception as e:
            basename = os.path.basename(input_file)
            msg = f"{basename} — failed to load for sorting: {str(e)}"
            skipped_msgs.append(msg)
            add_category_E(module_clean, msg)
            print(f"\033[91m⚠ SKIPPED: {msg}\033[0m")

    od = collections.OrderedDict(sorted(d_unsorted.items()))
    l_input_files_sorted = list(od.values())

    print('AMAC sorted dictionary values:')
    pprint(l_input_files_sorted)

    blues = mplt.cm.Blues(np.linspace(0.4, 0.9, max(len(l_input_files_sorted), 1)))
    oranges = mplt.cm.Oranges(np.linspace(0.4, 0.9, max(len(l_input_files_sorted), 1)))

    handles = []
    labels = []
    first_valid_timestamp = None
    valid_plot_count = 0

    for count, input_file in enumerate(l_input_files_sorted):
        if '.json' not in input_file:
            continue

        try:
            voltages, currents, timestamp, ntcpb_temp, ntcx_temp = read_AMAC_IV(
                input_file,
                module_clean,
                do_amac_offset
            )

            if first_valid_timestamp is None and timestamp != "Invalid Time":
                first_valid_timestamp = timestamp

            if len(voltages) == 0 or len(currents) == 0:
                basename = os.path.basename(input_file)
                msg = f"{basename} — empty"
                skipped_msgs.append(msg)
                add_category_D(module_clean, msg)
                print(f"\033[91m⚠ SKIPPED: {msg}\033[0m")
                continue

            valid_plot_count += 1

            print(f"Plotting {len(voltages)} points for file: {input_file}")

            lcolour = blues[count] if ntcpb_temp < 0 else oranges[count]
            ntcx_txt = '{0:.3g}'.format(ntcx_temp).replace('-', '$-$')

            line = ax.plot(
                voltages,
                currents,
                lw=2,
                ls='-',
                c=lcolour,
                label='{0}, {1}C'.format(timestamp, ntcx_txt)
            )

            handles.append(line[0])
            labels.append('{0}, {1}C'.format(timestamp, ntcx_txt))

        except Exception as e:
            basename = os.path.basename(input_file)
            err_text = str(e).strip()

            if "empty or missing IV data" in err_text:
                msg = f"{basename} — empty"
                add_category_D(module_clean, msg)
            else:
                msg = f"{basename} — {err_text}"
                add_category_E(module_clean, msg)

            skipped_msgs.append(msg)
            print(f"\033[91m⚠ SKIPPED: {msg}\033[0m")

    if valid_plot_count == 0:
        add_category_D(module_clean, "No valid IV curves were plotted for this module.")

    for msg in skipped_msgs:
        dummy_handle = plt.Line2D(
            [],
            [],
            color='red',
            marker='x',
            linestyle='None',
            markersize=8,
            markeredgewidth=1.5
        )
        handles.append(dummy_handle)
        labels.append(msg)

    if handles:
        legend = ax.legend(
            handles,
            labels,
            loc='upper left',
            prop={'size': 14},
            frameon=False,
            handlelength=1.8,
            handletextpad=0.5,
            borderpad=0.6,
            ncol=3,
            columnspacing=0.6
        )

        for text, label in zip(legend.get_texts(), labels):
            if label in skipped_msgs:
                text.set_color('red')

    text_size = 28

    if do_logY:
        ax.set_yscale('log')
        ax.set_ylim(1, 10000)
    else:
        ax.set_ylim(-20, 550)

    ax.set_xlim(-10, 750)

    plt.xlabel(r'Voltage [V]', labelpad=15, size=38)
    plt.ylabel(r'Current [nA]', labelpad=15, size=38)

    ax.tick_params('x', length=12, width=1, which='major', labelsize=28, pad=10, direction="in")
    ax.tick_params('x', length=6, width=1, which='minor', direction="in")
    ax.tick_params('y', length=12, width=1, which='major', labelsize=28, pad=10, direction="in", right=True)
    ax.tick_params('y', length=6, width=1, which='minor', direction="in", right=True)

    fig.text(0.20, 0.56, module_display, color='k', size=text_size)

    if first_valid_timestamp:
        fig.text(0.20, 0.51, f"Timestamp: {first_valid_timestamp}", color='k', size=text_size * 0.6)
    else:
        fig.text(0.20, 0.51, "Timestamp: Unknown", color='gray', size=text_size * 0.6)

    fig.text(0.20, 0.47, 'Temperatures = AMAC NTCx', color='gray', size=text_size * 0.5)

    plt.tight_layout(pad=0.3)
    plt.subplots_adjust(top=0.97, left=0.16, right=0.99)

    plot_dir = os.path.join("BNL", "ML", module_display, "IV")
    mkdir(plot_dir)

    save_name = os.path.join(plot_dir, module_display)

    print(f"Saving plot as {save_name}.pdf")
    plt.savefig(f"{save_name}.pdf", format='pdf')
    plt.savefig(f"{save_name}.png", format='png', dpi=300)
    plt.close(fig)


def read_AMAC_IV(file_name, module_clean, do_AMAC_offset=True):
    print(f'Opening file: {file_name}')

    with open(file_name, 'r') as infile:
        input_dict = json.load(infile)

    results = input_dict.get('results', {})
    current_raw = results.get('CURRENT') or results.get('current')
    voltage_raw = results.get('VOLTAGE') or results.get('voltage')

    if current_raw is None or voltage_raw is None:
        raise ValueError("empty or missing IV data")

    if len(current_raw) == 0 or len(voltage_raw) == 0:
        raise ValueError("empty or missing IV data")

    current_zero_offset = float(current_raw[0]) if do_AMAC_offset else 0.0
    print(f'Using AMAC current zero offset: {current_zero_offset}')

    voltages = [abs(float(x)) for x in voltage_raw]
    currents = [float(x) - current_zero_offset for x in current_raw]

    max_current = max(currents)

    if max_current > HIGH_CURRENT_THRESHOLD_NA:
        basename = os.path.basename(file_name)

        warning_msg = (
            f"{basename} — HIGH CURRENT WARNING: "
            f"maximum current = {max_current:.2f} nA "
            f"(> {HIGH_CURRENT_THRESHOLD_NA:.0f} nA)"
        )

        print(f"\033[91m⚠ {warning_msg}\033[0m")
        add_category_A(module_clean, warning_msg)

    if "temperatures" in input_dict:
        ntcpb_temp = input_dict["temperatures"].get("AMAC_NTCpb", [0.0])[0]
        ntcx_temp = input_dict["temperatures"].get("AMAC_NTCx", [0.0])[0]

    elif "properties" in input_dict and "DCS" in input_dict["properties"]:
        ntcpb_temp = input_dict["properties"]["DCS"].get("AMAC_NTCpb", 0.0)
        ntcx_temp = input_dict["properties"]["DCS"].get("AMAC_NTCx", 0.0)

    else:
        ntcpb_temp = 0.0
        ntcx_temp = 0.0

    timestamp = input_dict.get('timestamp', input_dict.get('date', '1970-01-01T00:00:00Z'))
    timestamp_stripped = timestamp.replace('T', ' ').split('.')[0]

    try:
        pydate_datetime_stamp = datetime.datetime.strptime(
            timestamp_stripped,
            '%Y-%m-%d %H:%M:%S'
        )
        out_datetime = pydate_datetime_stamp.strftime('%Y-%m-%d %H:%M')

    except ValueError:
        out_datetime = "Invalid Time"

    return voltages, currents, out_datetime, ntcpb_temp, ntcx_temp


def add_category_A(module_clean, message):
    modules_not_working.add(clean_sn(module_clean))
    category_A_high_current.append({
        "module": with_sn(module_clean),
        "message": message
    })


def add_category_D(module_clean, message):
    modules_not_working.add(clean_sn(module_clean))
    category_D_incomplete.append({
        "module": with_sn(module_clean),
        "message": message
    })


def add_category_E(module_clean, message):
    if module_clean != "UNKNOWN":
        modules_not_working.add(clean_sn(module_clean))

    category_E_script_data.append({
        "module": with_sn(module_clean) if module_clean != "UNKNOWN" else "UNKNOWN",
        "message": message
    })


def json_to_dict(file_name):
    with open(file_name, 'r') as infile:
        return json.load(infile)


def get_module_names(l_filtered_input_files):
    l_module_names = []

    for input_file in l_filtered_input_files:
        if '.json' not in input_file:
            continue

        try:
            input_dict = json_to_dict(input_file)
            module_name = input_dict.get('component', input_dict.get('serial_number', 'UNKNOWN'))

            if module_name != 'UNKNOWN':
                module_clean = clean_sn(module_name)

                if module_clean not in l_module_names:
                    l_module_names.append(module_clean)

        except Exception as e:
            basename = os.path.basename(input_file)
            msg = f"MODULE NAME PARSE ERROR: {basename} — {str(e)}"
            add_category_E("UNKNOWN", msg)
            print(f"\033[91m⚠ SKIPPED while parsing module name: {basename} — {str(e)}\033[0m")

    l_module_names.sort()
    return l_module_names


def write_error_summary(output_file="BNL/ML/iv_error_summary.txt"):
    mkdir(os.path.dirname(output_file))

    total_modules_checked = len(modules_checked)
    not_working_count = len(modules_not_working)
    working_count = total_modules_checked - not_working_count

    total_entries = (
        len(category_A_high_current)
        + len(category_D_incomplete)
        + len(category_E_script_data)
    )

    with open(output_file, "w") as f:
        f.write("IV Plot Error Summary\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"High current threshold: {HIGH_CURRENT_THRESHOLD_NA:.0f} nA\n\n")

        f.write("FINAL SUMMARY\n")
        f.write("-" * 80 + "\n")
        f.write(f"TOTAL MODULES CHECKED: {total_modules_checked}\n")
        f.write(f"WORKING MODULES: {working_count}\n")
        f.write(f"NOT WORKING MODULES: {not_working_count}\n")
        f.write(f"TOTAL FLAGGED FILES / WARNINGS: {total_entries}\n\n")

        f.write("CATEGORY COUNTS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Category A — IV current values above threshold: {len(category_A_high_current)}\n")
        f.write(f"Category D — Incomplete dataset or missing generated files: {len(category_D_incomplete)}\n")
        f.write(f"Category E — Script did not run or data are unavailable: {len(category_E_script_data)}\n\n")

        write_category_section(
            f,
            "Category A",
            "IV current values above threshold.",
            category_A_high_current
        )

        write_category_section(
            f,
            "Category D",
            "Incomplete dataset or missing generated files.",
            category_D_incomplete
        )

        write_category_section(
            f,
            "Category E",
            "Script did not run or data are unavailable.",
            category_E_script_data
        )

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    print(f"TOTAL MODULES CHECKED: {total_modules_checked}")
    print(f"WORKING MODULES: {working_count}")
    print(f"NOT WORKING MODULES: {not_working_count}")
    print(f"Category A high current: {len(category_A_high_current)}")
    print(f"Category D incomplete/empty: {len(category_D_incomplete)}")
    print(f"Category E script/data unavailable: {len(category_E_script_data)}")
    print(f"\nSaved organized error summary to: {output_file}")


def write_category_section(f, category_name, description, records):
    f.write("\n")
    f.write("=" * 80 + "\n")
    f.write(f"{category_name}\n")
    f.write(description + "\n")
    f.write("=" * 80 + "\n")

    if not records:
        f.write("None found.\n")
        return

    grouped = collections.defaultdict(list)

    for record in records:
        grouped[record["module"]].append(record["message"])

    for module in sorted(grouped.keys()):
        f.write(f"\n{module}\n")
        f.write("-" * len(module) + "\n")

        for i, message in enumerate(grouped[module], start=1):
            f.write(f"{i}. {message}\n")


def mkdir(dirPath):
    if not dirPath:
        return

    try:
        os.makedirs(dirPath, exist_ok=True)
        print('Successfully made directory:', dirPath)
    except OSError:
        pass


if __name__ == "__main__":
    main()