#pip install haversine
from haversine import haversine
import openrouteservice as ors
import pandas as pd

def close_loc(df, domain, ty, facility_name):
    
    # find the longitudes and latitudes of each address
    domain['coordinates'] = [[domain["longitudes"][i], domain["latitudes"][i]] for i in range(len(domain))]
    add = domain['coordinates']    
    d = df["coordinates"]
    domain[facility_name] = 0
    
    # compare each address with each facility
    for i in range(len(domain)):
        coor = add[i]
        
        # store distances between these two locations
        distances = []
        min_two = []
        
        # store the indexes of the two nearest points
        index_k = [] 
        client = ors.Client(key='5b3ce3597851110001cf624871b9224fee1d4d87b3a69a85f4fbb4a7')
        
        # compute all the distances
        for j in range(len(df)):
            dis = haversine((df["Latitude"][j], df["Longitude"][j]), (domain["latitudes"][i], domain["longitudes"][i]))
            distances.append(dis)
        lst = distances[:]
        
        # find the two nearest points of the address
        for k in range(2):
            index_i = lst.index(min(lst))
            index_k.append(index_i)
            lst[index_i] = float('inf')
            
        # compute the two distances as traveled by car
        for point in index_k:
            coordinates = [add[i], d[point]]
            route = client.directions(
                coordinates=coordinates,
                profile='driving-car',
                format='geojson',
                validate=False,
                radiuses=-1
            )
            min_two.append(route['features'][0]['properties']['segments'][0]['distance'])
            
        # print the cloest location
        print("Address %d : %d" % (i , min(min_two))) 
        domain[facility_name][i] = min(min_two)
        
    # generate a unique file name
    name = '../data/curated/' + ty + '_facilities' + ".csv"
    domain.to_csv(name, index = False)
