## Introduction

Here is a bundle of scripts for cleaning, transform and generate random data for visual purposes

## Random Photo Uploader

Create a folder named "products" with photos classified by subfolders. The script is going to randomize every subfolder and photo name to pick one and upload it into a airtable column.

Is necessary to create a new column in airtable with the formula "RECORD_ID()", copy the data and put into a "records.csv". The reference is going to be use for upload every photo for every row.

#### Enviroment variables

- API_KEY = Airtable api key. Obtain it here: https://airtable.com/create/tokens
- BASE_ID = The first value in the airtable url. Start with app... https://airtable.com/app...../....
- TABLE_ID = The Second value in the airtable url. Start with tbl...  https://airtable.com/app...../tbl.../...
- COLUMN_ID = You can get it checking the option "Manage Fields" in the dropdown list at the table name. Search for Field ID option into the button rigth the last column name "Dependencies". Make sure that the column type is "Attachment".

## Clean and Transform

Using sample data from https://www.kaggle.com/datasets/kyanyoga/sample-sales-data/data, the script makes type corrections, cleaning and create avg_price column grouping price_each by product_code.

## Random Specs Generator

Making use of lorem library, the script generates a short description for every product_code. 