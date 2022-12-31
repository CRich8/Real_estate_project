# Real Estate Market Analysis: Hoboken, NJ (07030)
Due to the rising house prices in New Jersey, I wanted to see if investing in real estate was still an excellent opportunity for those looking for passive income. I chose Hoboken, New Jersey, as the market to analyze because of my interest in this city and because it is in high demand both on Zillow and Airbnb. The goal is to create a dashboard for investors to analyze their real estate market of interest. I collected data from multiple sources, including Zillow, Airbnb, Realtor.com, and FHFA.

## Overview of the pipeline
The pipeline is set up on GCP to ingest each dataset and perform daily transformations to provide up-to-date data for performing analytics. The project is designed as per the diagram below. Airflow, hosted by Docker, is used to orchestrate the ingestion and scraping of active listings on Zillow to Google Cloud Storage (GCS). Airbnb data is extracted from Rapid API and transformed into a CSV for ingestion to GCS. FHFA and Realtor.com data are downloaded as CSV files from their sites and uploaded to GCS. DBT transforms the raw data to a staging layer in BigQuery, where the tables are prepared for Tableau.

![Pipeline overview](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Real_Estate_Project_Overview.png)

## Data Analysis
It is no secret that the average house price in America has sharply risen in the last few decades. In the previous 20 years, the House Price Index in New Jersey has more than doubled.

The definition of the House Price Index from the FHFA website:
> *The FHFA HPI is a broad measure of the movement of single-family house prices. The FHFA HPI is a weighted, repeat-sales index, meaning that it measures average price changes in repeat sales or refinancings on the same properties*

![NJHPI](https://github.com/CRich8/Real_estate_tracker/blob/main/images/NJHPI.png)

Many factors influence the housing market. The lower volume of active listings is partly the reason for such a sharp increase. The supply of available homes to purchase is decreasing while simultaneously, the demand for houses has increased. One solution to this problem is to improve the zoning laws in New Jersey. Local municipalities should focus on expanding high-density zoning to increase the housing supply.

![NJALC](https://github.com/CRich8/Real_estate_tracker/blob/main/images/NJALC.png)

To meet the needs of an investor looking to purchase a house, I scraped active listings from Zillow.com. I displayed the data in a map and table to quickly identify important details of a listing.

![Active Listings](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Active_Zillow_Listings_Map.png)

Airbnb is an excellent way for investors to generate passive income with residential real estate. There is a growing movement of entrepreneurs, real estate companies, and savvy homeowners converting their property into a passive income-generating asset. To determine the potential ROI of a house in Hoboken, I extracted Airbnb data from RapidAPI. This allows an investor to quickly compare the details of a Zillow listing to the Airbnb market of their chosen city.

Let's see the distribution of daily price, monthly income, and rental type for the Hoboken Airbnb market.

![Airbnb Overview](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Airbnb_overview.png)

As expected for a high-density city, Apartment is by far the most common rental type. The most common daily price ranges between $150 - $200, and monthly income between $1k  - $3k. Both daily price and rental income are right-skewed histograms which are not surprising since income and wealth are classic examples of this distribution. These are important metrics to consider when purchasing a house in Hoboken.

Another critical part of running a sucessful Airbnb business is understanding the occupancy rate of your property and local market. For example, owning a five-bedroom home valued at $500 a night is only as good as the number of monthly bookings you receive at that price.

![Room Count Analysis](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Room_count_analysis.png)

The national occupancy rate in 2022 was 48%. Hoboken saw an average of 57%, which is well above the national average, indicating a strong Airbnb market. It is also essential to compare the occupancy rate between different house sizes by room. By analyzing the performance between houses with different room counts, investors can narrow their search for homes optimized for the highest occupancy rate and daily price combination.

As you can see, one and three-bedroom houses have the highest occupancy rate. An interesting thing to note is the nearly identical monthly income of three and four-bedroom homes, which occurs despite four-room homes having a much higher median night rate. This exemplifies the importance of investing in high occupancy rate houses. You can also see that one and two-room houses have the highest count of rentals, which indicates higher competition for renters. 

Based on this analysis, three-room houses in Hoboken, NJ, have the greatest opportunitiy to maximize ROI. They have the highest occupancy rate and higher daily night price compared to one room and lower upfront investment compared to four room houses. However, an investor must be lucky enough to find an active three-room listing at a price that makes sense. Fortunately, my daily active Zillow listing scraper accomplishes this. 

As of 12/30/22, the listing for 218 Jackson St APT 6, Hoboken, NJ 07030 is the lowest cost, three-bedroom house on the market. At only $770k, you can convert this property into a ~$4k/month passive income generatig asset. https://www.zillow.com/homedetails/218-Jackson-St-APT-6-Hoboken-NJ-07030/2064674728_zpid/


