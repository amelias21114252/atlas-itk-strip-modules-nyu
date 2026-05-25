# CERN-ATLAS ITk Module Category Plotting Workflow

This guide explains how to run the scripts for the BNL, LBNL, and UCSC module-processing workflow.

The workflow includes:

- Generating serial-number lists
- Downloading test data into JSON files
- Generating IV plots
- Generating input-noise plots
- Generating combined histogram plots
- Generating detailed per-file histogram plots
- Identifying Category A, B, C, D, and E errors
- Generating timestamp lists
- Creating the final category webpage
- Uploading the webpage and folders to CERNBox

It also includes example commands for both:

- **HX Serial Numbers** for input-noise plots, combined histograms, no-skip histograms, and detailed histograms
- **ML Serial Numbers** for IV plots

---

# 1. Run `get_module_serial_numbers`

First, run the script that gets the module serial-number information.

Make sure to use the authentication token when running this command.

```bash
python get_module_serial_numbers.py
```

This script gives the raw text that connects HX serial numbers with their corresponding ML parent serial numbers.

Copy and paste the raw text from `get_module_serial_numbers.py` into each corresponding serial-number generator script.

The raw text is used to generate serial-number lists for BNL, LBNL, and UCSC.

---

# 2. Authenticate before running database scripts

Before running any database query script, authenticate using your ITK database token.

Use:

```bash
export ITK_DB_AUTH=TOKEN
```

You can find your database authentication token here:

```text
https://uuidentity.plus4u.net/uu-identitymanagement-maing01/a9b105aff2744771be4daa8361954677/showToken
```

The token expires roughly every 15 minutes, so you may need to refresh it often.

Authentication is required to convert test data into separate JSON files.

If authentication is missing or expired, the JSON-generation scripts may fail.

When the scripts fail or the data cannot be processed, modules may appear in Category E.

---

# 3. Generate HX serial-number lists for input noise

Copy and paste the raw text from `get_module_serial_numbers.py` into the corresponding input-noise serial-number generator scripts.

Then run:

```bash
python serialnumbergenerate_inputnoise_bnl.py
python serialnumbergenerate_inputnoise_lbnl.py
python serialnumbergenerate_inputnoise_ucsc.py
```

These scripts generate HX serial-number lists.

The HX serial-number lists are used for:

- Input-noise JSON generation
- Input-noise plots
- Combined input-noise histograms
- Combined no-skip histograms
- Detailed per-file histograms
- Category B, C, D(ii), and E(ii) classification

---

# 4. Generate ML serial-number lists for IV data

Copy and paste the raw text from `get_module_serial_numbers.py` into the corresponding IV serial-number generator scripts.

Then run:

```bash
python serialnumbergenerate_IV_bnl.py
python serialnumbergenerate_IV_lbnl.py
python serialnumbergenerate_IV_ucsc.py
```

These scripts generate ML serial-number lists.

The ML serial-number lists are used for:

- IV JSON generation
- IV plots
- Category A, D(i), and E(i) classification

---

# 5. Copy and paste serial numbers before running tests

After generating the HX and ML serial-number lists, copy and paste the serial numbers into the corresponding test scripts.

HX serial numbers should only be used for HX/input-noise sections.

ML serial numbers should only be used for ML/IV sections.

Use HX serial numbers for:

```text
Response Curve TC
```

Use ML serial numbers for:

```text
Module AMAC IV TC
```

---

# 6. Generate ML IV JSON files

These scripts generate JSON files for ML serial numbers.

Each ML module should generate 24 JSON files when the full IV dataset is available.

These scripts also print summary files that show Category E(i) errors.

Run:

```bash
python get_all_tests_categoryE_i_bnl.py
python get_all_tests_categoryE_i_lbnl.py
python get_all_tests_categoryE_i_ucsc.py
```

The BNL script generates:

```text
summary_page_bnl_ml.txt
```

The LBNL script generates:

