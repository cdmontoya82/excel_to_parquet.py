# Excel to Parquet Converter

A simple and robust Python script to batch convert Microsoft Excel (`.xlsx`) files into Apache Parquet (`.parquet`) format. 

Using Parquet format significantly reduces file size and speeds up data reading processes, making it ideal for data engineering pipelines and analytics.

## Features
* **Batch Processing:** Converts all Excel files located in a specific folder.
* **Schema Handling:** Automatically converts mixed-type 'object' columns to strings to prevent Parquet schema errors.
* **Clean Console:** Suppresses harmless `openpyxl` style warnings often found in auto-generated Excel reports.

## Prerequisites

You need Python installed along with the following libraries:

```bash
pip install pandas pyarrow openpyxl
