{{ config(materialized='view') }}

select
PARSE_DATE('%Y%m', cast(month_date_yyyymm as string)) as date,
postal_code,
nielsen_hh_rank,
hotness_rank,
hotness_rank_mm,
hotness_rank_yy
hotness_score,
median_days_on_market,
median_dom_vs_us,
median_listing_price,
median_listing_price_mm,
median_listing_price_yy,
median_listing_price_vs_us
from {{ source('mis', 'RDC_Inventory_Hotness_Metrics_Zip_History') }}