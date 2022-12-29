{{ config(materialized='view') }}

select 
Date,
zpid,
imgSrc,
detailUrl,
statusType,
statusText,
CAST(TRIM(REGEXP_REPLACE(price, r'\$|,', ''), '+') as INT64) price,
address,
addressStreet,
addressCity,
addressState,
addressZipcode,
CAST(JSON_VALUE(latLong, '$.latitude') as FLOAT64) as latitude,
CAST(JSON_VALUE(latLong, '$.longitude') as FLOAT64) as longitude,
beds,
baths,
area,
zestimate,
brokerName,
hasOpenHouse,
openHouseDescription,
openHouseEndDate,
openHouseStartDate,
best_deal
from {{ source('staging', 'hoboken_raw_daily') }}