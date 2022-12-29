{{ config(materialized='view') }}

select
*
from {{ source('mis', 'zw_home_vale_all_mid_tier_monthly') }}