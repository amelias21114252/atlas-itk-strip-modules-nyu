import subprocess

from pathlib import Path

import shutil

serial_numbers = [
    "20USBHX2001619",
    "20USBHX2001626",
    "20USBHX2001632",
    "20USBHX2001629",
    "20USBHX2001624",
    "20USBHX2001625",
    "20USBHX2001627",
    "20USBHX2001631",
    "20USBHX2001623",
    "20USBHX2001635",
    "20USBHX2001636",
    "20USBHX2001630",
    "20USBHX2002099",
    "20USBHX2002020",
    "20USBHX2002301",
    "20USBHX2002303",
    "20USBHX2002302",
    "20USBHX2002494",
    "20USBHX2002495",
    "20USBHX2002499",
    "20USBHX2002496",
    "20USBHX2002497",
    "20USBHX2002498",
    "20USBHX2002571",
    "20USBHX2002572",
    "20USBHX2002587",
    "20USBHX2002588",
    "20USBHX2002590",
    "20USBHX2002575",
    "20USBHX2002597",
    "20USBHX2002598",
    "20USBHX2002591",
    "20USBHX2002592",
    "20USBHX2002593",
    "20USBHX2002594",
    "20USBHX2002627",
    "20USBHX2002628",
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
    "20USBHX2004036",
    "20USBHX2004037",
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
    "20USBHX2005148",
    "20USBHX2005147",
    "20USBHX2005184",
    "20USBHX2005185",
    "20USBHX2005186",
    "20USBHX2005187",
    "20USBHX2005149",
    "20USBHX2005188",
    "20USBHX2005189",
    "20USBHX2005190",
    "20USBHX2005138",
    "20USBHX2005139",
    "20USBHX2005140",
    "20USBHX2005141",
    "20USBHX2005161",
    "20USBHX2005162",
    "20USBHX2005163",
    "20USBHX2005164",
    "20USBHX2005132",
    "20USBHX2005133",
    "20USBHX2005134",
    "20USBHX2005135",
    "20USBHX2005142",
    "20USBHX2005143",
    "20USBHX2005144",
    "20USBHX2005136",
    "20USBHX2005125",
    "20USBHX2005126",
    "20USBHX2005127",
    "20USBHX2005128",
    "20USBHX2005129",
    "20USBHX2005130",
    "20USBHX2005131",
    "20USBHX2005150",
    "20USBHX2005158",
    "20USBHX2005159",
    "20USBHX2005160",
    "20USBHX2005151",
    "20USBHX2005177",
    "20USBHX2005178",
    "20USBHX2005179",
    "20USBHX2005180",
    "20USBHX2005181",
    "20USBHX2005182",
    "20USBHX2005183",
    "20USBHX2004488",
    "20USBHX2005191",
    "20USBHX2005192",
    "20USBHX2005193",
    "20USBHX2005194",
    "20USBHX2005206",
    "20USBHX2005207",
    "20USBHX2005208",
    "20USBHX2005209",
    "20USBHX2005212",
    "20USBHX2005213",
    "20USBHX2005214",
    "20USBHX2005215",
    "20USBHX2005201",
    "20USBHX2005202",
    "20USBHX2005203",
    "20USBHX2005204",
    "20USBHX2005197",
    "20USBHX2005198",
    "20USBHX2005199",
    "20USBHX2005200",
    "20USBHX2005195",
    "20USBHX2005196",
    "20USBHX2005210",
    "20USBHX2005211",
    "20USBHX2005216",
    "20USBHX2005217",
    "20USBHX2005218",
    "20USBHX2005406",
    "20USBHX2005411",
    "20USBHX2005412",
    "20USBHX2005413",
    "20USBHX2005444",
    "20USBHX2005445",
    "20USBHX2005446",
    "20USBHX2005447",
    "20USBHX2005448",
    "20USBHX2005476",
    "20USBHX2005477",
    "20USBHX2005478",
    "20USBHX2005475",
    "20USBHX2005473",
    "20USBHX2005474",
    "20USBHX2005449",
    "20USBHX2005458",
]



def write_python_list(f, title, values):

    f.write(f"{title} = [\n")

    for serial in values:

        f.write(f'    "{serial}",\n')

    f.write("]\n\n")

passed = []

category_e_ii_failed = []

# ============================================================

# Output directories

# ============================================================

base_output_dir = Path("BNL")

hx_output_dir = base_output_dir / "HX"

hx_output_dir.mkdir(parents=True, exist_ok=True)

script_path = Path("get_test_run2.py").resolve()

# ============================================================

# Run modules

# ============================================================

for i, serial in enumerate(serial_numbers, start=1):

    print("=" * 80)

    print(f"[{i}/{len(serial_numbers)}] Running for {serial}")

    sn_serial = serial if serial.startswith("SN") else f"SN{serial}"

    final_module_dir = hx_output_dir / sn_serial

    temp_dir = hx_output_dir / f"temp_{sn_serial}"

    if temp_dir.exists():

        shutil.rmtree(temp_dir)

    temp_dir.mkdir(parents=True, exist_ok=True)

    try:

        result = subprocess.run(

            [

                "python",

                str(script_path),

                "--serial_number",

                serial,

                "--test_name",

                "Response Curve TC",

            ],

            check=True,

            capture_output=True,

            text=True,

            cwd=temp_dir,

        )

        nested_dir = temp_dir / sn_serial

        files_to_move = []

        if nested_dir.exists() and nested_dir.is_dir():

            files_to_move = list(nested_dir.iterdir())

        else:

            files_to_move = list(temp_dir.iterdir())

        files_to_move = [

            item for item in files_to_move

            if item.is_file() and item.suffix == ".json"

        ]

        if files_to_move:

            final_module_dir.mkdir(parents=True, exist_ok=True)

            for item in files_to_move:

                target = final_module_dir / item.name

                if target.exists():

                    target.unlink()

                item.rename(target)

            passed.append(serial)

            print(f"✅ PASSED: {serial}")

        else:

            category_e_ii_failed.append(serial)

            print(

                f"❌ CATEGORY E(ii) FAILURE: {serial} — no JSON files were created"

            )

        print(result.stdout)

        if result.stderr:

            print(result.stderr)

    except subprocess.CalledProcessError as e:

        print(e.stdout)

        print(e.stderr)

        category_e_ii_failed.append(serial)

        print(

            f"❌ CATEGORY E(ii) FAILURE: {serial} — input noise data could not be found or processed"

        )

    finally:

        if temp_dir.exists():

            shutil.rmtree(temp_dir)

# ============================================================

# Summary page

# ============================================================

summary_path = hx_output_dir / "summary_page_bnl_HX.txt"

with open(summary_path, "w") as f:

    f.write("=" * 80 + "\n")

    f.write("BNL HX CATEGORY E(ii) FINAL SUMMARY\n")

    f.write("=" * 80 + "\n\n")

    f.write(f"TOTAL MODULES CHECKED: {len(serial_numbers)}\n")

    f.write(f"WORKING MODULES: {len(passed)}\n")

    f.write(f"FAILED MODULES: {len(category_e_ii_failed)}\n\n")

    write_python_list(f, "working_modules", passed)

    write_python_list(f, "failed_modules", category_e_ii_failed)

print(f"\n📄 Summary saved to: {summary_path}")

print(f"📁 HX modules saved inside: {hx_output_dir}")