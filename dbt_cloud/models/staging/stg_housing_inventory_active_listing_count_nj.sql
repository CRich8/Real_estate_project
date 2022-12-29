{{ config(materialized='view') }}

select
*
from {{ source('mis', 'housing_inventory_active_listing_count_nj') }}