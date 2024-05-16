# Class for geographic areas
class Geography:
    def __init__(self, geoIDs=None, geoLevel=None, geoYear=None):
        self.geoIDs = geoIDs
        self.geoLevel = geoLevel
        self.geoYear = geoYear
    
    # Return the geographic ids
    def get_geo_ids(self):
        return self.geoIDs
    
    # Print the values of the object
    def print_values(self):
        print("GeoIDs: ", self.geoIDs)
        print("GeoLevel: ", self.geoLevel)
        print("GeoYear: ", self.geoYear)


# Class for Census variables
class Variables:
    def __init__(self, varIDs=None, varYear=None):
        self.varID = varIDs
        self.varYear = varYear
    
    # Return the variable ids
    def get_var_ids(self):
        return self.varID
    
    # Print the values of the object
    def print_values(self):
        print("VarIDs: ", self.varID)
        print("VarYear: ", self.varYear)


# Class for ACS Query
class ACS:
    def __init__(self, geo=Geography(), var=Variables(), acsYear=None):
        self.geo = geo
        self.var = var
        self.acsYear = acsYear
    
    # Set the geographic area
    def set_geography(self, geo):
        self.geo = geo
    
    # Set the variables
    def set_variables(self, var):
        self.var = var
    
    # Set the year
    def set_year(self, acsYear):
        self.acsYear = acsYear
    
    # Print the values of the object
    def print_values(self):
        print("ACS Year: ", self.acsYear)
        self.geo.print_values()
        self.var.print_values()

