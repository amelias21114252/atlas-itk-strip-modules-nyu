# CERN-ATLAS SCTVAR Plotting Workflow

This guide explains how to run the scripts in `CERN-ATLAS-` for:

- IV plots
- Input noise plots
- Combined histogram plots
- Detailed per-file histogram plots
- Webpage upload workflow

It also includes example commands for both:

- **X-Hybrid Mounted Numbers** (for input noise and histogram plots)
- **DB Serial Numbers** (for IV plots)

---

# 1. Go to the results directory

In Visual Studio Code terminal, first move into the directory where the scripts and input files are stored:

```bash
cd /Users/ameliastevens/Documents/GitHub/CERN-ATLAS-ITk-Strip-Modules-NYU-Contributions/production_database_scripts-master/
```

This changes the current working directory to the folder containing the plotting scripts and the JSON input files.

---

# 2. Plot IV data from existing JSON files

To run the IV plotting script on a specific module:

```bash
python plot_multi_IV.py -i 'iv/*SN20USBML1235331*.json'
```

This command:

- runs the IV plotting script on module `SN20USBML1235331`
- looks in the `iv/` subfolder for any JSON file containing that module name
- generates **Current vs Voltage** plots for leakage current

---

# 3. Plot input noise data from existing JSON files

To run the input noise plotting script on a specific X-hybrid:

```bash
python plot_multi_inputnoise.py -i 'inputnoise/*SN20USBHX2001865*.json'
```

This command:

- runs the input noise plotting script for `SN20USBHX2001865`
- looks in the `inputnoise/` directory for matching JSON files
- generates input noise plots per detector channel

---

# 4. ITK Production Database workflow for X-Hybrid Mounted Numbers

These steps are used for **input noise** and **histogram** plots.

Before running any database query script, authenticate using your ITK database token.

Ensure you follow the instructions here to authenticate:

```bash
export ITK_DB_AUTH=TOKEN
```

You can find your database authentication token here:

'https://uuidentity.plus4u.net/uu-identitymanagement-maing01/a9b105aff2744771be4daa8361954677/showToken`

The token expires roughly every 15 minutes, so you may need to refresh it often.

---

## 4.1 Download Response Curve TC data by X-Hybrid Mounted Number

Use `get_test_run2.py` with the X-Hybrid Mounted Number, for example:

```bash
python get_test_run2.py --serial_number 20USBHX2002657 --test_name 'Response Curve TC'
```

This script automatically:

- queries the ITK production database
- creates a folder named after the X-Hybrid Mounted Number
- saves **25 separate JSON files** inside that folder

These JSON files are then used for the input noise and histogram plotting scripts.

---

## 4.2 Plot combined histograms without skipping values

To plot the combined **away** and **under** histograms without skipping values:

```bash
python plot_combined_inputnoise_noskip.py --serial_number 20USBHX2002657
```

This script automatically:

- creates a folder called `histograms_combined_noskip`
- saves plots in both **PDF** and **PNG** format
- generates a JSON file that prints values:
  - below `600`
  - above `1000`

Use this version when you want to inspect all values without filtering.

---

## 4.3 Plot combined histograms with standard filtering

To plot the combined **away** and **under** histograms with filtering:

```bash
python plot_combined_inputnoise.py --serial_number 20USBHX2002657
```

This script automatically:

- creates a folder called `histograms_combined`
- saves plots in both **PDF** and **PNG** format
- skips:
  - values greater than `1000`
  - values with standard deviation greater than `300`

Use this version for standard cleaned histogram plots.

---

## 4.4 Plot detailed per-file histograms

To plot away and under histograms for each of the 25 tests individually:

```bash
python plot_detailed_inputnoise_histograms_per_file.py --serial_number 20USBHX2002657
```

This script automatically:

- creates a folder called `detailedhistograms`
- saves output plots in **PDF** format
- generates:
  - one combined away histogram per test
  - one combined under histogram per test
  - per-channel plots for each test

Example output filenames include:

- `SN20USBHX2002971_01_combined_innse_away`
- `SN20USBHX2002971_01_combined_innse_under`

---

## 4.5 Plot input noise after thermal cycling without skipping values

To plot the input noise after thermal cycling without skipping any values:

```bash
python plot_multi_inputnoise_noskip.py --serial_number 20USBHX2002657
```

Use this version when you want to preserve the full dataset with no cuts applied.

---

## 4.6 Plot input noise after thermal cycling with standard filtering

To plot the input noise after thermal cycling with filtering:

```bash
python plot_multi_inputnoise.py --serial_number 20USBHX2002657
```

Use this version for the standard filtered input noise plots.

---

# 5. ITK Production Database workflow for DB Serial Numbers

These steps are used for **IV plots**.

Before running the query, authenticate using your ITK database token:

