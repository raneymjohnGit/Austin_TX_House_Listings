SELECT r.*,
h.dec_2019_appreciation,
h.jan_2021_appreciation
INTO housing_data_appreciated
FROM raw_housing_data_3 as r
JOIN house_appreciation as h
ON r.month_year = h.month_year