```text
summary_page_lbnl_ml.txt
```

The UCSC script generates:

```text
summary_page_ucsc_ml.txt
```

These summary files only show Category E(i) errors.

Category E(i) means the IV data is unavailable or could not be processed.

---

# 7. Generate HX input-noise JSON files

These scripts generate JSON files for HX serial numbers.

Each HX module should generate 25 JSON files when the full input-noise dataset is available.

These scripts also print summary files that show Category D(ii) and Category E(ii) errors.

Run:

```bash
python get_all_tests_categoryDandE_ii_bnl.py --test_name "Module AMAC IV TC"
python get_all_tests_categoryDandE_ii_lbnl.py --test_name "Module AMAC IV TC"
python get_all_tests_categoryDandE_ii_ucsc.py --test_name "Module AMAC IV TC"
```

The BNL script generates:

```text
summary_page_bnl_HX.txt
```

The LBNL script generates:

```text
summary_page_lbnl_HX.txt
```

The UCSC script generates:

```text
summary_page_ucsc_HX.txt
```

These summary files show Category D(ii) and Category E(ii) errors.

Category D(ii) means the input-noise dataset is incomplete.

Category E(ii) means the input-noise data is unavailable or could not be processed.

---

# 8. Expected folder structure after JSON generation

The JSON-generation scripts should create folders for BNL, LBNL, and UCSC.

Inside each site folder, there should be HX and ML folders.

Inside the HX and ML folders, there should be serial-number folders.

Inside each serial-number folder, there should be JSON files.

The expected folder structure is:

```text
BNL/
  HX/
    SN20USBHX...
      *.json
  ML/
    SN20USBML...
      *.json

LBNL/
  HX/
    SN20USBHX...
      *.json
  ML/
    SN20USBML...
      *.json

UCSC/
  HX/
    SN20USBHX...
      *.json
  ML/
    SN20USBML...
      *.json
```

The HX folders contain input-noise JSON files.

The ML folders contain IV JSON files.

---

# 9. Generate JSON files for an individual HX module

For an individual HX module, use:

```bash
python get_test_run.py --serial_number 20USBHX2004501 --test_name "Response Curve TC"
```

You can also use:

```bash
python get_test_run2.py --serial_number 20USBHX2004826 --test_name "Response Curve TC"
```

The script `get_test_run2.py` separates HX module data into 25 JSON files.

Use this when you want to download or debug one HX module instead of processing the full site list.

---

# 10. Generate JSON files for an individual ML module

For an individual ML module, use:

```bash
python get_test_run.py --serial_number 20USBML1235274 --test_name "Module AMAC IV TC"
```

You can also use:

```bash
python get_test_run3.py --serial_number 20USBML1235274 --test_name "Module AMAC IV TC"
```

The script `get_test_run3.py` separates ML module data into 24 JSON files.

Use this when you want to download or debug one ML module instead of processing the full site list.

---

# 11. Generate IV plots for ML modules

Run the IV plotting scripts after the ML JSON files have been generated.

These scripts generate IV plots and identify Category A, Category D(i), and Category E(i) errors.

The plots should be generated inside the ML folder, inside each serial-number folder.

The plots should be saved as PDF and PNG files.

The IV script also generates:

```text
iv_error_summary.txt
```

Run:

```bash
python plot_multi_IV_final_BNL.py -i "BNL/ML/*/*.json"
python plot_multi_IV_final_BNL.py -i "LBNL/ML/*/*.json"
python plot_multi_IV_final_BNL.py -i "UCSC/ML/*/*.json"
```

This command:

- Runs the IV plotting script on ML module JSON files
- Generates Current vs Voltage plots
- Saves the plots as PDF and PNG files
- Creates the IV error summary
- Finds Category A, D(i), and E(i) errors

Category A means one or more IV current values are above the 300 nA threshold.

Category D(i) means the IV dataset is incomplete.

Category E(i) means the IV data is unavailable or could not be processed.

