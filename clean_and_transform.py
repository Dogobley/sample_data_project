import pandas as pd

path = 'sales_data_sample'
ext = '.csv'


df = pd.read_csv(path+ext)
df = df.replace('  ', ' ')

df.columns = df.columns.str.lower()

new_column_names = {
    'ordernumber' : 'order_number',
    'quantityordered' : 'quantity_ordered',
    'priceeach' : 'price_each',
    'orderlinenumber' : 'order_line_number',
    'sales' : 'sales',
    'orderdate' : 'order_date',
    'status' : 'status',
    'qtr_id' : 'qtr_id',
    'month_id' : 'month_id',
    'year_id' : 'year_id',
    'productline' : 'product_line',
    'msrp' : 'msrp',
    'productcode' : 'product_code',
    'customername' : 'customer_name',
    'phone' : 'phone',
    'addressline1' : 'address_line_1',
    'addressline2' : 'address_line_2',
    'city' : 'city',
    'state' : 'state',
    'postalcode' : 'postal_code',
    'country' : 'country',
    'territory' : 'territory',
    'contactlastname' : 'contact_last_name',
    'contactfirstname' : 'contact_first_name',
    'dealsize' : 'deal_size',
}

df = df.rename(columns=new_column_names)

replacements = {
    'address_line_1': {
        'Rambla de Catalu�a': 'Rambla de Cataluña',
        'Berguvsv�gen': 'Berguvsvägen'
    },
    'contact_first_name': {
        'Mart�n': 'Martin'
    }
}

for col, replace in replacements.items():
    for old, new in replace.items():
        df[col] = df[col].str.replace(old, new)


df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y %H:%M')
df['order_date'] = df['order_date'].dt.strftime('%m/%d/%Y')

df_avg_price = df.groupby('product_code')['price_each'].mean().round(2)
df = df.merge(df_avg_price, how='left', on='product_code')
df = df.rename(columns={'price_each_y': 'avg_price'})

df.to_csv(path + '_fixed' + ext, index=False)