from survey import CensusData
from geography import Geography
import os

# Global variables
MY_API_KEY = os.environ.get('CENSUS_API_KEY')
release_year = 2023

# Initialize a place
us = Geography(geographic_level='country', geography_name='United States', country_fips='1')
texas = Geography(geographic_level='state', geography_name='Texas', state_fips='48')
houston_metro = Geography(geographic_level='metro', geography_name='Houston Metro', metro_fips='26420')
harris_county = Geography(geographic_level='county', geography_name='Harris County', state_fips='48', county_fips='201')
houston_city = Geography(geographic_level='place', geography_name='Houston City', state_fips='48', place_fips='35000')
montrose = Geography(geographic_level='zipcode', geography_name='Montrose', state_fips='48', zipcode_fips=['77006', '77019'])
midtown = Geography(
    geographic_level='tract', 
    geography_name='Montrose Tract', 
    state_fips='48', 
    county_fips='201', 
    tract_fips=['312501', '312502'])

# Initialize a CensusData object
census_data = CensusData(survey_name='ACS', survey_span='5-Year', release_year=2023, api_key=MY_API_KEY)

# Create a group of geographies
areas = [us, texas, houston_metro, harris_county, houston_city, montrose, midtown]


# Basic Test
if not MY_API_KEY:
    raise ValueError("API key not found")
# Test survey parameter
try:
    assert census_data.get_survey_parameter() == '2023/acs/acs5/'
except:
    print(census_data.get_survey_parameter())
# Test base url
try:
    assert census_data.build_base_url() == 'https://api.census.gov/data/2023/acs/acs5/?key=' + MY_API_KEY
except:
    print(census_data.build_base_url())

# Test geography parameters
try:
    assert [x.get_geography_parameter(2023) for x in areas] == [
        '&for=us:1', 
        '&for=state:48', 
        '&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:26420', 
        '&for=county:201&in=state:48', 
        '&for=place:35000&in=state:48', 
        '&for=zip%20code%20tabulation%20area:77006,77019', 
        '&for=tract:312501,312502&in=state:48%20county:201'
    ]
except:
    print([x.get_geography_parameter(2023) for x in areas])



print("All tests pass")