Most of the flagged IV problems usually come from Category A, where IV current values are above the 300 nA threshold.

Some modules are placed in Category D(i) because they have incomplete or missing IV data files.

Modules are placed in Category E(i) when the script does not run correctly, the data is unavailable, or the data cannot be processed.

---

# 12. Generate IV plots for an individual ML module

For an individual IV run, use:

```bash
python plot_multi_IV.py -i "SN20USBML1235852/*.json"
```

This command reads the JSON files in the ML serial-number folder and generates IV plots for that module.

Use this when checking or debugging one ML serial number.

---

# 13. Generate BNL input-noise plots

Run the BNL input-noise plotting scripts after the HX JSON files have been generated.

To generate standard BNL input-noise plots, run:

```bash
python plot_multi_inputnoise_BNL.py -i "BNL/HX/SN*/*.json"
```

This generates:

```text
inputnoise_error_summary.txt
```

This summary only shows Category B errors.

To generate BNL no-skip input-noise plots, run:

```bash
python plot_multi_inputnoise_noskip_BNL.py -i "BNL/HX/SN*/*.json"
```

This generates:

```text
inputnoise_noskip_error_summary.txt
```

This summary only shows Category B errors.

To generate BNL combined input-noise histograms, run:

```bash
python plot_combined_inputnoise_BNL.py -i "BNL/HX/SN*/*.json"
```

This generates:

```text
histograms_combined_error_summary.txt
```

This is one of the most useful summaries for Category B and Category C errors.

To generate BNL combined no-skip input-noise histograms, run:

```bash
python plot_combined_inputnoise_noskip_BNL.py -i "BNL/HX/SN*/*.json"
```

This generates:

```text
histograms_combined_noskip_error_summary.txt
```

This is also one of the most useful summaries for Category B and Category C errors.

To generate BNL detailed per-file input-noise histograms, run:

```bash
python plot_detailed_inputnoise_histograms_per_file_BNL.py -i "BNL/HX/SN*/*.json"
```

This generates:

```text
detailedhistograms_error_summary.txt
```

This summary shows Category B and Category C errors.

---

# 14. Generate LBNL input-noise plots

Run the LBNL input-noise plotting scripts after the HX JSON files have been generated.

To generate standard LBNL input-noise plots, run:

```bash
python plot_multi_inputnoise_LBNL.py -i "LBNL/HX/SN*/*.json"
```

To generate LBNL no-skip input-noise plots, run:

```bash
python plot_multi_inputnoise_noskip_LBNL.py -i "LBNL/HX/SN*/*.json"
```

To generate LBNL combined input-noise histograms, run:

```bash
python plot_combined_inputnoise_LBNL.py -i "LBNL/HX/SN*/*.json"
```

To generate LBNL combined no-skip input-noise histograms, run:

```bash
python plot_combined_inputnoise_noskip_LBNL.py -i "LBNL/HX/SN*/*.json"
```

To generate LBNL detailed per-file input-noise histograms, run:

```bash
python plot_detailed_inputnoise_histograms_per_file_LBNL.py -i "LBNL/HX/SN*/*.json"
```

These scripts generate LBNL input-noise plots, no-skip plots, combined histograms, combined no-skip histograms, detailed histograms, and error summaries.

---

# 15. Generate UCSC input-noise plots

Run the UCSC input-noise plotting scripts after the HX JSON files have been generated.

To generate standard UCSC input-noise plots, run:

```bash
python plot_multi_inputnoise_UCSC.py -i "UCSC/HX/SN*/*.json"
```

To generate UCSC no-skip input-noise plots, run:

```bash
python plot_multi_inputnoise_noskip_UCSC.py -i "UCSC/HX/SN*/*.json"
```

To generate UCSC combined input-noise histograms, run:

```bash
python plot_combined_inputnoise_UCSC.py -i "UCSC/HX/SN*/*.json"
```

