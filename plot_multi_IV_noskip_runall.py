#!/usr/bin/env python3

#python plot_multi_IV_noskip_runall.py -i "parent/*"

#python plot_multi_IV_noskip_runall.py -i "parent/SN*/*.json"
#python plot_multi_IV_noskip_runall.py -i "SN*/*.json"


import matplotlib as mplt
mplt.use('Agg')

from glob import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
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


def main():
    parser = argparse.ArgumentParser(description='Plot IV curves after thermal cycling')
    parser.add_argument('-i', '--input', help='Path to IV JSON files, e.g. "data/*.json"', required=True)
    parser.add_argument('--do_amac_offset', dest='do_amac_offset', action='store_true')
    parser.add_argument('--do_logY', dest='do_logY', action='store_true')
    parser.add_argument('--max_workers', type=int, default=6, help='Number of modules to run at once')
    args = parser.parse_args()

    l_input_files = sorted(glob(args.input))
    do_amac_offset = args.do_amac_offset
    do_logY = args.do_logY

    if not l_input_files:
        print(f"No input files found for pattern: {args.input}")
        return

    # -----------------------------
    # LIST OF SERIAL NUMBERS
    # -----------------------------
    serial_numbers = [
    "20USBML1235274","20USBML1235275","20USBML1235276","20USBML1235277","20USBML1235278",
    "20USBML1235279","20USBML1235280","20USBML1235281","20USBML1235282","20USBML1235730",
    "20USBML1235731","20USBML1235747","20USBML1235748","20USBML1235749","20USBML1235750",
    "20USBML1235755","20USBML1235756","20USBML1235757","20USBML1235758","20USBML1235760",
    "20USBML1235761","20USBML1235762","20USBML1235763","20USBML1235850","20USBML1235851",
    "20USBML1235852","20USBML1235853","20USBML1235873","20USBML1235874","20USBML1235875",
    "20USBML1235876","20USBML1235877","20USBML1235878","20USBML1235879","20USBML1235880",
    "20USBML1235881","20USBML1235882","20USBML1235883","20USBML1235884","20USBML1235885",
    "20USBML1235886","20USBML1235887","20USBML1235888","20USBML1235889","20USBML1235907",
    "20USBML1235908","20USBML1235909","20USBML1235919","20USBML1235920","20USBML1235921",
    "20USBML1235922","20USBML1235923","20USBML1235924","20USBML1235925","20USBML1235926",
    "20USBML1235927","20USBML1235928","20USBML1235929","20USBML1236083","20USBML1236084",
    "20USBML1236085","20USBML1236086","20USBML1236087","20USBML1236088","20USBML1236090",
    "20USBML1236091","20USBML1236092","20USBML1236093","20USBML1236094","20USBML1236095",
    "20USBML1236096","20USBML1236097","20USBML1236098","20USBML1236100","20USBML1236101",
    "20USBML1236102","20USBML1236103","20USBML1236104","20USBML1236105","20USBML1236106",
    "20USBML1236107","20USBML1236108","20USBML1236109","20USBML1236110","20USBML1236111",
    "20USBML1236112","20USBML1236113","20USBML1236148","20USBML1236149","20USBML1236150",
    "20USBML1236151","20USBML1236152","20USBML1236153","20USBML1236154","20USBML1236155",
    "20USBML1236156","20USBML1236157","20USBML1236158","20USBML1236159","20USBML1236160",
    "20USBML1236161","20USBML1236162","20USBML1236163","20USBML1236164","20USBML1236165",
    "20USBML1236166","20USBML1236167","20USBML1236168","20USBML1236169","20USBML1236170",
    "20USBML1236171","20USBML1236172","20USBML1236173","20USBML1236174","20USBML1236175",
    "20USBML1236337","20USBML1236338","20USBML1236339","20USBML1236340","20USBML1236341",
    "20USBML1236342","20USBML1236343","20USBML1236344","20USBML1236448","20USBML1236449",
    "20USBML1236450","20USBML1236451","20USBML1236452","20USBML1236453","20USBML1236454",
    "20USBML1236455","20USBML1236456","20USBML1236457","20USBML1236565","20USBML1236566",
    "20USBML1236567","20USBML1236568","20USBML1236604","20USBML1236605","20USBML1236606",
    "20USBML1236607","20USBML1236608","20USBML1236609","20USBML1236610","20USBML1236611",
    "20USBML1236612","20USBML1236613","20USBML1236614","20USBML1236615","20USBML1236677",
    "20USBML1236678","20USBML1236679","20USBML1236680","20USBML1236681","20USBML1236682",
    "20USBML1236683","20USBML1236684","20USBML1236685","20USBML1236686","20USBML1236687",
    "20USBML1236688","20USBML1236689","20USBML1236690","20USBML1236691","20USBML1236692",
    "20USBML1236693","20USBML1236694","20USBML1236695","20USBML1236696","20USBML1236697",
    "20USBML1236698","20USBML1236699","20USBML1236700","20USBML1236701","20USBML1236702",
    "20USBML1236703","20USBML1236704","20USBML1236705","20USBML1236706","20USBML1236707",
    "20USBML1236708","20USBML1236709","20USBML1236710","20USBML1236711","20USBML1236712",
    "20USBML1236713","20USBML1236714","20USBML1236715","20USBML1236716","20USBML1236717",
    "20USBML1236718","20USBML1236719","20USBML1236720","20USBML1236721","20USBML1236722",
    "20USBML1236723","20USBML1236724","20USBML1236725","20USBML1236726","20USBML1236727",
    "20USBML1236728","20USBML1236729","20USBML1236730","20USBML1236731","20USBML1236732",
    "20USBML1236733","20USBML1236734","20USBML1236676","20USBML1237010","20USBML1237011",
    "20USBML1237012","20USBML1237013","20USBML1237014","20USBML1237015","20USBML1237016",
    "20USBML1237017","20USBML1237018","20USBML1237019","20USBML1237020","20USBML1237021",
    "20USBML1237022","20USBML1237023","20USBML1237024","20USBML1237025","20USBML1237026",
    "20USBML1237027","20USBML1237028","20USBML1237029","20USBML1237080","20USBML1237081",
    "20USBML1237082","20USBML1237083","20USBML1237084","20USBML1237085","20USBML1237086",
    "20USBML1237087","20USBML1237088","20USBML1237089","20USBML1237090","20USBML1237091",
    "20USBML1237092","20USBML1237093","20USBML1237094","20USBML1237095","20USBML1237096",
    "20USBML1237097","20USBML1237098","20USBML1237099","20USBML1237100","20USBML1237101",
    "20USBML1237102","20USBML1237103","20USBML1237104","20USBML1237105","20USBML1237106",
    "20USBML1237107","20USBML1237108","20USBML1237109","20USBML1237110","20USBML1237111",
    "20USBML1237112","20USBML1237113","20USBML1237114","20USBML1237115","20USBML1237116",
    "20USBML1237117","20USBML1237118","20USBML1237119","20USBML1237120","20USBML1237121",
    "20USBML1237122","20USBML1237123","20USBML1237124","20USBML1237125","20USBML1237437",
    "20USBML1237438","20USBML1237439","20USBML1237440","20USBML1237441","20USBML1237442",
    "20USBML1237443","20USBML1237444","20USBML1237445","20USBML1237446","20USBML1237447",
    "20USBML1237448","20USBML1237449","20USBML1237450","20USBML1237451","20USBML1237452",
    "20USBML1237453","20USBML1237454","20USBML1237455","20USBML1237456","20USBML1237457",
    "20USBML1237458","20USBML1237459","20USBML1237460","20USBML1237461","20USBML1237462",
    "20USBML1237463","20USBML1237464","20USBML1237465","20USBML1237466","20USBML1237467",
    "20USBML1237468","20USBML1237469","20USBML1237470","20USBML1237471","20USBML1237472",
    "20USBML1237473","20USBML1237474","20USBML1237475","20USBML1237860","20USBML1237861",
    "20USBML1237862","20USBML1237863","20USBML1237864","20USBML1237865","20USBML1237866",
    "20USBML1237867","20USBML1237868","20USBML1237869","20USBML1237870","20USBML1237871",
    "20USBML1237872","20USBML1237873","20USBML1237874","20USBML1237875","20USBML1237876",
    "20USBML1237877","20USBML1237878","20USBML1237879","20USBML1237880","20USBML1237881",
    "20USBML1237882","20USBML1237883","20USBML1237884"
]

    l_module_names = serial_numbers

    print('\nJSON output data files to consider:')
    pprint(l_input_files)
    print('\nModule names selected to make plots:')
    pprint(l_module_names)

    if args.max_workers <= 1:
        for module_name in l_module_names:
            try:
                mk_single_plot(module_name, l_input_files, do_amac_offset, do_logY)
            except Exception as e:
                print(f"⚠️ Failed processing module {module_name}: {e}")
    else:
        print(f"\nRunning with max_workers = {args.max_workers}")
        with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {
                executor.submit(
                    mk_single_plot,
                    module_name,
                    l_input_files,
                    do_amac_offset,
                    do_logY
                ): module_name
                for module_name in l_module_names
            }

            for future in as_completed(futures):
                module_name = futures[future]
                try:
                    future.result()
                    print(f"✅ Finished module: {module_name}")
                except Exception as e:
                    print(f"⚠️ Failed processing module {module_name}: {e}")


