{{ config(materialized='view') }}

select
cast('2022-11-01' as Date) as Date,
postal_code,
median_listing_price,
median_days_on_market,
median_listing_price_per_square_foot,
median_square_feet,
average_listing_price
from {{ source('mis', 'RDC_Inventory_Core_Metrics_Zip') }}