To generate UCSC combined no-skip input-noise histograms, run:

```bash
python plot_combined_inputnoise_noskip_UCSC.py -i "UCSC/HX/SN*/*.json"
```

To generate UCSC detailed per-file input-noise histograms, run:

```bash
python plot_detailed_inputnoise_histograms_per_file_UCSC.py -i "UCSC/HX/SN*/*.json"
```

These scripts generate UCSC input-noise plots, no-skip plots, combined histograms, combined no-skip histograms, detailed histograms, and error summaries.

---

# 16. Generate HX plots for an individual module

For individual HX plotting runs, use the commands below.

To generate standard input-noise plots for one HX module, run:

```bash
python plot_multi_inputnoise.py --serial_number 20USBHX2002657
```

To generate no-skip input-noise plots for one HX module, run:

```bash
python plot_multi_inputnoise_noskip.py --serial_number 20USBHX2002657
```

To generate combined input-noise histograms for one HX module, run:

```bash
python plot_combined_inputnoise.py --serial_number 20USBHX2002657
```

To generate combined no-skip input-noise histograms for one HX module, run:

```bash
python plot_combined_inputnoise_noskip.py --serial_number 20USBHX2002657
```

To generate detailed per-file input-noise histograms for one HX module, run:

```bash
python plot_detailed_inputnoise_histograms_per_file.py --serial_number 20USBHX2002657
```

Use these commands when debugging one HX module or checking the plots for a specific serial number.

---

# 17. Input-noise plot outputs

The input-noise scripts generate plots and summaries inside the HX serial-number folders.

The generated outputs may include:

- Input-noise plots
- Input-noise no-skip plots
- Combined histograms
- Combined no-skip histograms
- Detailed per-file histograms
- Low/high value JSON files
- Error summary text files

The combined histogram scripts are the most useful for finding Category B and Category C errors.

The no-skip combined histogram script is especially useful because it includes all values and also generates JSON files showing low and high input-noise values.

Example low/high value JSON paths:

```text
BNL/HX/SN20USBHX2002592/histograms_combined_noskip/SN20USBHX2002592_away_low_high_values.json
BNL/HX/SN20USBHX2002592/histograms_combined_noskip/SN20USBHX2002592_under_low_high_values.json
```

---

# 18. Input-noise error categories

The HX plotting scripts are used to find Category B, Category C, Category D(ii), and Category E(ii) errors.

Category B means the input-noise mean is above 1100.

Category C means the input-noise values are below the low-noise threshold.

Category D(ii) means the input-noise dataset is incomplete.

Category E(ii) means the input-noise data is unavailable or could not be processed.

The combined input-noise histogram scripts are the most useful for identifying Category B and Category C errors.

---

# 19. Generate timestamp lists

Copy and paste the serial-number list from:

```text
serialnumbergenerate_inputnoise_bnl.py
```

Also copy and paste the raw `ml_hx_text` from:

```text
get_module_serial_numbers.py
```

Then run:

```bash
python get_test_timestamp_full_list_BNL.py
python get_test_timestamp_full_list_LBNL.py
python get_test_timestamp_full_list_UCSC.py
```

The BNL script generates:

```text
formatted_timestamps_bnl.txt
```

The LBNL script generates:

```text
formatted_timestamps_lbnl.txt
```

The UCSC script generates:

```text
formatted_timestamps_ucsc.txt
```

These timestamp files are used to fill the `institutes` section in the webpage generator script.

---

# 20. Copy timestamp lists into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Copy and paste the contents of:

```text
formatted_timestamps_bnl.txt
```

into the `institutes` BNL section.

Copy and paste the contents of:

```text
formatted_timestamps_lbnl.txt
```

into the `institutes` LBNL section.

Copy and paste the contents of:

```text
formatted_timestamps_ucsc.txt
```

into the `institutes` UCSC section.

These timestamp entries connect each HX serial number with its ML parent module and timestamp.

---

