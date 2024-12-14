
# Classes: Think of classes as blueprints for objects. 
# They define the structure and behavior of objects. 
# In this case, we have a class called Sandbox that defines the structure and behavior of a sandbox object. 
# The sandbox object is a dictionary that stores the variables and their values that are created in the sandbox. 
# Attributes: Are the variables that are defined in the class.
# Methods/Members: Are the functions that are defined in the class.

class Car:
    
    # Parameterized constructor
    def __init__(self):
        """
        Initializes the car object with attributes.
        """
        self.Brand = ""
        self.Model = ""
        self.Year = 0
        self.Color = ""
        
    def __del__(self):
        """
        Destructor that is called when the object is destroyed.
        """
        print("Object is destroyed")
        
    def setBrand(self, brand):
        """
        Sets the brand of the car.
        """
        self.Brand = brand
        
    def setModel(self, model):
        """
        Sets the model of the car.
        """
        
        self.Model = model
        
    def setYear(self, year):
        """
        Sets the year of the car.
        """
        self.Year = year
        
    def setColor(self, color):
        """
        Sets the color of the car.
        """
        self.Color = color
        
    def getBrand(self):
        """
        Returns the brand of the car.
        """
        return self.Brand
    
    def getModel(self):
        """
        Returns the model of the car.
        """
        return self.Model
    
    def getYear(self):
        """
        Returns the year of the car.
        """
        return self.Year
    
    def getColor(self):
        """
        Returns the color of the car.
        """
        return self.Color
        
    def display(self):
        """
        Displays the details of the car
        """
        print("Brand: ", self.Brand)
        print("Model: ", self.Model)
        print("Year: ", self.Year)
        print("Color: ", self.Color)

