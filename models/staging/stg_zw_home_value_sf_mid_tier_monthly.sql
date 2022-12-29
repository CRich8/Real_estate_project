{{ config(materialized='view') }}

select
*
from {{ source('mis', 'zw_home_value_sf_mid_tier_monthly') }}