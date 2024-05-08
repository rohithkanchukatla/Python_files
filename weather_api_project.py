import requests
class city:
    def __init__(self,name,lat,lon,units="metric"):
        self.name=name
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}')
            
        except:
            print("oops no ineternet")

        response_json=response.json()
        self.temp=response_json["main"]["temp"]
        self.temp_min=response_json["main"]["temp_min"]
        self.temp_max=response_json["main"]["temp_max"]

    def print_data(self):
        units_symbol='C'
        if self.units=='imperial':
            units_symbol='F'
            print(f"In {self.name} the temperature is {self.temp} {units_symbol} ")
            print(f"In {self.name} the  minimum temperature is {self.temp_min} {units_symbol} C")
            print(f"In {self.name} the maximum temperature is {self.temp_max} {units_symbol} C")
        

city1=city("tokyo",38,49,units="imperial")
city1.print_data()
     
