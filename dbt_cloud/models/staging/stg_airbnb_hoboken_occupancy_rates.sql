{{ config(materialized='view') }}

select
'07030' as zipcode,
*
from {{ source('airbnb', 'hoboken_occupancy_rates') }}