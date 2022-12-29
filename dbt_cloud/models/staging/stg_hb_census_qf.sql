{{ config(materialized='view') }}

select
string_field_0 as Category,
string_field_2 as Stat
from {{ source('mis', 'hb_census_qf') }}