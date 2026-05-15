#!/usr/bin/env python3

# python get_all_tests_categoryE_i_bnl.py --test_name "Module AMAC IV TC"

import os
import json
import argparse
import itkdb
from pathlib import Path

serial_numbers = [
    "20USBML1235091",
    "20USBML1235094",
    "20USBML1235097",
    "20USBML1235096",
    "20USBML1235090",
    "20USBML1235100",
    "20USBML1235093",
    "20USBML1235095",
    "20USBML1235098",
    "20USBML1235092",
    "20USBML1235101",
    "20USBML1235102",
    "20USBML1235099",
    "20USBML1235274",
    "20USBML1235275",
    "20USBML1235276",
    "20USBML1235277",
    "20USBML1235278",
    "20USBML1235279",
    "20USBML1235280",
    "20USBML1235281",
    "20USBML1235282",
    "20USBML1235730",
    "20USBML1235731",
    "20USBML1235747",
    "20USBML1235748",
    "20USBML1235749",
    "20USBML1235750",
    "20USBML1235755",
    "20USBML1235756",
    "20USBML1235757",
    "20USBML1235758",
    "20USBML1235760",
    "20USBML1235761",
    "20USBML1235762",
    "20USBML1235763",
    "20USBML1235850",
    "20USBML1235851",
    "20USBML1235852",
    "20USBML1235853",
    "20USBML1235873",
    "20USBML1235874",
    "20USBML1235875",
    "20USBML1235876",
    "20USBML1235877",
    "20USBML1235878",
    "20USBML1235879",
    "20USBML1235880",
    "20USBML1235881",
    "20USBML1235882",
    "20USBML1235883",
    "20USBML1235884",
    "20USBML1235885",
    "20USBML1235886",
    "20USBML1235887",
    "20USBML1235888",
    "20USBML1235889",
    "20USBML1235907",
    "20USBML1235908",
    "20USBML1235909",
    "20USBML1235919",
    "20USBML1235920",
    "20USBML1235921",
    "20USBML1235922",
    "20USBML1235923",
    "20USBML1235924",
    "20USBML1235925",
    "20USBML1235926",
    "20USBML1235927",
    "20USBML1235928",
    "20USBML1235929",
    "20USBML1236083",
    "20USBML1236084",
    "20USBML1236085",
    "20USBML1236086",
    "20USBML1236087",
    "20USBML1236088",
    "20USBML1236090",
    "20USBML1236091",
    "20USBML1236092",
    "20USBML1236093",
    "20USBML1236094",
    "20USBML1236095",
    "20USBML1236096",
    "20USBML1236097",
    "20USBML1236098",
    "20USBML1236100",
    "20USBML1236101",
    "20USBML1236102",
    "20USBML1236103",
    "20USBML1236104",
    "20USBML1236105",
    "20USBML1236106",
    "20USBML1236107",
    "20USBML1236108",
    "20USBML1236109",
    "20USBML1236110",
    "20USBML1236111",
    "20USBML1236112",
    "20USBML1236113",
    "20USBML1236148",
    "20USBML1236149",
    "20USBML1236150",
    "20USBML1236151",
    "20USBML1236152",
    "20USBML1236153",
    "20USBML1236154",
    "20USBML1236155",
    "20USBML1236156",
    "20USBML1236157",
    "20USBML1236158",
    "20USBML1236159",
    "20USBML1236160",
    "20USBML1236161",
    "20USBML1236162",
    "20USBML1236163",
    "20USBML1236164",
    "20USBML1236165",
    "20USBML1236166",
    "20USBML1236167",
    "20USBML1236168",
    "20USBML1236169",
    "20USBML1236170",
    "20USBML1236171",
    "20USBML1236172",
    "20USBML1236173",
    "20USBML1236174",
    "20USBML1236175",
    "20USBML1236337",
    "20USBML1236338",
    "20USBML1236339",
    "20USBML1236340",
    "20USBML1236341",
    "20USBML1236342",
    "20USBML1236343",
    "20USBML1236344",
    "20USBML1236448",
    "20USBML1236449",
    "20USBML1236450",
    "20USBML1236451",
    "20USBML1236452",
    "20USBML1236453",
    "20USBML1236454",
    "20USBML1236455",
    "20USBML1236456",
    "20USBML1236457",
    "20USBML1236565",
    "20USBML1236566",
    "20USBML1236567",
    "20USBML1236568",
    "20USBML1236604",
    "20USBML1236605",
    "20USBML1236606",
    "20USBML1236607",
    "20USBML1236608",
    "20USBML1236609",
    "20USBML1236610",
    "20USBML1236611",
    "20USBML1236612",
    "20USBML1236613",
    "20USBML1236614",
    "20USBML1236615",
    "20USBML1236677",
    "20USBML1236678",
    "20USBML1236679",
    "20USBML1236680",
    "20USBML1236681",
    "20USBML1236682",
    "20USBML1236683",
    "20USBML1236684",
    "20USBML1236685",
    "20USBML1236686",
    "20USBML1236687",
    "20USBML1236688",
    "20USBML1236689",
    "20USBML1236690",
    "20USBML1236691",
    "20USBML1236692",
    "20USBML1236693",
    "20USBML1236694",
    "20USBML1236695",
    "20USBML1236696",
    "20USBML1236697",
    "20USBML1236698",
    "20USBML1236699",
    "20USBML1236700",
    "20USBML1236701",
    "20USBML1236702",
    "20USBML1236703",
    "20USBML1236704",
    "20USBML1236705",
    "20USBML1236706",
    "20USBML1236707",
    "20USBML1236708",
    "20USBML1236709",
    "20USBML1236710",
    "20USBML1236711",
    "20USBML1236712",
    "20USBML1236713",
    "20USBML1236714",
    "20USBML1236715",
    "20USBML1236716",
    "20USBML1236717",
    "20USBML1236718",
    "20USBML1236719",
    "20USBML1236720",
    "20USBML1236721",
    "20USBML1236722",
    "20USBML1236723",
    "20USBML1236724",
    "20USBML1236725",
    "20USBML1236726",
    "20USBML1236727",
    "20USBML1236728",
    "20USBML1236729",
    "20USBML1236730",
    "20USBML1236731",
    "20USBML1236732",
    "20USBML1236733",
    "20USBML1236676",
    "20USBML1236734",
    "20USBML1237010",
    "20USBML1237011",
    "20USBML1237012",
    "20USBML1237013",
    "20USBML1237014",
    "20USBML1237015",
    "20USBML1237016",
    "20USBML1237017",
    "20USBML1237018",
    "20USBML1237019",
    "20USBML1237020",
    "20USBML1237021",
    "20USBML1237022",
    "20USBML1237023",
    "20USBML1237024",
    "20USBML1237025",
    "20USBML1237026",
    "20USBML1237027",
    "20USBML1237028",
    "20USBML1237029",
    "20USBML1237080",
    "20USBML1237081",
    "20USBML1237082",
    "20USBML1237083",
    "20USBML1237084",
    "20USBML1237085",
    "20USBML1237086",
    "20USBML1237087",
    "20USBML1237088",
    "20USBML1237089",
    "20USBML1237090",
    "20USBML1237091",
    "20USBML1237092",
    "20USBML1237093",
    "20USBML1237094",
    "20USBML1237095",
    "20USBML1237096",
    "20USBML1237097",
    "20USBML1237098",
    "20USBML1237099",
    "20USBML1237100",
    "20USBML1237101",
    "20USBML1237102",
    "20USBML1237103",
    "20USBML1237104",
    "20USBML1237105",
    "20USBML1237106",
    "20USBML1237107",
    "20USBML1237108",
    "20USBML1237109",
    "20USBML1237110",
    "20USBML1237111",
    "20USBML1237112",
    "20USBML1237113",
    "20USBML1237114",
    "20USBML1237115",
    "20USBML1237116",
    "20USBML1237117",
    "20USBML1237118",
    "20USBML1237119",
    "20USBML1237120",
    "20USBML1237121",
    "20USBML1237122",
    "20USBML1237123",
    "20USBML1237124",
    "20USBML1237125",
    "20USBML1237437",
    "20USBML1237438",
    "20USBML1237439",
    "20USBML1237440",
    "20USBML1237441",
    "20USBML1237442",
    "20USBML1237443",
    "20USBML1237444",
    "20USBML1237445",
    "20USBML1237446",
    "20USBML1237447",
    "20USBML1237448",
    "20USBML1237449",
    "20USBML1237450",
    "20USBML1237451",
    "20USBML1237452",
    "20USBML1237453",
    "20USBML1237454",
    "20USBML1237455",
    "20USBML1237456",
    "20USBML1237457",
    "20USBML1237458",
    "20USBML1237459",
    "20USBML1237460",
    "20USBML1237461",
    "20USBML1237462",
    "20USBML1237463",
    "20USBML1237464",
    "20USBML1237465",
    "20USBML1237466",
    "20USBML1237467",
    "20USBML1237468",
    "20USBML1237469",
    "20USBML1237470",
    "20USBML1237471",
    "20USBML1237472",
    "20USBML1237473",
    "20USBML1237474",
    "20USBML1237475",
    "20USBML1237860",
    "20USBML1237861",
    "20USBML1237862",
    "20USBML1237863",
    "20USBML1237864",
    "20USBML1237865",
    "20USBML1237866",
    "20USBML1237867",
    "20USBML1237868",
    "20USBML1237869",
    "20USBML1237870",
    "20USBML1237871",
    "20USBML1237872",
    "20USBML1237873",
    "20USBML1237874",
    "20USBML1237875",
    "20USBML1237876",
    "20USBML1237877",
    "20USBML1237878",
    "20USBML1237879",
    "20USBML1237880",
    "20USBML1237881",
    "20USBML1237882",
    "20USBML1237883",
    "20USBML1237884",
    "20USBML1237885",
    "20USBML1237886",
    "20USBML1237887",
    "20USBML1237888",
    "20USBML1237889",
    "20USBML1237890",
    "20USBML1237891",
    "20USBML1237892",
    "20USBML1237893",
    "20USBML1237894",
    "20USBML1237895",
    "20USBML1237896",
    "20USBML1237897",
    "20USBML1237898",
    "20USBML1237899",
    "20USBML1237900",
    "20USBML1238073",
    "20USBML1238074",
    "20USBML1238075",
    "20USBML1238076",
    "20USBML1238077",
    "20USBML1238078",
    "20USBML1238079",
    "20USBML1238080",
    "20USBML1238081",
    "20USBML1238082",
    "20USBML1238083",
    "20USBML1238084",
    "20USBML1238085",
    "20USBML1238086",
    "20USBML1238087",
    "20USBML1238088",
    "20USBML1238498",
    "20USBML1238499",
    "20USBML1238500",
    "20USBML1238501",
    "20USBML1238502",
    "20USBML1238503",
    "20USBML1238504",
    "20USBML1238505",
    "20USBML1238506",
    "20USBML1238507",
    "20USBML1238508",
    "20USBML1238509",
    "20USBML1238510",
    "20USBML1238511",
    "20USBML1238512",
    "20USBML1238513",
    "20USBML1238514",
    "20USBML1238515",
    "20USBML1238516",
    "20USBML1238517",
    "20USBML1238518",
    "20USBML1238519",
    "20USBML1238520",
    "20USBML1238521",
    "20USBML1238522",
    "20USBML1238523",
    "20USBML1238524",
    "20USBML1238525",
    "20USBML1238526",
    "20USBML1238527",
    "20USBML1238528",
    "20USBML1238529",
    "20USBML1238530",
    "20USBML1238679",
    "20USBML1238680",
    "20USBML1238681",
    "20USBML1238682",
    "20USBML1238683",
    "20USBML1238684",
    "20USBML1238685",
    "20USBML1238686",
    "20USBML1238687",
    "20USBML1238688",
    "20USBML1238689",
    "20USBML1238690",
    "20USBML1238691",
    "20USBML1238692",
    "20USBML1238693",
    "20USBML1238694",
    "20USBML1238695",
    "20USBML1238696",
    "20USBML1238697",
    "20USBML1238698",
    "20USBML1238699",
    "20USBML1238700",
    "20USBML1238701",
    "20USBML1238702",
    "20USBML1238703",
    "20USBML1238704",
    "20USBML1238705",
    "20USBML1238706",
    "20USBML1238707",
    "20USBML1238708",
    "20USBML1238709",
    "20USBML1238710",
    "20USBML1238711",
    "20USBML1239198",
    "20USBML1239199",
    "20USBML1239200",
    "20USBML1239201",
    "20USBML1239202",
    "20USBML1239203",
    "20USBML1239204",
    "20USBML1239205",
    "20USBML1239206",
    "20USBML1239207",
    "20USBML1239208",
    "20USBML1239209",
    "20USBML1239210",
    "20USBML1239211",
    "20USBML1239212",
    "20USBML1239213",
    "20USBML1239214",
    "20USBML1239215",
    "20USBML1239216",
    "20USBML1239217",
    "20USBML1239218",
    "20USBML1239219",
    "20USBML1239220",
    "20USBML1239221",
]





