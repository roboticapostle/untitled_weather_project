import requests
import json

class Forcast:
    def __init__(self, lat, long):
    	self.lat = lat
    	self.long = long
    	self.gridX = self.gridY = None
    	self.queryURL = "https://api.weather.gov/"
  
    #def parseQuery(self):

    
    #def getQueryResult(self):

    
    def convertLatLongToGridPoints(self):
        header = 'User-Agent: (project_lapis_manalis, roboticapostle@gmail.com)'
        url = 'https://api.weather.gov/points/' + self.lat + ',' + self.long
        gridRequest = requests.get(url, headers = {'User-Agent': '(project_lapis_manalis, roboticapostle@gmail.com)'})
        if(gridRequest.status_code == 200):
            requestRet = json.loads(gridRequest.text)
            self.gridX = requestRet["properties"]["gridX"]
            self.gridY = requestRet["properties"]["gridY"]
        else:
            print('Request for lat and long returned error code: ' + str(gridRequest.status_code))

    
    def query(self):
        if self.gridX == None and self.gridY == None:
           self.convertLatLongToGridPoints()

# Testing function for this class
if __name__ == "__main__":
    isEntryDone = False
    while isEntryDone == False:
        print("Enter your latitude")
        lat = input()

        print("Enter your longitude")
        long = input()

        print("You entered: " + str(lat) + " " + str (long) + " ")
        print("Is this correct? (y/n)")

        isSelectionMade = False

        while isSelectionMade == False:
            done = input()

            if done == "n":
                isSelectionMade = True
                isEntryDone = False
            elif done == "y":
                isSelectionMade = True
                isEntryDone = True
            else:
                print("Invalid selection: enter y or n")
                isSelectionMade = False
        forcast = Forcast(lat,long)
        forcast.query()