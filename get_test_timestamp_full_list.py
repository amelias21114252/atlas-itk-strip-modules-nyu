#!/usr/bin/env python3
#python get_test_timestamp_full_list.py --serial_number 20USBHX2002592 --test_name 'Response Curve TC'
#python get_test_timestamp_full_list.py --serial_number 20USBML1235761 --test_name 'Module AMAC IV TC'

import os
import json
import itkdb

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
    "20USBHX2002953",
    "20USBHX2002954",
    "20USBHX2002956",
    "20USBHX2002957",
    "20USBHX2002971",
    "20USBHX2002964",
    "20USBHX2002965",
    "20USBHX2002966",
    "20USBHX2002967",
    "20USBHX2002983",
    "20USBHX2002960",
    "20USBHX2002961",
    "20USBHX2002787",
    "20USBHX2002959",
    "20USBHX2002958",
    "20USBHX2002980",
    "20USBHX2002981",
    "20USBHX2002982",
    "20USBHX2002968",
    "20USBHX2002969",
    "20USBHX2002970",
    "20USBHX2003655",
    "20USBHX2002962",
    "20USBHX2002963",
    "20USBHX2002986",
    "20USBHX2003063",
    "20USBHX2003058",
    "20USBHX2003059",
    "20USBHX2003060",
    "20USBHX2003061",

    "20USBHX2003042",
    "20USBHX2003041",
    "20USBHX2003036",
    "20USBHX2003037",
    "20USBHX2003038",
    "20USBHX2003039",
    "20USBHX2003040",
    "20USBHX2003233",
    "20USBHX2003238",
    "20USBHX2003234",
    "20USBHX2003240",
    "20USBHX2003242",
    "20USBHX2003243",
    "20USBHX2003244",
    "20USBHX2003130",
    "20USBHX2003131",
    "20USBHX2003134",
    "20USBHX2003135",
    "20USBHX2003540",
    "20USBHX2003541",
    "20USBHX2003542",
    "20USBHX2003543",
    "20USBHX2003560",
    "20USBHX2003561",
    "20USBHX2003563",
    "20USBHX2003564",
    "20USBHX2003565",
    "20USBHX2003566",
    "20USBHX2003545",
    "20USBHX2003559",
    "20USBHX2003558",
    "20USBHX2003666",
    "20USBHX2003548",
    "20USBHX2003549",
    "20USBHX2003550",
    "20USBHX2003553",
    "20USBHX2003554",
    "20USBHX2003557",
    "20USBHX2003672",
    "20USBHX2003546",
    "20USBHX2003547",
    "20USBHX2003555",
    "20USBHX2003556",
    "20USBHX2003544",
    "20USBHX2003644",
    "20USBHX2003645",
    "20USBHX2003647",
    "20USBHX2003669",
    "20USBHX2003671",
    "20USBHX2003652",
    "20USBHX2003659",
    "20USBHX2003653",
    "20USBHX2003654",
    "20USBHX2003658",
    "20USBHX2003657",
    "20USBHX2003865",
    "20USBHX2003866",
    "20USBHX2003867",
    "20USBHX2003868",
    "20USBHX2003869",
    "20USBHX2003870",
    "20USBHX2004025",
    "20USBHX2003871",
    "20USBHX2003872",
    "20USBHX2003875",
    "20USBHX2003873",
    "20USBHX2003668",
    "20USBHX2003667",
    "20USBHX2003660",
    "20USBHX2003661",
    "20USBHX2003662",
    "20USBHX2003663",
    "20USBHX2003646",
    "20USBHX2003649",
    "20USBHX2003664",
    "20USBHX2003665",
    "20USBHX2003860",
    "20USBHX2003861",
    "20USBHX2003862",
    "20USBHX2003863",
    "20USBHX2003859",
    "20USBHX2003856",
    "20USBHX2003857",
    "20USBHX2003858",
    "20USBHX2003990",
    "20USBHX2003991",
    "20USBHX2003992",
    "20USBHX2003993",
    "20USBHX2003996",
    "20USBHX2004004",
    "20USBHX2004005",
    "20USBHX2003994",
    "20USBHX2004006",
    "20USBHX2004007",
    "20USBHX2004008",
    "20USBHX2004009",
    "20USBHX2003995",
    "20USBHX2004037",
    "20USBHX2004036",
    "20USBHX2004018",
    "20USBHX2004019",
    "20USBHX2004020",
    "20USBHX2004021",
    "20USBHX2004026",
    "20USBHX2004027",
    "20USBHX2004028",
    "20USBHX2004029",
    "20USBHX2004159",
    "20USBHX2004160",
    "20USBHX2004161",
    "20USBHX2004162",
    "20USBHX2004163",
    "20USBHX2004164",
    "20USBHX2004165",
    "20USBHX2004166",
    "20USBHX2004167",
    "20USBHX2004168",
    "20USBHX2004169",
    "20USBHX2004170",
    "20USBHX2004171",
    "20USBHX2004172",
    "20USBHX2004173",
    "20USBHX2004174",
    "20USBHX2003904",
    "20USBHX2004022",
    "20USBHX2004023",
    "20USBHX2004024",
    "20USBHX2003905",
    "20USBHX2003906",
    "20USBHX2003907",
    "20USBHX2003908",
    "20USBHX2003235",
    "20USBHX2003236",
    "20USBHX2003237",
    "20USBHX2003239",
    "20USBHX2003132",
    "20USBHX2003133",
    "20USBHX2003241",
    "20USBHX2003245",
    "20USBHX2003909",
    "20USBHX2002955",
    "20USBHX2003670",
    "20USBHX2003648",
    "20USBHX2003864",
    "20USBHX2002573",
    "20USBHX2004175",
    "20USBHX2004501",
    "20USBHX2004502",
    "20USBHX2004503",
    "20USBHX2004504",
    "20USBHX2004505",
    "20USBHX2004506",
    "20USBHX2004493",
    "20USBHX2004494",
    "20USBHX2004507",
    "20USBHX2004508",
    "20USBHX2004509",
    "20USBHX2004510",
    "20USBHX2004489",
    "20USBHX2004490",
    "20USBHX2004491",
    "20USBHX2004492",
    "20USBHX2004513",
    "20USBHX2004514",
    "20USBHX2004515",
    "20USBHX2004516",
    "20USBHX2004481",
    "20USBHX2004511",
    "20USBHX2004512",
    "20USBHX2004517",
    "20USBHX2004519",
    "20USBHX2004520",
    "20USBHX2004523",
    "20USBHX2004522",
    "20USBHX2004518",
    "20USBHX2004524",
    "20USBHX2004858",
    "20USBHX2004859",
    "20USBHX2004860",
    "20USBHX2004861",
    "20USBHX2004852",
    "20USBHX2004853",
    "20USBHX2004854",
    "20USBHX2004855",
    "20USBHX2004856",
    "20USBHX2004857",
    "20USBHX2004862",
    "20USBHX2004863",
    "20USBHX2004483",
    "20USBHX2004484",
    "20USBHX2004485",
    "20USBHX2004867",
    "20USBHX2004480",
    "20USBHX2004482",
    "20USBHX2004487",
    "20USBHX2004870",
    "20USBHX2004486",
    "20USBHX2004864",
    "20USBHX2004865",
    "20USBHX2004866",
    "20USBHX2004868",
    "20USBHX2004869",
    "20USBHX2004825",
    "20USBHX2004826",
    "20USBHX2004827",
    "20USBHX2004828",
    "20USBHX2004829",
    "20USBHX2005137",
    "20USBHX2005145",
    "20USBHX2005146",
    "20USBHX2005147",
    "20USBHX2005148",
    "20USBHX2005184",
    "20USBHX2005185",
    "20USBHX2005186",
    "20USBHX2005187",
]

