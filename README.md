# Reak Estate Market Analysis: Hoboken, NJ (07030)
Due to the rise in prices of houses in New Jersey, I was interested to see if investing in real estate was still a great opportunity for those looking for passive income. I chose Hoboken, New Jersey as the market to analyze because I personally am interested in this city and because it is in high demand both on Zillow and Airbnb. I collected data from multiple sources including Zillow, Airbnb, Realtor.com and Census in order to get an overview of the real estate market.

## Overview of the pipeline
The pipeline is setup on GCP to ingest each dataset and perform ddaily transformation in order to provide up-to-date data for performing analytics. The project is desiigned as per the diagram, below. Airflow, hosted by Docker, is used to orchestrate the ingestion and scraping of active listings on Zillow to Google Cloud Storage (GCS). Airbnb data is extracted from Rapid API and transformed into a CSV for ingestion to GCS. Census and Realtor.com data are downloaded as CSV files from their sites and uploaded to GCS. DBT transforms the raw data to a staging layer in BigQuery where the tables are prepared for Tableau.

![Pipeline overview](https://github.com/CRich8/Real_estate_tracker/blob/main/images/Real_Estate_Project_Overview.png)

## Data Analysis
It is no secret that the average house price in America has been on a sharp rise in the last few decades. In the last 20 years, the House Price Index in New Jersey has more than doubled.

![NJHPI](https://github.com/CRich8/Real_estate_tracker/blob/main/images/NJHPI.png)
