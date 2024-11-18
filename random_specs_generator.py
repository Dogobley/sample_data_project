import pandas as pd
import lorem as lm

df = pd.read_csv('sales_data_sample_fixed.csv')
products = df['product_code'].unique()

specs = []

for product in products:
    spec = {}
    spec['product_code'] = product
    spec['specifications'] = lm.sentence()
    
    specs.append(spec)

specs = pd.DataFrame(specs)

df = df.merge(specs, how='left', on='product_code')
df = df[['product_code', 'specifications']]

df.to_csv('product_specification_lorem.csv', index=False)