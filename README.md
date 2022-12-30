# Reak Estate Market Analysis: Hoboken, NJ (07030)
Due to the rise in prices of houses in New Jersey, I was interested to see if investing in real estate was still a great opportunity for those looking for passive income. I chose Hoboken, New Jersey as the market to analyze because I personally am interested in this city and because it is in high demand both on Zillow and Airbnb.  The goal is to create a dashboard for an investor to use to analyze the real estate market of interest. I collected data from multiple sources including Zillow, Airbnb, Realtor.com and FHFA in order to get an overview of the real estate market of Hoboken, NJ.

## Overview of the pipeline
The pipeline is setup on GCP to ingest each dataset and perform ddaily transformation in order to provide up-to-date data for performing analytics. The project is desiigned as per the diagram, below. Airflow, hosted by Docker, is used to orchestrate the ingestion and scraping of active listings on Zillow to Google Cloud Storage (GCS). Airbnb data is extracted from Rapid API and transformed into a CSV for ingestion to GCS. Census and Realtor.com data are downloaded as CSV files from their sites and uploaded to GCS. DBT transforms the raw data to a staging layer in BigQuery where the tables are prepared for Tableau.

![Pipeline overview](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Real_Estate_Project_Overview.png)

## Data Analysis
It is no secret that the average house price in America has been on a sharp rise in the last few decades. In the last 20 years, the House Price Index in New Jersey has more than doubled.

The definition of House Price Index from the FHFA website:
> *The FHFA HPI is a broad measure of the movement of single-family house prices. The FHFA HPI is a weighted, repeat-sales index, meaning that it measures average price changes in repeat sales or refinancings on the same properties*

![NJHPI](https://github.com/CRich8/Real_estate_tracker/blob/main/images/NJHPI.png)

There are many factors which influence the housing market. Part of the reason for such a sharp increase is due to the lower volume of active listings. The supply of availble homes to purchase are decreasing while simultaneaously, the demand for houses has increased. The laws of supply and demand in this relationship clearly are responsible for the price increase. One solution to this problem is to improve the zoning laws in New Jersey. Local municipalities should focus on expanding high density zoning to increase the supply of housing.

![NJALC](https://github.com/CRich8/Real_estate_tracker/blob/main/images/NJALC.png)

To meet the needs of an investor looking to purchase a house, I scraped active listings from Zillow.com. I displayed the data in a map and table to easily identify important details of a listing.

![Active Listings](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Active_Zillow_Listings_Map.png)

Airbnb is a great way for investors to generate passive income with residential real estate. There is a growing movement of entrepreanurs, real estate companies and savvy homeowners converting their property into a passive income generating asset. To determine the potential ROI of a house in Hoboken, I extracted Airbnb data from RapidAPI. This allows an investor to easily compare the details of a listing to the Airbnb market of their chosen city. In this case study, the Hoboken Airbnb market is 

Let's see what the distribution of daily price, monthly income and rental type are for the Hoboken Airbnb market.

![Airbnb Overview](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Airbnb_overview.png)

As to be expected for a high density city, Apartment is by far the most common rental type. The most common daily price ranges between $150 - $200 and monthly income between $1k  - $3k. Both daily price and rental income are right-skewed histograms which iis not surprsising since income and wealth are classic examples of this distribution. These are important metrics to consider when purchasing a house in Hoboken.

Another important part of running an Airbnb business is being aware of the occupancy rate of the city and your own property. For example, owning a 5 bedroom home valued at $500 a night is only as good as the amount of bookings you get in a month to cover your mortgage.

![Room Count Analysis](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Room_count_analysis.png)

The national occupancy rate in 2022 was 48%. Hoboken saw an average of 57% which is well above the national average, indicating it has a strong Airbnb market. It is also important to compare the occupancy rate between different house sizes by room. By analyzing the performance between houses with diifferent room counts. an investor can narrow down their search for houses that are optimized for the highest occupancy rateand daily price combination.

As you can see, 1 and 3 bedroom houses have the highest occupancy rate. An interesting thing to note is the near identical monthly income of 3 and 4 bedroom homes. This occurs despite 4 room homes having a much higher median night rate. This exemplifies the importance of investing in high occupancy rate houses. You can also see that 1 and 2 room houses have the highest count of rentals which to investor should indicate more competition. 

Based on this analysis, 3 room houses in Hoboken, NJ appear to be the best investment. However, an investor must be lucky enough to find an active 3 room listing. Fortunately, my daily active Zillow listing scraper accomplishes this. 

As of 12/30/22, the listing for 218 Jackson St APT 6, Hoboken, NJ 07030 is the lowest cost, 3 bedroom house on the market. https://www.zillow.com/homedetails/218-Jackson-St-APT-6-Hoboken-NJ-07030/2064674728_zpid/