# 21. Copy Category A serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_a_iv_high
```

Copy and paste ML serial numbers into the corresponding BNL, LBNL, or UCSC ML-only section.

Category A is only for ML serial numbers.

Category A means:

```text
IV current above 300 nA threshold.
One or more IV JSON files show HIGH CURRENT WARNING.
These modules have leakage/current values exceeding the allowed limit.
```

---

# 22. Copy Category B serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_b_noise_high
```

Copy and paste HX serial numbers into the corresponding BNL, LBNL, or UCSC HX-only section.

Category B is only for HX serial numbers.

Category B means:

```text
Input-noise mean above 1100.
One or more input-noise JSON files have mean noise > 1100.
These modules show excessive input noise and fail the noise threshold requirement.
```

---

# 23. Copy Category C serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_c_noise_low
```

Copy and paste HX serial numbers into the corresponding BNL, LBNL, or UCSC HX-only section.

Category C is only for HX serial numbers.

Category C means:

```text
Input-noise values are below the low-noise threshold.
These modules contain unusually low input-noise values.
```

---

# 24. Copy Category D(i) serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_d_i_iv_incomplete
```

Copy and paste ML serial numbers into the corresponding BNL, LBNL, or UCSC ML-only section.

Category D(i) is only for ML serial numbers.

Category D(i) means:

```text
Incomplete IV dataset.
The IV test exists, but the expected number of IV JSON files was not generated.
```

---

# 25. Copy Category D(ii) serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_d_ii_inputnoise_incomplete
```

Copy and paste HX serial numbers into the corresponding BNL, LBNL, or UCSC HX-only section.

Category D(ii) is only for HX serial numbers.

Category D(ii) means:

```text
Incomplete input-noise dataset.
The input-noise test exists, but the expected number of input-noise JSON files was not generated.
```

---

# 26. Copy Category E(i) serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_e_i_iv_unavailable
```

Copy and paste ML serial numbers into the corresponding BNL, LBNL, or UCSC ML-only section.

Category E(i) is only for ML serial numbers.

Category E(i) means:

```text
IV data unavailable or could not be processed.
The IV data is missing, inaccessible, or the script could not process it correctly.
```

---

# 27. Copy Category E(ii) serial numbers into the webpage generator

Open:

```text
generate_channel_page_scrolldetailedhis.py
```

Find the section:

```python
category_e_ii_inputnoise_unavailable
```

Copy and paste HX serial numbers into the corresponding BNL, LBNL, or UCSC HX-only section.

Category E(ii) is only for HX serial numbers.

Category E(ii) means:

```text
Input-noise data unavailable or could not be processed.
The input-noise data is missing, inaccessible, or the script could not process it correctly.
```

---

# 28. Add module comments

Module comments can be added in:

```text
generate_channel_page_scrolldetailedhis.py
```

Use this format:

```python
module_comments = {
    "SN20USBHX2002099": "GPC2413-0017-B6-X",
}
```

The module comment appears in the final webpage row for that module.

Module comments are useful for adding extra production information, module identifiers, or notes.

---

# 29. Generate the final category webpage

After copying the timestamp lists, category lists, and module comments into:

```text
generate_channel_page_scrolldetailedhis.py
```

run:

```bash
python generate_channel_page_scrolldetailedhis.py
```

This generates the category website folder.

The generated files are:

```text
index.html
bnl.html
lbnl.html
ucsc.html
```

These pages show the IV plots, input-noise plots, combined histograms, detailed histograms, JSON files, timestamps, comments, and category notes.

---

# 30. What each webpage row shows

Each row lists the HX serial number, the ML parent module, available input-noise plots, IV plots, combined histograms, detailed histograms, and category notes.

Each row includes:

```text
HX serial number
ML parent module
timestamp
input-noise plots
IV plots
combined histograms
detailed histograms
status/category notes
module comments
```

The webpage links to available files such as:

