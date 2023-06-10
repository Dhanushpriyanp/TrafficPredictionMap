# 1178435025
# 981458031

import json 
import heapq
import math

MAX_VAL = float("inf")
global graph

PLACES = {
    "Marina Beach": [13.0500, 80.2824],
    "Kapaleeshwarar Temple": [13.0325, 80.2697],
    "Fort St. George": [13.0803, 80.2870],
    "Valluvar Kottam": [13.0509, 80.2422],
    "Santhome Basilica": [13.0352, 80.2754],
    "Guindy National Park": [13.0067, 80.2217],
    "Elliott's Beach": [12.9996, 80.2713],
    "Government Museum": [13.0756, 80.2626],
    "Theosophical Society": [13.0064, 80.2586],
    "Arignar Anna Zoological Park": [12.8761, 80.0858],
    "Vivekananda House": [13.0493, 80.2766],
    "Crocodile Bank": [12.7829, 80.2516],
    "Cholamandal Artists' Village": [12.8665, 80.2437],
    "DakshinaChitra": [12.8331, 80.2482],
    "Sri Parthasarathy Temple": [13.0669, 80.2825],
    "Kishkinta Theme Park": [12.9073, 80.0847],
    "MGR Film City": [12.8532, 80.1328],
    "Semmozhi Poonga": [13.0486, 80.2525],
    "Armenian Church": [13.0781, 80.2612],
    "VGP Universal Kingdom": [12.8236, 80.2503],
    "Kalakshetra Foundation": [12.9950, 80.2586],
    "Edward Elliot's Beach": [13.0062, 80.2656],
    "Pondy Bazaar": [13.0490, 80.2421],
    "Birla Planetarium": [13.0117, 80.2361],
    "Snake Park": [13.0068, 80.2557],
    "Ashtalakshmi Temple": [13.0074, 80.2741],
    "Valluvar Statue": [13.0567, 80.2711],
    "VGP Snow Kingdom": [12.8239, 80.2499],
    "Vandalur Zoo": [12.8936, 80.0837],
    "Ripon Building": [13.0836, 80.2763],
    "Sri Ramakrishna Math": [13.0358, 80.2650],
    "Anna Centenary Library": [13.0106, 80.2086],
    "Dheeran Chinnamalai Statue": [13.0919, 80.2176],
    "Connemara Public Library": [13.0712, 80.2645],
    "Chennai Rail Museum": [13.100257, 80.20883],
    "Government Estate": [13.0761, 80.2602],
    "Valluvar Kottam Monument": [13.0497, 80.2426]
}

with open('NNetworkData.json') as json_file:
    graph = json.load(json_file)

completeCoordinateList = {}

for node in graph:

    latitude = int(graph[node]["LAT"].split(',')[0])
    longitude = int(graph[node]["LON"].split(',')[0])

    latitude = latitude*0.00001
    longitude = longitude*0.00001

    latitude = round(latitude, 5)
    longitude = round(longitude, 5)

    completeCoordinateList[(latitude, longitude)] = node    

# print(completeCoordinateList)
    
print(f'the graph contains {len(graph)} nodes')

for link, data in graph.items():
    new = data["REF_NODE_NEIGHBOR_LINKS"].split(',')
    new_non = data["NONREF_NODE_NEIGHBOR_LINKS"].split(',')
    data["REF_NODE_NEIGHBOR_LINKS"] = new
    data["NONREF_NODE_NEIGHBOR_LINKS"] = new_non

print('done')



# to find closest pair of coordinates

def haversineDistance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

def findClosestPlace(latitude, longitude):
    min_distance = float('inf')
    closest_place_id = None

    for coords, place in completeCoordinateList.items():
        place_lat, place_lon = coords
        distance = haversineDistance(latitude, longitude, place_lat, place_lon)
        if distance < min_distance:
            min_distance = distance
            closest_place_id = place

    return closest_place_id



def path(graph, start_node, end_node):

    distances = {node:MAX_VAL for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}

    
    queue = [(0, start_node)]

    while queue:

        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == end_node:
            break

        all_neighbors = graph[current_node]['REF_NODE_NEIGHBOR_LINKS'] + graph[current_node]['NONREF_NODE_NEIGHBOR_LINKS']

        for neighbor in all_neighbors:


            neighbor = neighbor.strip('-')

            if neighbor != '' and neighbor in graph:

                link, data = graph[neighbor]['LINK_ID'], graph[neighbor]['LINK_LENGTH']
                distance = current_distance + float(data)

                if distance < distances[neighbor]:

                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

    if distances[end_node] == float('inf'):
        return 'fuck'
    
    path = []
    node = end_node
    while node is not None:
        path.insert(0, node)
        node = predecessors[node]
    
    final_coord = []
    for link in path:
        final_coord += [[graph[link]['LON'].split(',')[0], graph[link]['LAT'].split(',')[0]]]
    
    return final_coord



# cl = (path(graph, '714263571', '715032831'))
# for i in cl:
#     a = int(i[0])
#     b = int(i[1])
#     a = a*0.00001
#     b = b*0.00001 
#     print(str([round(a, 5),round(b, 5)])+',') 
