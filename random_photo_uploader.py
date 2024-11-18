import os
import random
import requests
import base64
import pandas as pd
from dotenv import load_dotenv
import time

load_dotenv()

source_folder = os.path.join(os.getcwd(), 'products')
certificate = os.path.join(os.getcwd(), 'airtable.crt')
rec_ids = pd.read_csv('records.csv', header=0)['record_id']
num_products = rec_ids.shape[0]

api_key = os.getenv('API_KEY')
base_id = os.getenv('BASE_ID')
table_id = os.getenv('TABLE_ID')
column_id = os.getenv('COLUMN_ID')

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def send_request(payload, rec_id):

    airtable_url = f"https://content.airtable.com/v0/{base_id}/{rec_id}/{column_id}/uploadAttachment"    

    response = requests.post(airtable_url, headers=headers, json=payload, verify=True)

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)


# Car brand folders in products
subfolders = [os.path.join(source_folder, subfolder) 
              for subfolder in os.listdir(source_folder) 
              if os.path.isdir(os.path.join(source_folder, subfolder))]

every_five = 0

# For every product, pick a random photo
for i in range(num_products):
    random_subfolder = random.choice(subfolders)
    photos = [f for f in os.listdir(random_subfolder) if os.path.isfile(os.path.join(random_subfolder, f))]
    
    if not photos:
        print(f"No photos found in subfolder: {random_subfolder}")
        continue
    
    random_photo = random.choice(photos)
    
    source_path = os.path.join(random_subfolder, random_photo)

    with open(source_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    payload = {
        "contentType": "image/jpeg",
        "file": base64_string,
        "filename": str(i)+".jpg"
        }

    every_five+=1

    send_request(payload, rec_ids.iloc[i])

    if every_five == 5:
        time.sleep(2)
        every_five = 0
    
