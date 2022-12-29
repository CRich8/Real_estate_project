{{ config(materialized='view') }}

select
*
from {{ source('mis', 'housing_inventory__new_listing_count_nj') }}