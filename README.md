# Mini-Mart Sales Analysis — Pandas Practice Project

## Scenario
You're a data analyst at **Mini-Mart**, a small online store. You've been handed
raw order exports for January and February 2024, plus a customer lookup table.
Management wants a clean analysis: what's selling, who's buying, and where the
data needs cleanup. This project walks you through that, using every skill from
the 6-lesson pandas course, in order.

## Files
- `orders_jan.csv` — January orders (messy: missing discounts, missing ratings)
- `orders_feb.csv` — February orders (same structure as January)
- `customers.csv` — customer lookup table (id, name, signup date, tier, country)
- `starter.py` — skeleton script with all tasks as TODOs — **do this one**
- `solutions.py` — full worked solution — check yourself after attempting

Open `starter.py`, fill in each TODO, and run it (`python starter.py`) to check
your output against the expected description as you go.

---

## Tasks

### Part 1 — Creating, Reading, Writing
1. Read `orders_jan.csv` and `orders_feb.csv` into DataFrames. Print `.shape` and `.head()` of each.
2. Create a small DataFrame by hand called `store_info` with two columns, `metric` and `value`,
   holding `"store_name": "Mini-Mart"` and `"analyst": <your name>"` (as two rows).
3. Save `store_info` to `store_info.csv` without the index column.

### Part 2 — Indexing, Selecting, Assigning
4. Using `.loc`, select all orders from the `North` region with `unit_price ($)` above 50, from January.
5. Using `.iloc`, grab the first 10 rows and the first 3 columns of the January data.
6. Set `order_id` as the index of the January DataFrame (don't overwrite the original — assign to a new variable).
7. Add a new column `total_price` to both January and February data equal to `qty * unit_price ($) * (1 - discount_pct)`.
   (Careful — `discount_pct` has missing values; think about what a missing discount should mean for this calculation before you fill it, or come back to this after Part 5.)

### Part 3 — Summary Functions and Maps
8. Run `.describe()` on `unit_price ($)` and on `category` for the January data — note how the output differs for numeric vs. object columns.
9. Find the most common `category` and the most common `region` in January using `.value_counts()`.
10. Use `.map()` (or a direct arithmetic operation) to create a column `unit_price_vnd` that converts `unit_price ($)` to VND using a rate of 25,000.
11. Use `.apply()` with `axis='columns'` to create a column `high_value` that is `True` when `total_price > 100`.

### Part 4 — Grouping and Sorting
12. Group January orders by `category` and get total `qty` sold per category.
13. Group by `["region", "category"]` and compute total revenue (`total_price`) per group using `.agg()` with `sum`, `mean`, and `count` all at once.
14. Sort the result from task 13 by total revenue, descending.
15. Find, for each region, the single highest-value order (hint: `.groupby().apply(lambda df: df.loc[df.total_price.idxmax()])`).

### Part 5 — Data Types and Missing Values
16. Check `.dtypes` for the January DataFrame. Convert `order_date` to an actual datetime type.
17. Count how many missing values exist in each column (`.isnull().sum()`).
18. Fill missing `discount_pct` values with `0` (no discount recorded = none given). Fill missing `rating` values with the string `"Not rated"`.
19. Recompute `total_price` now that discounts are filled in, and compare it to your answer from task 7.

### Part 6 — Renaming and Combining
20. Rename `qty` back to `quantity` and `unit_price ($)` to `unit_price_usd` in both DataFrames.
21. Combine January and February into one DataFrame called `orders` using `pd.concat()`. Check the combined shape makes sense.
22. Join `orders` with `customers` on `customer_id` (a left join, so every order keeps its row even if a customer is somehow missing).
23. Using the joined table, find the total spend per `membership_tier`. Which tier brings in the most revenue in total? Which tier spends the most *on average per order*?

### Stretch goals (optional, combine everything)
24. Which `country` generated the most revenue in Feb specifically?
25. Which 5 customers (by `customer_name`) spent the most overall across both months?
26. Export your final cleaned & joined `orders` table to `orders_clean.csv`.
27. Bonus: what pattern do you notice about the `region` column missingness — is it random, or does it seem to correlate with anything (e.g. category)? (There's no single right answer here — this is about practicing exploration, since real messy data rarely has a clean explanation.)

---

## Tips
- Work top to bottom, but it's fine to peek at `solutions.py` for a specific task if you're stuck — the goal is fluency, not suffering.
- Print intermediate results constantly (`print(df.head())`, `print(df.dtypes)`) — that habit alone will save you the most debugging time.
- If a `groupby` result looks weird, check whether you have a MultiIndex you forgot to `.reset_index()`.