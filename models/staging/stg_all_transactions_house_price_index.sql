{{ config(materialized='view') }}

select
*
from {{ source('mis', 'all_transactions_house_price_index') }}