def mk_single_plot(in_name, l_input_files, do_amac_offset, do_logY):
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)
    print(f'Making plot for {in_name}')

    l_input_files_amac = []
    for f in l_input_files:
        try:
            with open(f, 'r') as jf:
                data = json.load(jf)

            name = data.get("component", data.get("serial_number", ""))
            name_stripped = str(name).replace("SN", "")

            if name == in_name or name == f"SN{in_name}" or name_stripped == in_name:
                l_input_files_amac.append(f)

        except Exception as e:
            print(f"⚠️ Failed to parse {f}: {e}")

    if not l_input_files_amac:
        print(f"⚠️ No matching files found for module {in_name}")
        plt.close(fig)
        return

    d_unsorted = {}
    for input_file in l_input_files_amac:
        try:
            input_dict = json_to_dict(input_file)
            timestamp = input_dict.get('timestamp', input_dict.get('date', '1970-01-01T00:00:00Z'))
            sort_key = f"{timestamp}_{os.path.basename(input_file)}"
            d_unsorted[sort_key] = input_file
        except Exception as e:
            print(f"⚠️ Failed to parse/sort {input_file}: {e}")

    od = collections.OrderedDict(sorted(d_unsorted.items()))
    l_input_files_sorted = list(od.values())

    print('AMAC sorted dictionary values:')
    pprint(l_input_files_sorted)

    blues = mplt.cm.Blues(np.linspace(0.4, 0.9, max(len(l_input_files_sorted), 1)))
    oranges = mplt.cm.Oranges(np.linspace(0.4, 0.9, max(len(l_input_files_sorted), 1)))

    plotted_anything = False

    for count, input_file in enumerate(l_input_files_sorted):
        if '.json' not in input_file:
            continue

        voltages, currents, timestamp, ntcpb_temp, ntcx_temp = read_AMAC_IV(input_file, do_amac_offset)

        if len(voltages) == 0 or len(currents) == 0:
            print(f"⚠️ Skipping plot for {input_file} due to empty or missing data.")
            continue

        print(f"Plotting {len(voltages)} points for file: {input_file}")

        lcolour = blues[count] if ntcpb_temp < 0 else oranges[count]
        ntcx_txt = '{0:.3g}'.format(ntcx_temp).replace('-', '$-$')

        ax.plot(
            voltages,
            currents,
            lw=2,
            ls='-',
            c=lcolour,
            label='{0}, {1}C'.format(timestamp, ntcx_txt)
        )
        plotted_anything = True

    if not plotted_anything:
        print(f"⚠️ No valid IV data found for module {in_name}")
        plt.close(fig)
        return

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

    ax.legend(
        loc='upper left',
        prop={'size': 14},
        frameon=False,
        handlelength=2.1,
        handletextpad=0.5,
        borderpad=0.6,
        ncol=3,
        columnspacing=0.6
    )

    fig.text(0.20, 0.56, in_name, color='k', size=text_size)
    fig.text(0.20, 0.51, 'Temperatures = AMAC NTCx', color='gray', size=text_size * 0.5)

    plt.tight_layout(pad=0.3)
    plt.subplots_adjust(top=0.97, left=0.16, right=0.99)

    # Save to SN<serial>/IV/SN<serial>.pdf
    module_folder_name = f"SN{in_name}"
    plot_dir = os.path.join(module_folder_name, "IV")
    mkdir(plot_dir)

    save_name = os.path.join(plot_dir, module_folder_name)
    print(f"Saving plot as {save_name}.pdf")
    plt.savefig(f"{save_name}.pdf", format='pdf')
    plt.savefig(f"{save_name}.png", format='png', dpi=300)
    plt.close(fig)


