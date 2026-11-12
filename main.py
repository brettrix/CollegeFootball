import pandas as pd

data = pd.read_csv("cfb.csv")

input_season = int(input("Enter a season to analyze: "))

season_data = data[data["Season"] == input_season]

while season_data.empty:
    print("No season data. Please try again.")
    print()
    input_season = int(input("Enter a season to analyze: "))
    season_data = data[data["Season"] == input_season]

win_groups = {
    "10 or more wins:" : [],
    "8-9 wins:" : [],
    "6-7 wins:" : [],
    "Fewer than 6 wins:" : []
}

names = season_data["Team"].tolist()
wins = season_data["Win"].tolist()

for i in range(len(names)):
    if wins[i] < 6:
        win_groups["Fewer than 6 wins:"].append(names[i])
    elif wins[i] <= 7:
        win_groups["6-7 wins:"].append(names[i])
    elif wins[i] <= 9:
        win_groups["8-9 wins:"].append(names[i])
    else:
        win_groups["10 or more wins:"].append(names[i])

print(f"College Football results for {input_season}")
for i in win_groups:
    print(i)
    for j in win_groups[i]:
        print(f"   {j}")
    print()