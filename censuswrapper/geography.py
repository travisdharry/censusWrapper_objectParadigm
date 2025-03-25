# Class named Geography that holds information about the geographic_level and geographic_codes
class Geography:
    ALLOWED_LEVELS = ['country', 'state', 'county', 'metro', 'place', 'zipcode', 'tract']

    def __init__(
            self, 
            geographic_level='country', 
            country_fips=1,
            geography_name = None,
            state_fips=None,
            county_fips=None,
            metro_fips=None,
            place_fips=None,
            zipcode_fips=None,
            tract_fips=None,
        ):
        # Check if the geographic level is valid
        if geographic_level in self.ALLOWED_LEVELS:
            self.geographic_level = geographic_level
        else:
            raise ValueError(f"Geographic level must be one of {self.ALLOWED_LEVELS}")
        # Set the name of the geography
        self.geography_name = geography_name
        # Set the fips codes
        if country_fips:
            if isinstance(country_fips, str):
                self.country_fips = country_fips
            elif isinstance(country_fips, int):
                self.country_fips = str(country_fips)
            else:
                raise ValueError("Country fips must be a string or an integer")
        if state_fips:
            if isinstance(state_fips, str):
                self.state_fips = state_fips
            elif isinstance(state_fips, int):
                self.state_fips = str(state_fips)
            else:
                raise ValueError("State fips must be a string or an integer")
        if county_fips:
            if isinstance(county_fips, str):
                self.county_fips = county_fips
            elif isinstance(county_fips, int):
                self.county_fips = str(county_fips)
            else:
                raise ValueError("County fips must be a string or an integer")
        if metro_fips:
            if isinstance(metro_fips, str):
                self.metro_fips = metro_fips
            elif isinstance(metro_fips, int):
                self.metro_fips = str(metro_fips)
            else:
                raise ValueError("Metro fips must be a string or an integer")
        if place_fips:
            if isinstance(place_fips, str):
                self.place_fips = place_fips
            elif isinstance(place_fips, int):
                self.place_fips = str(place_fips)
            else:
                raise ValueError("Place fips must be a string or an integer")
        # Check if the zipcode_fips datatypes are correct (lists are allowed)
        if zipcode_fips:
            if isinstance(zipcode_fips, str):
                self.zipcode_fips = zipcode_fips
            elif isinstance(zipcode_fips, int):
                self.zipcode_fips = str(zipcode_fips)
            elif isinstance(zipcode_fips, list):
                if all(isinstance(x, str) for x in zipcode_fips):
                    self.zipcode_fips = ",".join(zipcode_fips)
                elif all(isinstance(x, int) for x in zipcode_fips):
                    self.zipcode_fips = ",".join([str(x) for x in zipcode_fips])
            else:
                raise ValueError("Zipcode fips must be a string or a list of strings")
        # Check if the tract_fips datatypes are correct (lists are allowed)
        if tract_fips:
            if isinstance(tract_fips, str):
                self.tract_fips = tract_fips
            elif isinstance(tract_fips, int):
                self.tract_fips = str(tract_fips)
            elif isinstance(tract_fips, list):
                if all(isinstance(x, str) for x in tract_fips):
                    self.tract_fips = ",".join(tract_fips)
                elif all(isinstance(x, int) for x in tract_fips):
                    self.tract_fips = ",".join([str(x) for x in tract_fips])
                else:
                    raise ValueError("Tract fips must be a list of strings or integers")
            else:
                raise ValueError("Tract fips must be a string or integer")
        # Check if the lower geographic_levels have the info they need about the higher levels
        if self.geographic_level == 'county':
            if not self.state_fips:
                raise ValueError("state_fips must be provided")
        elif self.geographic_level == 'place':
            if not self.state_fips:
                raise ValueError("state_fips must be provided")
        elif self.geographic_level == 'zipcode':
            if not self.state_fips:
                raise ValueError("state_fips must be provided")
        elif self.geographic_level == 'tract':
            if not self.state_fips:
                raise ValueError("state_fips must be provided")
            if not self.county_fips:
                raise ValueError("county_fips must be provided")
        
    # Method to return the url component for the geography
    def get_geography_parameter(self, year: int) -> str:
        if self.geographic_level == 'country':
            return f'&for=us:{self.country_fips}'
        elif self.geographic_level == 'state':
            return f'&for=state:{self.state_fips}'
        elif self.geographic_level == 'county':
            return f'&for=county:{self.county_fips}&in=state:{self.state_fips}'
        elif self.geographic_level == 'metro':
            return f'&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:{self.metro_fips}'
        elif self.geographic_level == 'place':
            return f'&for=place:{self.place_fips}&in=state:{self.state_fips}'
        elif self.geographic_level == 'zipcode':
            # Handle the inconsistency in the census where they removed the "in" parameter for zipcodes in 2020
            if year >= 2020:
                return f'&for=zip%20code%20tabulation%20area:{self.zipcode_fips}'
            else:
                return f'&for=zip%20code%20tabulation%20area:{self.zipcode_fips}&in=state:{self.state_fips}'
        elif self.geographic_level == 'tract':
            return f'&for=tract:{self.tract_fips}&in=state:{self.state_fips}%20county:{self.county_fips}'
        

# Class named Geographic_Collection that groups a list of Geography objects
class Geographic_Collection:

    def __init__(self, geographies):
        # Check that the geographies are Geography objects, or a list of them
        if isinstance(geographies, Geography):
            geographies = [geographies]
        elif isinstance(geographies, list):
            for geo in geographies:
                if not isinstance(geo, Geography):
                    raise ValueError("All elements in the geography list must be Geography objects")
        else:
            raise ValueError("Geography must be a Geography object or a list of Geography objects")
        self.geographies = geographies
        
    # Iterate through self.geographies and return the individual Geography objects
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self.geographies):
            result = self.geographies[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


            
        
        




