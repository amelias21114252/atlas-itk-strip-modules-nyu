#!/usr/bin/env python3

# python get_all_tests_categoryE_i_lbnl.py --test_name "Module AMAC IV TC"

import os
import json
import argparse
import itkdb

serial_numbers = [
    "20USBML1236979",
    "20USBML1236980",
    "20USBML1236981",
    "20USBML1236982",
    "20USBML1236983",
    "20USBML1236984",
    "20USBML1236985",
    "20USBML1236986",
    "20USBML1236987",
    "20USBML1236988",
    "20USBML1236989",
    "20USBML1236990",
    "20USBML1237030",
    "20USBML1237031",
    "20USBML1237032",
    "20USBML1237033",
    "20USBML1237034",
    "20USBML1237035",
    "20USBML1237046",
    "20USBML1237047",
    "20USBML1237048",
    "20USBML1237049",
    "20USBML1237050",
    "20USBML1237051",
    "20USBML1237068",
    "20USBML1237069",
    "20USBML1237070",
    "20USBML1237071",
    "20USBML1237072",
    "20USBML1237073",
    "20USBML1237074",
    "20USBML1237075",
    "20USBML1237076",
    "20USBML1237077",
    "20USBML1237078",
    "20USBML1237079",
    "20USBML1237134",
    "20USBML1237135",
    "20USBML1237136",
    "20USBML1237137",
    "20USBML1237138",
    "20USBML1237139",
    "20USBML1237155",
    "20USBML1237156",
    "20USBML1237157",
    "20USBML1237158",
    "20USBML1237159",
    "20USBML1237160",
    "20USBML1237191",
    "20USBML1237192",
    "20USBML1237193",
    "20USBML1237194",
    "20USBML1237195",
    "20USBML1237196",
    "20USBML1237197",
    "20USBML1237198",
    "20USBML1237199",
    "20USBML1237200",
    "20USBML1237201",
    "20USBML1237202",
    "20USBML1237228",
    "20USBML1237229",
    "20USBML1237230",
    "20USBML1237231",
    "20USBML1237232",
    "20USBML1237233",
    "20USBML1237234",
    "20USBML1237235",
    "20USBML1237236",
    "20USBML1237237",
    "20USBML1237238",
    "20USBML1237239",
    "20USBML1237388",
    "20USBML1237389",
    "20USBML1237390",
    "20USBML1237391",
    "20USBML1237392",
    "20USBML1237393",
    "20USBML1237394",
    "20USBML1237395",
    "20USBML1237396",
    "20USBML1237397",
    "20USBML1237398",
    "20USBML1237399",
    "20USBML1237567",
    "20USBML1237568",
    "20USBML1237569",
    "20USBML1237570",
    "20USBML1237571",
    "20USBML1237572",
    "20USBML1237573",
    "20USBML1237574",
    "20USBML1237575",
    "20USBML1237576",
    "20USBML1237577",
    "20USBML1237578",
    "20USBML1237579",
    "20USBML1237580",
    "20USBML1237581",
    "20USBML1237582",
    "20USBML1237583",
    "20USBML1237584",
    "20USBML1237587",
    "20USBML1237588",
    "20USBML1237589",
    "20USBML1237590",
    "20USBML1237591",
    "20USBML1237592",
    "20USBML1237593",
    "20USBML1237594",
    "20USBML1237595",
    "20USBML1237596",
    "20USBML1237597",
    "20USBML1237598",
    "20USBML1237599",
    "20USBML1237600",
    "20USBML1237601",
    "20USBML1237602",
    "20USBML1237603",
    "20USBML1237604",
    "20USBML1237605",
    "20USBML1237606",
    "20USBML1237607",
    "20USBML1237608",
    "20USBML1237609",
    "20USBML1237610",
    "20USBML1237626",
    "20USBML1237627",
    "20USBML1237628",
    "20USBML1237654",
    "20USBML1237655",
    "20USBML1237656",
    "20USBML1237715",
    "20USBML1237716",
    "20USBML1237717",
    "20USBML1237718",
    "20USBML1237719",
    "20USBML1237720",
    "20USBML1237773",
    "20USBML1237774",
    "20USBML1237775",
    "20USBML1237776",
    "20USBML1237777",
    "20USBML1237778",
    "20USBML1237791",
    "20USBML1237792",
    "20USBML1237793",
    "20USBML1237794",
    "20USBML1237795",
    "20USBML1237796",
    "20USBML1237797",
    "20USBML1237798",
    "20USBML1237799",
    "20USBML1237800",
    "20USBML1237801",
    "20USBML1237802",
    "20USBML1237829",
    "20USBML1237830",
    "20USBML1237831",
    "20USBML1237832",
    "20USBML1237833",
    "20USBML1237834",
    "20USBML1237854",
    "20USBML1237855",
    "20USBML1237856",
    "20USBML1237857",
    "20USBML1237858",
    "20USBML1237859",
    "20USBML1237925",
    "20USBML1237926",
    "20USBML1237927",
    "20USBML1237928",
    "20USBML1237980",
    "20USBML1238004",
    "20USBML1238005",
    "20USBML1238006",
    "20USBML1238007",
    "20USBML1238008",
    "20USBML1238009",
    "20USBML1238010",
    "20USBML1238011",
    "20USBML1238012",
    "20USBML1238069",
    "20USBML1238070",
    "20USBML1238071",
    "20USBML1238072",
    "20USBML1238089",
    "20USBML1238090",
    "20USBML1238091",
    "20USBML1238135",
    "20USBML1238136",
    "20USBML1238137",
    "20USBML1238138",
    "20USBML1238139",
    "20USBML1238140",
    "20USBML1238141",
    "20USBML1238142",
    "20USBML1238167",
    "20USBML1238168",
    "20USBML1238169",
    "20USBML1238170",
    "20USBML1238171",
    "20USBML1238208",
    "20USBML1238209",
    "20USBML1238210",
    "20USBML1238211",
    "20USBML1238212",
    "20USBML1238213",
    "20USBML1238214",
    "20USBML1238215",
    "20USBML1238216",
    "20USBML1238217",
    "20USBML1238218",
    "20USBML1238219",
    "20USBML1238348",
    "20USBML1238349",
    "20USBML1238350",
    "20USBML1238351",
    "20USBML1238352",
    "20USBML1238353",
    "20USBML1238355",
    "20USBML1238356",
    "20USBML1238357",
    "20USBML1238358",
    "20USBML1238402",
    "20USBML1238404",
    "20USBML1238405",
    "20USBML1238406",
    "20USBML1238407",
    "20USBML1238408",
    "20USBML1238455",
    "20USBML1238456",
    "20USBML1238457",
    "20USBML1238458",
    "20USBML1238459",
    "20USBML1238531",
    "20USBML1238590",
    "20USBML1238591",
    "20USBML1238592",
    "20USBML1238593",
    "20USBML1238616",
    "20USBML1238617",
    "20USBML1238618",
    "20USBML1238619",
    "20USBML1238620",
    "20USBML1238769",
    "20USBML1238770",
    "20USBML1238771",
    "20USBML1238772",
    "20USBML1238773",
    "20USBML1238774",
    "20USBML1238775",
    "20USBML1238776",
    "20USBML1238777",
    "20USBML1238778",
    "20USBML1238779",
    "20USBML1238780",
    "20USBML1238781",
    "20USBML1238782",
    "20USBML1238783",
    "20USBML1238784",
    "20USBML1238785",
    "20USBML1238786",
    "20USBML1238787",
    "20USBML1238788",
    "20USBML1238789",
    "20USBML1238790",
    "20USBML1238791",
    "20USBML1238792",
    "20USBML1238793",
    "20USBML1238794",
    "20USBML1238795",
    "20USBML1238796",
    "20USBML1238797",
    "20USBML1238798",
    "20USBML1238799",
    "20USBML1238800",
    "20USBML1238801",
    "20USBML1238802",
    "20USBML1238803",
    "20USBML1238804",
    "20USBML1238805",
    "20USBML1238806",
    "20USBML1238807",
    "20USBML1238808",
    "20USBML1238809",
    "20USBML1238810",
    "20USBML1238811",
    "20USBML1238812",
    "20USBML1238813",
    "20USBML1238814",
    "20USBML1238815",
    "20USBML1238816",
    "20USBML1238817",
    "20USBML1238818",
    "20USBML1238819",
    "20USBML1238820",
    "20USBML1238821",
    "20USBML1238822",
    "20USBML1238823",
    "20USBML1238824",
    "20USBML1238825",
    "20USBML1238826",
    "20USBML1238827",
    "20USBML1238828",
    "20USBML1238829",
    "20USBML1238830",
    "20USBML1238831",
    "20USBML1238832",
    "20USBML1238833",
    "20USBML1238834",
    "20USBML1238835",
    "20USBML1238836",
    "20USBML1238837",
    "20USBML1238838",
    "20USBML1238839",
    "20USBML1238840",
    "20USBML1238841",
    "20USBML1238842",
    "20USBML1238843",
    "20USBML1238844",
    "20USBML1238845",
    "20USBML1238846",
    "20USBML1238847",
    "20USBML1238848",
    "20USBML1238849",
    "20USBML1238850",
    "20USBML1238851",
    "20USBML1239099",
    "20USBML1239100",
    "20USBML1239101",
    "20USBML1239102",
    "20USBML1239103",
    "20USBML1239104",
    "20USBML1239105",
    "20USBML1239106",
    "20USBML1239107",
    "20USBML1239108",
    "20USBML1239109",
    "20USBML1239110",
    "20USBML1239111",
    "20USBML1239112",
    "20USBML1239113",
    "20USBML1239114",
    "20USBML1239115",
    "20USBML1239116",
    "20USBML1239117",
    "20USBML1239118",
    "20USBML1239119",
    "20USBML1239120",
    "20USBML1239121",
    "20USBML1239122",
    "20USBML1239178",
    "20USBML1239179",
    "20USBML1239180",
    "20USBML1239181",
    "20USBML1239182",
    "20USBML1239183",
    "20USBML1239184",
    "20USBML1239185",
    "20USBML1239186",
    "20USBML1239187",
    "20USBML1239188",
    "20USBML1239189",
    "20USBML1239190",
    "20USBML1239191",
    "20USBML1239192",
    "20USBML1239193",
    "20USBML1239194",
    "20USBML1239195",
    "20USBML1239196",
    "20USBML1239197",
    "20USBML1239261",
    "20USBML1239262",
    "20USBML1239263",
    "20USBML1239264",
    "20USBML1239265",
    "20USBML1239266",
    "20USBML1239267",
    "20USBML1239268",
    "20USBML1239269",
    "20USBML1239270",
    "20USBML1239271",
    "20USBML1239272",
    "20USBML1239273",
    "20USBML1239274",
    "20USBML1239275",
    "20USBML1239276",
    "20USBML1239277",
    "20USBML1239278",
    "20USBML1239279",
]


