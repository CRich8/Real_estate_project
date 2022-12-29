{{ config(materialized='view') }}

select
*
from {{ source('mis', 'zw_home_value_all_top_tier_monthly') }}