def write_python_list(f, title, values):

    f.write(f"{title} = [\n")

    for serial in values:

        f.write(f'    "{serial}",\n')

    f.write("]\n\n")

def get_test_run(client, serial_number, test_name, base_output_dir):

    try:

        component = client.get(

            "getComponent",

            json={"component": serial_number}

        )

        testID = [

            y["id"]

            for x in component["tests"]

            for y in x["testRuns"]

            if x["name"] == test_name

        ]

        if not testID:

            print(f"❌ CATEGORY E(i): No IV test run found for {serial_number}")

            return False

        print("=" * 80)

        print(f"Serial number: {serial_number}")

        print(f"Test name: {test_name}")

        print(f"Getting test ID: {testID[0]}")

        testRun = client.get(

            "getTestRun",

            json={"testRun": testID[0]}

        )

        timestamp = testRun["components"][0]["stateTs"]

        innse_under = []

        innse_away = []

        current = []

        voltage = []

        for x in testRun["results"]:

            if x.get("name") == "innse_under":

                innse_under = x.get("value", [])

            elif x.get("name") == "innse_away":

                innse_away = x.get("value", [])

            elif x.get("code") == "CURRENT":

                current = x.get("value", [])

            elif x.get("code") == "VOLTAGE":

                voltage = x.get("value", [])

        if not current or not voltage:

            print(f"❌ CATEGORY E(i): IV data could not be found or processed for {serial_number}")

            return False

        props = testRun["properties"][0]["value"] if testRun.get("properties") else {}

        amac_pb = props.get("AMAC_NTCpb")

        amac_x = props.get("AMAC_NTCx")

        amac_y = props.get("AMAC_NTCy")

        output_dir = base_output_dir / "ML" / f"SN{serial_number}"

        output_dir.mkdir(parents=True, exist_ok=True)

        for i in range(24):

            json_data = {

                "serial_number": serial_number,

                "test_name": test_name,

                "test_id": testID[0],

                "timestamp": timestamp,

                "properties": {

                    "DCS": {

                        "AMAC_NTCpb": amac_pb[i] if amac_pb and i < len(amac_pb) else None,

                        "AMAC_NTCx": amac_x[i] if amac_x and i < len(amac_x) else None,

                        "AMAC_NTCy": amac_y[i] if amac_y and i < len(amac_y) else None,

                    },

                    "det_info": {

                        "Address": list(range(10)),

                        "Channel": list(range(1, 11)),

                        "name": f"SN{serial_number}",

                    },

                    "fit_type_code": 4,

                },

                "index": i,

                "results": {

                    "innse_under": innse_under[i] if i < len(innse_under) else None,

                    "innse_away": innse_away[i] if i < len(innse_away) else None,

                    "current": current[i] if i < len(current) else None,

                    "voltage": voltage[i] if i < len(voltage) else None,

                },

            }

            filename = output_dir / f"SN{serial_number}_{i + 1:02}.json"

            with open(filename, "w") as f:

                json.dump(json_data, f, indent=2)

            print(f"✅ Wrote: {filename}")

        print(f"✅ Finished {serial_number}")

        return True

    except Exception as e:

        print(f"❌ CATEGORY E(i): IV data could not be found or processed for {serial_number}")

        print(f"Error: {e}")

        return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(

        description="Run ITkDB Module AMAC IV extraction for many BNL ML serials"

    )

    parser.add_argument(

        "--test_name",

        default="Module AMAC IV TC",

        help="Test name"

    )

    parser.add_argument(

        "--output_dir",

        default="BNL",

        help="Main output directory"

    )

    args = parser.parse_args()

    token = os.getenv("ITK_DB_AUTH")

    if not token:

        raise RuntimeError("ITK_DB_AUTH environment variable not set")

    user = itkdb.core.UserBearer(bearer=token)

    client = itkdb.Client(user=user)

    base_output_dir = Path(args.output_dir)

    ml_output_dir = base_output_dir / "ML"

    ml_output_dir.mkdir(parents=True, exist_ok=True)

    passed = []

    category_e_i_failed = []

    for i, serial in enumerate(serial_numbers, start=1):

        print("\n" + "=" * 80)

        print(f"[{i}/{len(serial_numbers)}] Running {serial}")

        success = get_test_run(

            client=client,

            serial_number=serial,

            test_name=args.test_name,

            base_output_dir=base_output_dir,

        )

        if success:

            passed.append(serial)

        else:

            category_e_i_failed.append(serial)

    summary_path = ml_output_dir / "summary_page_bnl_ml.txt"

    with open(summary_path, "w") as f:

        f.write("=" * 80 + "\n")

        f.write("BNL ML FINAL SUMMARY\n")

        f.write("=" * 80 + "\n\n")

        f.write(f"TOTAL MODULES CHECKED: {len(serial_numbers)}\n")

        f.write(f"WORKING MODULES: {len(passed)}\n")

        f.write(f"NOT WORKING MODULES: {len(category_e_i_failed)}\n\n")

        write_python_list(f, "working_modules", passed)

        write_python_list(f, "not_working_modules", category_e_i_failed)

    print("\n" + "=" * 80)

    print("BNL ML FINAL SUMMARY")

    print("=" * 80)

    print(f"\n✅ WORKING MODULES ({len(passed)}):")

    print("[")

    for serial in passed:

        print(f'    "{serial}",')

    print("]")

    print(f"\n❌ NOT WORKING MODULES ({len(category_e_i_failed)}):")

    print("[")

    for serial in category_e_i_failed:

        print(f'    "{serial}",')

    print("]")

    print(f"\n📄 Summary saved to: {summary_path}")