 # censusWrapper_objectParadigm
Wrapper to simplify queries of the American Community Survey API and perform common transformations and calculations<br>

# Disclaimer
This library provides a more convenient way to interact with the Census Bureau API, and no guarantee is made regarding the accuracy of the data that is returned. This library is dependent upon equivalency tables published by the Census Bureau, the no guarantee is made that either the geographies or variables are precisely equivalent. Researchers are responsible for ensuring the methodology for translating geographies and variables from year-to-year is suitable for their needs.<br>

# Background
The US Census Bureau publishes their American Community Survey (ACS) on an annual basis. The ACS helps researchers understand communities by providing survey data aggregated across a variety of geographical areas. <br>
Datasets: The American Community Survey is published in two datasets - one with 5-year data and another with 1-year data. The 5-year dataset samples the population of an area over the course of 5 years, while the 1-year dataset only samples the population in a single year. In some cases, researchers prefer to use 5-year data because the results are expected to have a higher degree of statistical accuracy. In other cases, researchers prefer to use 1-year data because the results are more current, especially when the community is changing rapidly. This project will focus on the 5-year datasets to begin with, with plans to expand to include the 1-year datasets. (There is also a 3-year dataset, but it was discontinued after 2013.) <br>
Years: The American Community Survey was first collected in 2005, and 1-year datasets are available back to this time. The 5-year dataset was first published with the completion of the 2009 survey. <br>
Geographies: ACS surveys are collected from a sample of individuals across the country, but individual responses are not made available to the public. The only data available to the public is that which has been aggregated across different geographical areas. These geographical areas may be as granular as tracts or blocks, or as broad as the entire nation.
Variables: ACS variables represent the questions asked in surveys. The variables (like "DP05_001E") have a label (like "Estimate!!SEX AND AGE!!Total population") and are grouped in tables (like "DP05") according to their concept (like "ACS DEMOGRAPHIC AND HOUSING ESTIMATES"). <br>
Values: Each dataset-year-geography-variable combination has a published value representing the number or percentage of the population that fits its criteria. These values may be of integer (estimates), float (margins of error/percentages), or string (annotations) datatypes. In some cases where values are unavailable, the number "-666666666" is used as a placeholder for "NA" values.<br>

# Challenges when using ACS data
The Census Bureau made a REST API available to the public to easily query their datasets. Even so, there are difficulties that arise, especially when working with data from different years. <br>
Geographies are not static and may change from year to year. For instance, census tracts are redrawn every ten years with the decennial census, meaning the 2019 residents of tract "2125.00" may find that as of 2020 their homes have been redesignated as part of tract "2125.02". This means that researchers of this neighborhood must look up its census tract for each year they wish to research and adjust their API call accordingly. <br>
Variables are not consistent either, and a survey question in one year may not have the same variable from one year to another. For instance, the population of an area that is foreign-born is assigned the variable "DP02_0094E" in 2019, but is assigned the variable "DP02_0095E" in 2020. This means that a researcher who is comparing foreign-born populations in 2019 to foreign-born populations in 2020 must be aware of this change and adjust their API call accordingly. <br>
Furthermore, sometimes researchers may wish to present the data in different ways. For instance, by grouping the population over the age of 65 together in one bracket, whereas the ACS has several variables for several brackets for those ages over 65. Or the researcher may wish to show the average Annual Median Income for a group of census tracts. This requires researchers to perform their own calculations to obtain the desired results. <br>

# Purpose of this wrapper
This wrapper aims to simplify the process of translating ACS geographies and variables from one year to another, as well as to automatically perform some of the most common transformations and calculations that researchers need. <br>

# Setup
Run setup.py <br>
The Census Bureau publishes several change documents with each release of the ACS which highlight any geographies and variables that have been redefined since the previous year. The setup.py script scrapes the Census Bureau website for these change documents and creates a dictionary that enables us to translate geographies and variables from one year to another.<br>

# Making a query
#### Choose years
#### Choose geographies
#### Choose variables
#### Run a query
#### Transform the data