import requests
import json

class Forcast:
    def __init__(self, lat, long):
    	self.lat = lat
    	self.long = long
    	self.forcastUrl = self.gridId = self.gridX = self.gridY = None
  
    #def parseQuery(self):

    
    #def getQueryResult(self):

    
    def getStationGridDataFromLatLong(self):
        header = 'User-Agent: (project_lapis_manalis, roboticapostle@gmail.com)'
        url = 'https://api.weather.gov/points/' + self.lat + ',' + self.long
        gridRequest = requests.get(url, headers = {'User-Agent': '(project_lapis_manalis, roboticapostle@gmail.com)'})
        if(gridRequest.status_code == 200):
            requestRet = json.loads(gridRequest.text)
            self.gridX = requestRet["properties"]["gridX"]
            self.gridY = requestRet["properties"]["gridY"]
            self.gridId = requestRet["properties"]["gridId"]
            self.forcastUrl = requestRet["properties"]["forecast"]
        else:
            print('Request for lat and long returned error code: ' + str(gridRequest.status_code))

    
    def query(self):
        # First we need the to convert lat and long to grid points and get additonal data for those points.
        if self.gridX == None and self.gridY == None:
           self.getStationGridDataFromLatLong()

        header = 'User-Agent: (project_lapis_manalis, roboticapostle@gmail.com)'
        gridRequest = requests.get(self.forcastUrl, headers = {'User-Agent': '(project_lapis_manalis, roboticapostle@gmail.com)'})
        if(gridRequest.status_code == 200):
            print(gridRequest.text)
        else:
            print('Request for lat and long returned error code: ' + str(gridRequest.status_code))

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