import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# A function to fetch data for each round of formula one from 2024 races

def fetch_round_data(round):
    print("Fetching data for round:", round)

    url = f"https://api.jolpi.ca/ergast/f1/2024/{round}/constructorstandings/"
    r = requests.get(url)
    data = r.json()
    return data



# Now we need to write a function that can parse the returned json 
# the Json contains all kinds of data but I only want specific data
# We also need to get that data into tabular format for plotting

def organize_data(round_data):

    round_df = pd.DataFrame({"Round": [], "Constructor":[], "Points":[], "Position":[]})
    print("Creating dataframe for round no:", round_data["MRData"]["StandingsTable"]["round"])


    for i in range(0, 10, 1):

        round = round_data["MRData"]["StandingsTable"]["round"]
        constructor = round_data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][i]['Constructor']['name']
        position = round_data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][i]['position']
        points = round_data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][i]['points']

        round_df = pd.concat([round_df, 
                              pd.DataFrame({"Round":[round], "Constructor":[constructor], "Points":[points], "Position":[position]})],
                              axis = 0)

    return round_df


# Let's check what is the latest round the data is available for 

url = "https://api.jolpi.ca/ergast/f1/2024/constructorstandings/"
r = requests.get(url)
json = r.json()
lastest_round = int(json["MRData"]["StandingsTable"]["round"])
print("Latest round data available is:" ,lastest_round)


# Finally let's fetch the data for all the available rounds from season 2024

rounds = np.arange(1, lastest_round + 1, 1)

data = pd.DataFrame({"Round":[], "Constructor":[], "Points":[], "Position":[]})

for round in rounds:
    round_data_json = fetch_round_data(round)
    round_data_df = organize_data(round_data_json)
    data = pd.concat([data, round_data_df], axis = 0)


#Fix the datatypes 

data_2024 = data.astype({"Round":"int32", "Points":"int32", "Position":"int32"})


print("Writing data to csv")
data_2024.to_csv("constructors_2024_standings.csv", index=False)
print("CSV written succesfully")
