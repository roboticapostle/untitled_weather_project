import requests
import json

class ForcastQuery:
    def __init__(self, lat, long):
    	self.lat = lat
    	self.long = long
    	self.forcastUrl = self.gridId = self.gridX = self.gridY = self.forcastDict = None
    
    def getQueryResult(self):
        return self.forcastDict
    
    def getStationGridDataFromLatLong(self):
        header = 'User-Agent: (project_lapis_manalis, roboticapostle@gmail.com)'
        url = 'https://api.weather.gov/points/' + self.lat + ',' + self.long
        gridRequest = requests.get(url, headers = {'User-Agent': '(project_lapis_manalis)'})
        if(gridRequest.status_code == 200):
            requestRet = json.loads(gridRequest.text)
            self.gridX = requestRet["properties"]["gridX"]
            self.gridY = requestRet["properties"]["gridY"]
            self.gridId = requestRet["properties"]["gridId"]
            self.forcastUrl = requestRet["properties"]["forecast"]
            return True
        else:
            print('Request for lat and long returned error code: ' + str(gridRequest.status_code))
            return False
    
    def query(self):
        # First we need the to convert lat and long to grid points and get additonal data for those points.
        if self.gridX == None and self.gridY == None:
           if(self.getStationGridDataFromLatLong() == False):
               print("Query failed")
               return False

        header = 'User-Agent: (project_lapis_manalis, roboticapostle@gmail.com)'
        forcastRequest = requests.get(self.forcastUrl, headers = {'User-Agent': '(project_lapis_manalis, roboticapostle@gmail.com)'})
        if(forcastRequest.status_code == 200):
            print(forcastRequest.text)
            self.forcastDict = json.loads(forcastRequest.text)
            return True
        else:
            print('Request for lat and long returned error code: ' + str(forcastRequest.status_code))
            return False

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
    forcast = ForcastQuery(lat,long)
    forcast.query()