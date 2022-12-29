{{ config(materialized='view') }}

select
'07030' as zipcode,
room_size,
value,
state,
city,
beds,
count,
min,
max,
avg,
median,
adjusted_rental_income,
median_night_rate,
median_occupancy
from {{ source('airbnb', 'hoboken_rental_rates') }}