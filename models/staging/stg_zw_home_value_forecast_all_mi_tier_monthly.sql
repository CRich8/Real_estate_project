{{ config(materialized='view') }}

select
*
from {{ source('mis', 'zw_home_value_forecast_all_mi_tier_monthly') }}