test_name = "Response Curve TC"
output_file = "timestamps_list.json"


def format_timestamp(ts):
    """
    Convert:
    2025-05-29T18:47:56.395Z
    ->
    2025-05-29 18:47:56.395
    """
    if not ts:
        return None
    try:
        dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    except Exception:
        return ts.replace("T", " ").replace("Z", "")


def add_sn_prefix(s):
    if s is None:
        return None
    return s if s.startswith("SN") else f"SN{s}"


def get_entry(client, serial_number):
    try:
        component = client.get("getComponent", json={"component": serial_number})

        test_ids = [
            y["id"]
            for x in component.get("tests", [])
            for y in x.get("testRuns", [])
            if x.get("name") == test_name
        ]

        if not test_ids:
            return (None, add_sn_prefix(serial_number), None)

        testRun = client.get("getTestRun", json={"testRun": test_ids[0]})

        raw_ts = None
        if testRun.get("components") and len(testRun["components"]) > 0:
            raw_ts = testRun["components"][0].get("stateTs")

        timestamp = format_timestamp(raw_ts)

        parent_name = None
        child_name = None

        # Hybrid serials: return (parent ML, hybrid HX, timestamp)
        if "HX" in serial_number or "HY" in serial_number:
            try:
                parent_name = testRun["components"][0]["ancestorMap"]["parent"]["component"]["serialNumber"]
                parent_name = add_sn_prefix(parent_name)
                print(f"Module (parent) serial number: {parent_name}")
            except Exception:
                parent_name = None

            return (parent_name, add_sn_prefix(serial_number), timestamp)

        # Module serials: return (module ML/MS, child hybrid, timestamp)
        if "ML" in serial_number or "MS" in serial_number:
            try:
                child_name = testRun["properties"][1]["value"]["name"]
                child_name = add_sn_prefix(child_name)
                print(f"Hybrid (child) serial number: {child_name}")
            except Exception:
                child_name = None

            return (add_sn_prefix(serial_number), child_name, timestamp)

        return (add_sn_prefix(serial_number), None, timestamp)

    except Exception as e:
        print(f"Error for {serial_number}: {e}")
        return (None, add_sn_prefix(serial_number), None)


def main():
    token = os.getenv("ITK_DB_AUTH")
    if not token:
        raise RuntimeError("ITK_DB_AUTH not set")

    user = itkdb.core.UserBearer(bearer=token)
    client = itkdb.Client(user=user)

    results = []

    for i, serial in enumerate(serial_numbers, start=1):
        print(f"[{i}/{len(serial_numbers)}] {serial}")
        entry = get_entry(client, serial)
        results.append(entry)
        print(entry)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print("\nFormatted output:\n")
    for entry in results:
        if entry[0] is not None and entry[1] is not None and entry[2] is not None:
            print(f'("{entry[0]}", "{entry[1]}", "{entry[2]}"),')

    print(f"\n✅ Saved to {output_file}")


if __name__ == "__main__":
    main()