def get_test_run(client, serial_number, test_name):

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

        output_dir = f"SN{serial_number}"
        os.makedirs(output_dir, exist_ok=True)

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

            filename = os.path.join(
                output_dir,
                f"SN{serial_number}_{i+1:02}.json"
            )

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
        description="Run ITkDB Module AMAC IV extraction for many serials"
    )

    parser.add_argument(
        "--test_name",
        default="Module AMAC IV TC",
        help="Test name"
    )

    args = parser.parse_args()

    token = os.getenv("ITK_DB_AUTH")

    if not token:
        raise RuntimeError("ITK_DB_AUTH environment variable not set")

    user = itkdb.core.UserBearer(bearer=token)
    client = itkdb.Client(user=user)

    passed = []
    category_e_i_failed = []

    for i, serial in enumerate(serial_numbers, start=1):

        print("\n" + "=" * 80)
        print(f"[{i}/{len(serial_numbers)}] Running {serial}")

        success = get_test_run(
            client=client,
            serial_number=serial,
            test_name=args.test_name
        )

        if success:
            passed.append(serial)
        else:
            category_e_i_failed.append(serial)

    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)

    print(f"\n✅ PASSED ({len(passed)}):")
    for serial in passed:
        print(f"  ✅ {serial}")

    print(f"\n❌ CATEGORY E(i) FAILED ({len(category_e_i_failed)}):")
    print("Category E(i): IV data could not be found or processed")

    for serial in category_e_i_failed:
        print(f"  ❌ {serial}")