def read_AMAC_IV(file_name, do_AMAC_offset=True):
    print(f'Opening file: {file_name}')
    with open(file_name, 'r') as infile:
        input_dict = json.load(infile)

    results = input_dict.get('results', {})
    current_raw = results.get('CURRENT') or results.get('current')
    voltage_raw = results.get('VOLTAGE') or results.get('voltage')

    if current_raw is None or voltage_raw is None:
        print(f"⚠️ Skipping {file_name} — missing current or voltage data.")
        return [], [], "INVALID", 0.0, 0.0

    if len(current_raw) == 0 or len(voltage_raw) == 0:
        print(f"⚠️ Skipping {file_name} — empty current or voltage data.")
        return [], [], "INVALID", 0.0, 0.0

    current_zero_offset = float(current_raw[0]) if do_AMAC_offset else 0.0
    print(f'Using AMAC current zero offset: {current_zero_offset}')

    try:
        voltages = [abs(float(x)) for x in voltage_raw]
        currents = [float(x) - current_zero_offset for x in current_raw]
    except Exception as e:
        print(f"⚠️ Failed converting IV data in {file_name}: {e}")
        return [], [], "INVALID", 0.0, 0.0

    if all(i == 0 for i in currents) or all(v == 0 for v in voltages):
        print(f"⚠️ Warning: Empty or zero IV data in {file_name}")

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
    timestamp_stripped = timestamp.replace('T', ' ').replace('Z', '').split('.')[0]

    try:
        pydate_datetime_stamp = datetime.datetime.strptime(timestamp_stripped, '%Y-%m-%d %H:%M:%S')
        out_datetime = pydate_datetime_stamp.strftime('%Y-%m-%d %H:%M')
    except ValueError:
        out_datetime = "Invalid Time"

    return voltages, currents, out_datetime, ntcpb_temp, ntcx_temp


def json_to_dict(file_name):
    with open(file_name, 'r') as infile:
        return json.load(infile)


def get_module_names(l_filtered_input_files):
    l_module_names = []
    for input_file in l_filtered_input_files:
        if '.json' in input_file:
            try:
                input_dict = json_to_dict(input_file)
                module_name = input_dict.get('component', input_dict.get('serial_number', 'UNKNOWN'))
                module_name = str(module_name).replace("SN", "")
                if module_name not in l_module_names:
                    l_module_names.append(module_name)
            except Exception as e:
                print(f"⚠️ Could not read module name from {input_file}: {e}")
    l_module_names.sort()
    return l_module_names


def mkdir(dirPath):
    try:
        os.makedirs(dirPath, exist_ok=True)
        print('Successfully made directory:', dirPath)
    except OSError as e:
        print(f"⚠️ Could not create directory {dirPath}: {e}")


if __name__ == "__main__":
    main()