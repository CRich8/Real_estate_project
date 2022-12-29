{{ config(materialized='view') }}

select
string_field_0 as Category,
string_field_2 as Stat
from {{ source('mis', 'nj_census_qf') }}