```text
input-noise PDF plots
input-noise PNG plots
IV PDF plots
IV PNG plots
combined histogram PDFs
combined no-skip histogram PDFs
detailed histogram PDFs
JSON files
low/high value JSON files
```

---

# 31. Upload the webpage and folders to CERNBox

After generating the webpage, copy and paste the generated HTML files into the CERNBox script or CERNBox upload location.

Upload:

```text
index.html
bnl.html
lbnl.html
ucsc.html
```

Also upload the full site folders:

```text
BNL/
LBNL/
UCSC/
```

The BNL, LBNL, and UCSC folders must be uploaded because the HTML files link to plots and JSON files inside those folders.

If the folders are not uploaded, the webpage may load, but the plot and JSON links will not work.

---

---

# 32. Webpage instructions

To create the webpage, follow the CERN Web EOS site creation tutorials:

```text
https://webeos.docs.cern.ch/create_site/
```

The webpage is linked here:

```text
https://ameliame.web.cern.ch/
```

---

## 32.1 Generate the HTML page

Run the page-generation script:

```bash
python generate_channel_page_scrolldetailedhis.py
```

This creates:

```text
index.html
```

Then upload `index.html` to your CERNBox.

All plot folders should also be uploaded to CERNBox.

Example plot folders include:

```text
SN20USBML1235874
SN20USBHX2002657
```

---

## 32.2 Upload `index.html` to CERNBox

Upload `index.html` to the following path:

```text
https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www
```

Each time you edit `index.html`, re-upload the updated version to CERNBox.

---

## 32.3 Upload plot folders to CERNBox

Upload each DB Serial Number folder and X-Hybrid Mounted Number folder to the corresponding site folder.

For BNL modules, upload to:

```text
https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www/BNL/
```

For LBNL modules, upload to:

```text
https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www/LBNL/
```

For UCSC modules, upload to:

```text
https://cernbox.cern.ch/files/spaces/eos/user/a/ameliame/www/UCSC/
```

This is where the webpage reads the plot content from.

---

# 33. Notes

A few useful naming conventions used in this workflow:

- **X-Hybrid Mounted Number**: used for input noise and histogram workflows
- **DB Serial Number**: used for IV workflows
- **Response Curve TC**: used for input noise related database extraction
- **Module AMAC IV TC**: used for thermal cycling IV data
- **Module IV with PS V1**: used for pre-gluing IV data


# 34. Category definitions

Category A means the IV current is above the 300 nA threshold.

This category uses ML serial numbers.

Category B means the input-noise mean is above 1100.

This category uses HX serial numbers.

Category C means input-noise values are below the low-noise threshold.

This category uses HX serial numbers.

Category D(i) means the IV dataset is incomplete.

This category uses ML serial numbers.

Category D(ii) means the input-noise dataset is incomplete.

This category uses HX serial numbers.

Category E(i) means the IV data is unavailable or could not be processed.

This category uses ML serial numbers.

Category E(ii) means the input-noise data is unavailable or could not be processed.

This category uses HX serial numbers.

---

# 35. Full command list

Run the serial-number generator scripts:

```bash
python serialnumbergenerate_inputnoise_bnl.py
python serialnumbergenerate_inputnoise_lbnl.py
python serialnumbergenerate_inputnoise_ucsc.py
python serialnumbergenerate_IV_bnl.py
python serialnumbergenerate_IV_lbnl.py
python serialnumbergenerate_IV_ucsc.py
```

Run the ML IV JSON-generation scripts:

```bash
python get_all_tests_categoryE_i_bnl.py
python get_all_tests_categoryE_i_lbnl.py
python get_all_tests_categoryE_i_ucsc.py
```

Run the HX input-noise JSON-generation scripts:

```bash
python get_all_tests_categoryDandE_ii_bnl.py --test_name "Module AMAC IV TC"
python get_all_tests_categoryDandE_ii_lbnl.py --test_name "Module AMAC IV TC"
python get_all_tests_categoryDandE_ii_ucsc.py --test_name "Module AMAC IV TC"
```

