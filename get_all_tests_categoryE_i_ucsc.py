#!/usr/bin/env python3

# python get_all_tests_categoryE_i_ucsc.py --test_name "Module AMAC IV TC"

import os
import json
import argparse
import itkdb

serial_numbers = [
    "20USBML1236791",
    "20USBML1236792",
    "20USBML1236793",
    "20USBML1236794",
    "20USBML1236795",
    "20USBML1236796",
    "20USBML1236797",
    "20USBML1236798",
    "20USBML1236799",
    "20USBML1236800",
    "20USBML1236801",
    "20USBML1236802",
    "20USBML1236803",
    "20USBML1236804",
    "20USBML1236805",
    "20USBML1236806",
    "20USBML1236807",
    "20USBML1236808",
    "20USBML1236809",
    "20USBML1236810",
    "20USBML1236811",
    "20USBML1236892",
    "20USBML1236893",
    "20USBML1236956",
    "20USBML1236957",
    "20USBML1236958",
    "20USBML1236959",
    "20USBML1236960",
    "20USBML1236961",
    "20USBML1236962",
    "20USBML1236963",
    "20USBML1236964",
    "20USBML1236965",
    "20USBML1236966",
    "20USBML1236967",
    "20USBML1236968",
    "20USBML1236969",
    "20USBML1236970",
    "20USBML1236971",
    "20USBML1236972",
    "20USBML1236973",
    "20USBML1236974",
    "20USBML1236975",
    "20USBML1236976",
    "20USBML1236977",
    "20USBML1236978",
    "20USBML1237126",
    "20USBML1237127",
    "20USBML1237128",
    "20USBML1237129",
    "20USBML1237130",
    "20USBML1237131",
    "20USBML1237132",
    "20USBML1237133",
    "20USBML1237161",
    "20USBML1237162",
    "20USBML1237163",
    "20USBML1237164",
    "20USBML1237178",
    "20USBML1237179",
    "20USBML1237180",
    "20USBML1237181",
    "20USBML1237182",
    "20USBML1237183",
    "20USBML1237184",
    "20USBML1237185",
    "20USBML1237186",
    "20USBML1237187",
    "20USBML1237188",
    "20USBML1237189",
    "20USBML1237190",
    "20USBML1237476",
    "20USBML1237477",
    "20USBML1237478",
    "20USBML1237479",
    "20USBML1237480",
    "20USBML1237481",
    "20USBML1237482",
    "20USBML1237483",
    "20USBML1237484",
    "20USBML1237509",
    "20USBML1237510",
    "20USBML1237511",
    "20USBML1237512",
    "20USBML1237513",
    "20USBML1237514",
    "20USBML1237515",
    "20USBML1237516",
    "20USBML1237517",
    "20USBML1237518",
    "20USBML1237519",
    "20USBML1237520",
    "20USBML1237521",
    "20USBML1237522",
    "20USBML1237523",
    "20USBML1237524",
    "20USBML1237525",
    "20USBML1237526",
    "20USBML1237527",
    "20USBML1237544",
    "20USBML1237545",
    "20USBML1237546",
    "20USBML1237547",
    "20USBML1237548",
    "20USBML1237549",
    "20USBML1237550",
    "20USBML1237551",
    "20USBML1237552",
    "20USBML1237553",
    "20USBML1237554",
    "20USBML1237555",
    "20USBML1237556",
    "20USBML1237557",
    "20USBML1237558",
    "20USBML1237559",
    "20USBML1237560",
    "20USBML1237561",
    "20USBML1237562",
    "20USBML1237563",
    "20USBML1237564",
    "20USBML1237565",
    "20USBML1237566",
    "20USBML1237585",
    "20USBML1237586",
    "20USBML1237629",
    "20USBML1237630",
    "20USBML1237631",
    "20USBML1237632",
    "20USBML1237633",
    "20USBML1237634",
    "20USBML1237635",
    "20USBML1237636",
    "20USBML1237637",
    "20USBML1237638",
    "20USBML1237639",
    "20USBML1237640",
    "20USBML1237641",
    "20USBML1237642",
    "20USBML1237643",
    "20USBML1237644",
    "20USBML1237645",
    "20USBML1237646",
    "20USBML1237647",
    "20USBML1237648",
    "20USBML1237649",
    "20USBML1237650",
    "20USBML1237651",
    "20USBML1237652",
    "20USBML1237653",
    "20USBML1237657",
    "20USBML1237658",
    "20USBML1237659",
    "20USBML1237660",
    "20USBML1237661",
    "20USBML1237662",
    "20USBML1237663",
    "20USBML1237664",
    "20USBML1237665",
    "20USBML1237666",
    "20USBML1237667",
    "20USBML1237668",
    "20USBML1237669",
    "20USBML1237670",
    "20USBML1237671",
    "20USBML1237672",
    "20USBML1237673",
    "20USBML1237674",
    "20USBML1237675",
    "20USBML1237676",
    "20USBML1237677",
    "20USBML1237678",
    "20USBML1237679",
    "20USBML1237680",
    "20USBML1237681",
    "20USBML1237682",
    "20USBML1237683",
    "20USBML1237684",
    "20USBML1237685",
    "20USBML1237686",
    "20USBML1237687",
    "20USBML1237688",
    "20USBML1237689",
    "20USBML1237690",
    "20USBML1237691",
    "20USBML1237921",
    "20USBML1237922",
    "20USBML1237923",
    "20USBML1237924",
    "20USBML1237929",
    "20USBML1237930",
    "20USBML1237931",
    "20USBML1237932",
    "20USBML1237951",
    "20USBML1237952",
    "20USBML1237953",
    "20USBML1237954",
    "20USBML1237955",
    "20USBML1237956",
    "20USBML1237957",
    "20USBML1237958",
    "20USBML1237959",
    "20USBML1237960",
    "20USBML1237961",
    "20USBML1237962",
    "20USBML1237963",
    "20USBML1237964",
    "20USBML1237965",
    "20USBML1237966",
    "20USBML1237967",
    "20USBML1237968",
    "20USBML1237969",
    "20USBML1237970",
    "20USBML1237971",
    "20USBML1237972",
    "20USBML1237973",
    "20USBML1237974",
    "20USBML1237975",
    "20USBML1237976",
    "20USBML1237978",
    "20USBML1237979",
    "20USBML1237981",
    "20USBML1237982",
    "20USBML1237983",
    "20USBML1237984",
    "20USBML1237985",
    "20USBML1237986",
    "20USBML1237987",
    "20USBML1237988",
    "20USBML1237989",
    "20USBML1237990",
    "20USBML1237991",
    "20USBML1237992",
    "20USBML1237993",
    "20USBML1237994",
    "20USBML1237995",
    "20USBML1237996",
    "20USBML1237997",
    "20USBML1237998",
    "20USBML1237999",
    "20USBML1238000",
    "20USBML1238001",
    "20USBML1238002",
    "20USBML1238003",
    "20USBML1238359",
    "20USBML1238360",
    "20USBML1238361",
    "20USBML1238362",
    "20USBML1238363",
    "20USBML1238364",
    "20USBML1238365",
    "20USBML1238366",
    "20USBML1238367",
    "20USBML1238368",
    "20USBML1238369",
    "20USBML1238370",
    "20USBML1238371",
    "20USBML1238372",
    "20USBML1238373",
    "20USBML1238374",
    "20USBML1238375",
    "20USBML1238376",
    "20USBML1238377",
    "20USBML1238378",
    "20USBML1238379",
    "20USBML1238380",
    "20USBML1238381",
    "20USBML1238382",
    "20USBML1238383",
    "20USBML1238384",
    "20USBML1238385",
    "20USBML1238386",
    "20USBML1238387",
    "20USBML1238388",
    "20USBML1238389",
    "20USBML1238390",
    "20USBML1238391",
    "20USBML1238392",
    "20USBML1238393",
    "20USBML1238394",
    "20USBML1238395",
    "20USBML1238396",
    "20USBML1238397",
    "20USBML1238398",
    "20USBML1238399",
    "20USBML1238400",
    "20USBML1238401",
    "20USBML1238403",
    "20USBML1238409",
    "20USBML1238410",
    "20USBML1238411",
    "20USBML1238412",
    "20USBML1238413",
    "20USBML1238414",
    "20USBML1238415",
    "20USBML1238416",
    "20USBML1238417",
    "20USBML1238418",
    "20USBML1238419",
    "20USBML1238420",
    "20USBML1238421",
    "20USBML1238422",
    "20USBML1238423",
    "20USBML1238424",
    "20USBML1238425",
    "20USBML1238426",
    "20USBML1238427",
    "20USBML1238428",
    "20USBML1238984",
    "20USBML1238985",
    "20USBML1238986",
    "20USBML1238987",
    "20USBML1238988",
    "20USBML1238989",
    "20USBML1238990",
    "20USBML1238991",
    "20USBML1238992",
    "20USBML1238993",
    "20USBML1238994",
    "20USBML1238995",
    "20USBML1238996",
    "20USBML1238997",
    "20USBML1238998",
    "20USBML1238999",
    "20USBML1239000",
    "20USBML1239001",
    "20USBML1239002",
    "20USBML1239003",
    "20USBML1239004",
    "20USBML1239005",
    "20USBML1239006",
    "20USBML1239007",
    "20USBML1239008",
    "20USBML1239009",
    "20USBML1239010",
    "20USBML1239011",
    "20USBML1239012",
    "20USBML1239013",
    "20USBML1239014",
    "20USBML1239015",
    "20USBML1239016",
    "20USBML1239017",
    "20USBML1239018",
    "20USBML1239019",
    "20USBML1239020",
    "20USBML1239021",
    "20USBML1239022",
    "20USBML1239023",
    "20USBML1239024",
    "20USBML1239025",
    "20USBML1239026",
    "20USBML1239027",
    "20USBML1239028",
    "20USBML1239029",
    "20USBML1239030",
    "20USBML1239031",
    "20USBML1239032",
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