```bash
export ITK_DB_AUTH=TOKEN
```

---

## 5.1 Download Module AMAC IV TC data by DB Serial Number

Use `get_test_run3.py` with the DB Serial Number, for example:

```bash
python get_test_run3.py --serial_number 20USBML1235874 --test_name 'Module AMAC IV TC'
```

This script automatically:

- queries the ITK production database
- creates a folder named after the DB Serial Number
- saves **25 separate JSON files** inside that folder

---

## 5.2 Plot IV data for a DB Serial Number

To plot IV data for the corresponding DB Serial Number:

```bash
python plot_multi_IV.py -i 'SN20USBML1235761/*.json'
```

This command reads the JSON files in that DB Serial Number folder and generates the IV plots.

---

# 6. Example database commands in the same style

Below is a cleaned example in the same style as your preferred README formatting.

Ensure you follow the instructions here to authenticate:

```bash
export ITK_DB_AUTH=TOKEN
```

You can find your database authentication token here:

`https://uuidentity.plus4u.net/uu-identitymanagement-maing01/a9b105aff2744771be4daa8361954677/showToken`

Annoyingly, the token expires roughly every 15 minutes, so be patient, as you may have to do this often.

Once done, list the component information by serial number:

```bash
python get_test_run2.py --serial_number 20USBHX2002657 --test_name 'Response Curve TC'
```

The script then proceeds to extract interesting test information, for example:

- Input noise under and away streams (`innse_under`, `innse_away`)
- AMAC negative-temperature coefficient temperatures (`AMAC_NTCpb`, `AMAC_NTCx`)

---

# 7. Current-voltage

Module AMAC IV scan data can be queried using the module serial number and the test name:

```bash
python get_test_run3.py --serial_number 20USBML1235761 --test_name 'Module AMAC IV TC'  # During module thermocycling
```

This also prints out the timestamp and child hybrid serial number at the end of the terminal output.

If you wish to study the IV performed on a tabbed sensor *before* gluing circuit boards, pass a different test name:

```bash
python get_test_run3.py --serial_number 20USBML1235761 --test_name 'Module IV with PS V1'  # Before gluing tabbed sensor
```

---

# 8. Webpage instructions

To create the webpage, follow the CERN Web EOS site creation tutorials:

`https://webeos.docs.cern.ch/create_site/`

The webpage is linked here:

`https://ameliame.web.cern.ch/`

---

## 8.1 Generate the HTML page

Run the page-generation script:

```bash
python generate_channel_page_final.py
```

This creates `index.html`.

Then:

- upload `index.html` to your CERNBox

All plot folders should also be uploaded to CERNBox, for example:

- `SN20USBML1235874`
- `SN20USBHX2002657`

---

## 8.2 Upload `index.html` to CERNBox

Upload `index.html` to the following path:

`https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www`

Each time you edit `index.html`, re-upload the updated version to CERNBox.

---

## 8.3 Upload plot folders to CERNBox

Upload each DB Serial Number folder and X-Hybrid Mounted Number folder to:

`https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www/atlas-plots/`

This is where the webpage reads the plot content from.

---


# 9. Suggested next steps

- Insert timestamps on the webpage for each serial number
- Add the California and UK modules (SCIPPY and LBNL) and find child/parent modules from the ITK database
- Insert comments for each module and classify red light or green light
- Reach out to Matt and Stefania at BNL

---

# 10. Notes

A few useful naming conventions used in this workflow:

- **X-Hybrid Mounted Number**: used for input noise and histogram workflows
- **DB Serial Number**: used for IV workflows
- **Response Curve TC**: used for input noise related database extraction
- **Module AMAC IV TC**: used for thermal cycling IV data
- **Module IV with PS V1**: used for pre-gluing IV data

---

# 11. Quick command summary

## Input noise workflow

```bash
python get_test_run2.py --serial_number 20USBHX2002657 --test_name 'Response Curve TC'
python plot_combined_inputnoise_noskip.py --serial_number 20USBHX2002657
python plot_combined_inputnoise.py --serial_number 20USBHX2002657
python plot_detailed_inputnoise_histograms_per_file.py --serial_number 20USBHX2002657
python plot_multi_inputnoise_noskip.py --serial_number 20USBHX2002657
python plot_multi_inputnoise.py --serial_number 20USBHX2002657
```

## IV workflow

```bash
python get_test_run3.py --serial_number 20USBML1235874 --test_name 'Module AMAC IV TC'
python plot_multi_IV.py -i 'SN20USBML1235874/*.json'
```

## Existing JSON file plotting

```bash
python plot_multi_IV.py -i 'iv/*SN20USBML1235331*.json'
python plot_multi_inputnoise.py -i 'inputnoise/*SN20USBHX2001865*.json'
```
