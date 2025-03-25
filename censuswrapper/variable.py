# Class named variable that holds information about the variable_name and variable_code
class Variable:
    def __init__(self, variable_code):
        self.variable_code = variable_code
    
    def is_valid(self):
        pass

    def get_variable_parameter(self):
        pass 


# Class named Variable_Collection that holds a collection of variables
class Variable_Collection:
    def __init__(self, variables, release_year):
        # Check that the variables are census variable codes, or a list of them
        self.release_year = release_year
        self.variables = variables
        self.variable_collection = []
        self.build_variable_collection()
    

    def build_variable_collection(self):
        # Check that all the variables are valid
        for var in self.variables:
            if Variable(var).is_valid():
                self.variable_collection.append(Variable(var))
            else:
                raise ValueError("Invalid variable code")
    
    def __iter__(self):
        return iter(self.variable_collection)
    
    def __len__(self):
        return len(self.variable_collection)
    
    def __getitem__(self, index):
        return self.variable_collection[index]