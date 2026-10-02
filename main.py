"""
Mini-Mart Sales Analysis — starter skeleton.
Fill in each TODO. Run with: python starter.py
See README.md for the full task descriptions.
"""
import pandas as pd

# ---------- Part 1: Creating, Reading, Writing ----------

#  1: read orders_jan.csv and orders_feb.csv
jan = pd.read_csv('orders_jan.csv', index_col=0)
feb = pd.read_csv('orders_feb.csv', index_col=0)
print(jan.shape, jan.head())
print(feb.shape, feb.head())

# 2: create store_info DataFrame by hand
store_info = pd.DataFrame()

#  3: save store_info to store_info.csv (no index)
store_info.to_csv('store_info.csv')

# ---------- Part 2: Indexing, Selecting, Assigning ----------

#  4: North region orders in Jan with unit_price ($) > 50
north_expensive = jan.loc[(jan.region == 'North') & (jan['unit_price ($)'] > 50)]

#  5: first 10 rows, first 3 columns of jan, using iloc
jan_subset = jan.iloc[:11, :4]

#  6: set order_id as index on a NEW variable (don't overwrite jan)
jan_indexed = jan.set_index('order_id')

#  7: add total_price column to jan and feb
jan["total_price"] = jan['qty'] + jan['unit_price ($)'] + jan['discount_pct']
feb["total_price"] = feb['qty'] + feb['unit_price ($)'] + feb['discount_pct']


# ---------- Part 3: Summary Functions and Maps ----------

#  8: describe() on unit_price ($) and category
a = jan['unit_price ($)'].describe()
b = jan['category'].describe()

#  9: most common category and region in jan
most_common_cat_jan = jan['category'].value_counts()[0]
most_common_reg_jan = jan['region'].value_counts()[0]

#  10: unit_price_vnd column (rate = 25000)
jan['unit_price_vnd'] = jan['unit_price ($)'] * 25000
#  11: high_value column using apply(axis='columns')
jan['high_value'] = jan.apply(lambda row : row['total_price'] > 100, axis='columns')

# ---------- Part 4: Grouping and Sorting ----------

#  12: total qty sold per category (jan)
jan.groupby('category').qty.sum()

#  13: group by [region, category], agg total_price with sum/mean/count
total_revenue = jan.groupby(['region', 'category'])['total_price'].agg(['sum', 'mean', 'count'])

# 14: sort task 13's result by total revenue, descending
what = total_revenue.sort_values(by='sum', ascending=False)


# 15: highest-value order per region
jan.groupby('region').apply(lambda df: df.loc[df['total_price'].idxmax()])

# ---------- Part 5: Data Types and Missing Values ----------

# 16: dtypes check + convert order_date to datetime
print(jan.dtypes)
jan['order_date'] = pd.to_datetime(jan['order_date'], errors='coerce')

# 17: count missing values per column
missing_values_col = jan.isna().sum()

# 18: fill missing discount_pct with 0, missing rating with "Not rated"
jan_filled = jan.fillna({'discount_pct': 0, 'missing rating': 'Not rated'})
# 19: recompute total_price after filling discounts
recomputed_total_price = jan.groupby(['region', 'category'])['total_price'].agg(['sum', 'mean', 'count']).sort_values(by='sum', ascending=False)

# ---------- Part 6: Renaming and Combining ----------

# 20: rename qty -> quantity, "unit_price ($)" -> unit_price_usd (both dfs)
jan.rename(columns={"qty": "quantity", "unit_price ($)": "unit_price_usd"}, inplace=True)
feb.rename(columns={"qty": "quantity", "unit_price ($)": "unit_price_usd"}, inplace=True)

# 21: concat jan + feb into `orders`
orders = pd.concat([jan, feb], axis=0)

# TODO 22: read customers.csv and left-join onto orders on customer_id
customers = pd.read_csv('customers.csv')

# TODO 23: total spend per membership_tier (sum and mean)


# ---------- Stretch goals ----------

# TODO 24: top country by revenue in Feb

# TODO 25: top 5 customers by total spend across both months

# TODO 26: export cleaned/joined orders to orders_clean.csv

# TODO 27: explore region missingness vs category (open-ended)
