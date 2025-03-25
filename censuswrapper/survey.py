# Import dependencies
from geography import Geographic_Collection
from variable import Variable_Collection

# Global variables
# Most recent year for each survey
LATEST_YEAR = 2023

# Class which stores the survey_name, survey_span, and release_year
class CensusData:
    ALLOWED_SURVEYS = ['ACS']
    ALLOWED_SPANS = ['1-Year', '5-Year']

    def __init__(self, survey_name: str, survey_span: str, release_year: int, api_key: str):
        # Check if the survey name and span are valid
        if survey_name not in self.ALLOWED_SURVEYS:
            raise ValueError(f"Survey name must be one of {self.ALLOWED_SURVEYS}")
        if survey_span not in self.ALLOWED_SPANS:
            raise ValueError(f"Survey span must be one of {self.ALLOWED_SPANS}")
        # Set the survey name, span, and release year
        self.survey_name = survey_name
        self.survey_span = survey_span
        self.release_year = release_year
        self.api_key = api_key
        self.response_collection = []

    # Method to return the survey code
    def get_survey_parameter(self):
        if self.survey_name == 'ACS':
            if self.survey_span == '1-Year':
                # Check if the survey year is within the valid range, if so return the url component for this survey
                if self.release_year in range(2005, LATEST_YEAR + 1):
                    return f'{self.release_year}/acs/acs1/'
                else:
                    raise ValueError(f"Release year must be between 2005 and {LATEST_YEAR}")
            elif self.survey_span == '5-Year':
                # Check if the survey year is within the valid range, if so return the url component for this survey
                if self.release_year in range(2009, LATEST_YEAR + 1):
                    return f'{self.release_year}/acs/acs5/'
                else:
                    raise ValueError(f"Release year must be between 2009 and {LATEST_YEAR}")

    # Method to build the base url
    def build_base_url(self) -> str:
        # Start with the base url
        url = f'https://api.census.gov/data/{self.get_survey_parameter()}?key={self.api_key}'
        return url

    # Method to build the url and call the api
    def query(self, geographies, variables): #??????
        geographies = Geographic_Collection(geographies)
        variables = Variable_Collection(variables, self.release_year)
        # Loop through the geographies
        for geo in geographies:
            # Build the base url
            base_url = self.build_base_url()
            # Add the geographic parameter
            base_url += f'{geo.get_geography_parameter(self.release_year)}'
            # Add the variables to the url
            variables = Variable_Collection(variables)
            for var in variables:
                url = base_url + var.get_variable_parameter()
                # Call the api with the url
                response = self.call_api(url)
                # Add the response to the collection
                self.add_response(response)
        return self.response_collection



    # Method to change years
    def reset_year(self, release_year: int):
        self.release_year = release_year
        self.response_collection = []
        self.survey_parameter = self.get_survey_parameter()
        # Translate the variables to the new year
        #


    def add_response(self, response):
        self.response_collection.append(response)   
        

    def call_api(url):
        # Call the api
        pass
        # 