Run the IV plotting scripts:

```bash
python plot_multi_IV_final_BNL.py -i "BNL/ML/*/*.json"
python plot_multi_IV_final_BNL.py -i "LBNL/ML/*/*.json"
python plot_multi_IV_final_BNL.py -i "UCSC/ML/*/*.json"
```

Run the BNL input-noise plotting scripts:

```bash
python plot_multi_inputnoise_BNL.py -i "BNL/HX/SN*/*.json"
python plot_multi_inputnoise_noskip_BNL.py -i "BNL/HX/SN*/*.json"
python plot_combined_inputnoise_BNL.py -i "BNL/HX/SN*/*.json"
python plot_combined_inputnoise_noskip_BNL.py -i "BNL/HX/SN*/*.json"
python plot_detailed_inputnoise_histograms_per_file_BNL.py -i "BNL/HX/SN*/*.json"
```

Run the LBNL input-noise plotting scripts:

```bash
python plot_multi_inputnoise_LBNL.py -i "LBNL/HX/SN*/*.json"
python plot_multi_inputnoise_noskip_LBNL.py -i "LBNL/HX/SN*/*.json"
python plot_combined_inputnoise_LBNL.py -i "LBNL/HX/SN*/*.json"
python plot_combined_inputnoise_noskip_LBNL.py -i "LBNL/HX/SN*/*.json"
python plot_detailed_inputnoise_histograms_per_file_LBNL.py -i "LBNL/HX/SN*/*.json"
```

Run the UCSC input-noise plotting scripts:

```bash
python plot_multi_inputnoise_UCSC.py -i "UCSC/HX/SN*/*.json"
python plot_multi_inputnoise_noskip_UCSC.py -i "UCSC/HX/SN*/*.json"
python plot_combined_inputnoise_UCSC.py -i "UCSC/HX/SN*/*.json"
python plot_combined_inputnoise_noskip_UCSC.py -i "UCSC/HX/SN*/*.json"
python plot_detailed_inputnoise_histograms_per_file_UCSC.py -i "UCSC/HX/SN*/*.json"
```

Run the timestamp scripts:

```bash
python get_test_timestamp_full_list_BNL.py
python get_test_timestamp_full_list_LBNL.py
python get_test_timestamp_full_list_UCSC.py
```

Run the webpage generator:

```bash
python generate_channel_page_scrolldetailedhis.py
```

Upload the generated files and folders to CERNBox:

```text
index.html
bnl.html
lbnl.html
ucsc.html
BNL/
LBNL/
UCSC/
```

---

# 36. Troubleshooting notes

If a module appears in Category E(i), the IV data may be missing, unavailable, inaccessible, or not processed correctly.

If a module appears in Category E(ii), the input-noise data may be missing, unavailable, inaccessible, or not processed correctly.

If a module appears in Category D(i), the IV test exists, but not all 24 expected JSON files were generated.

If a module appears in Category D(ii), the input-noise test exists, but not all 25 expected JSON files were generated.

If a module appears in Category A, the IV data was processed successfully, but one or more current values exceeded the 300 nA threshold.

If a module appears in Category B, the input-noise data was processed successfully, but one or more files had mean noise above 1100.

If a module appears in Category C, the input-noise data was processed successfully, but one or more values were below the low-noise threshold.

If a webpage link is broken, check that the corresponding PDF, PNG, or JSON file exists in the expected folder.

If the webpage loads but the plots do not open, make sure the BNL, LBNL, and UCSC folders were uploaded to CERNBox with the same folder structure used by the HTML files.

If many modules appear in Category E, check the authentication token first.

If the timestamp column is missing or incorrect, regenerate the timestamp files and copy them again into the correct BNL, LBNL, or UCSC section of `generate_channel_page_scrolldetailedhis.py`.
