import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("constructors_2024_standings.csv")

print(data.info())

lastest_round = data["Round"].max()

teams = data["Constructor"].unique()
teams_name = ['Red Bull', 'Ferrari', 'Mercedes', 'McLaren', 'Aston Martin',
       'Sauber', 'Haas', 'RB', 'Williams',
       'Alpine']
colors = []
for team in teams:
    if team == "McLaren":
        colors.append("Orange")
    elif team == "Ferrari":
        colors.append("Red")
    elif team == "Red Bull":
        colors.append("Steelblue")
    else:
        colors.append("grey")



# Create a figure
fig, ax = plt.subplots(figsize=(8,6), facecolor="Black")  # Adjust the figure size for better proportions
  # Spans all 10 rows in the first column

for team, color in zip(teams, colors):
    df = data[data["Constructor"] == team]
    ax.plot(df["Round"], df["Position"], color = color, linewidth=2)

for team, color, name in zip(teams, colors, teams_name):
    df = data[data["Round"] == lastest_round]
    position = int(data[(data["Round"] == lastest_round) & (data["Constructor"] == team)]["Position"].iloc[0])
    ax.text(lastest_round + 0.2, position, s = name, color = color, fontsize=10)


ax.invert_yaxis()
ax.set_frame_on(False)

ax.set_xlabel("Round", fontsize=14, font = "Times New Roman", color="grey")
ax.set_ylabel("Championship Position", fontsize = 14, font = "Times New Roman", color="grey")
ax.set_xticks(np.arange(2, 19, 2), labels= np.arange(2, 19, 2), font = "sans serif", color="grey")
ax.set_yticks([x for x in range(1, 11)], labels=[x for  x in range(1, 11)], font = "sans serif", color="grey")
ax.set_title("F1 Constructor Championship standings \nSeason (2024)", font = 'Times New Roman', size = 18, color="White")
ax.grid(visible = False)
ax.text(0, 11.5, s = "x - @i_oxymoron", font="Times New Roman", color = "white", fontsize=13)

fig.savefig("standings.png", format="png", dpi=600)



fig, ax = plt.subplots(figsize=(8,6), facecolor="Black")  # Adjust the figure size for better proportions
  # Spans all 10 rows in the first column

for team, color in zip(teams, colors):
    df = data[data["Constructor"] == team]
    ax.plot(df["Round"], df["Points"], color = color, linewidth=2)

for team, color, name in zip(teams, colors, teams_name):
    df = data[data["Round"] == lastest_round]
    position = int(data[(data["Round"] == lastest_round) & (data["Constructor"] == team)]["Points"].iloc[0])
    ax.text(lastest_round + 0.2, position, s = name, color = color, fontsize=7)

ax.set_frame_on(False)

ax.set_xlabel("Round", fontsize=14, font = "Times New Roman", color="grey")
ax.set_ylabel("Championship Points", fontsize = 14, font = "Times New Roman", color="grey")
ax.set_xticks(np.arange(2, 19, 2), labels= np.arange(2, 19, 2), font = "sans serif", color="grey")
ax.set_yticks(np.arange(0, 550, 50), labels= np.arange(0, 550, 50), font = "sans serif", color="grey")
ax.set_title("F1 Constructor Championship standings \nSeason (2024)", font = 'Times New Roman', size = 18, color="White")
ax.grid(visible = False)
ax.text(0, -100, s = "x - @i_oxymoron", font="Times New Roman", color = "white", fontsize=11)

fig.savefig("standings_points.png", format="png", dpi=600)
