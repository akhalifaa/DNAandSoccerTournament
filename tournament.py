# Simulate a sports tournament

import csv
import sys
import random
from math import sqrt

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    #CLA to input csv file, it will be in sys.argv[1]
    with open(sys.argv[1],"r") as file:  #open csv file in read mode and name it file
        reader = csv.DictReader(file)  #create a reader for the file in dictionary form
        for row in reader:
            row['rating'] = int(row['rating'])
            teams.append(row)  #loop over every row in that reader, convert each rating value to int and append the dict row into our teams list



    counts = {}
    keys = []
    for i in range(len(teams)):
        keys.append((teams[i]['team'])) #loop over range of teams, append team names in our keys list

    for j in range(len(keys)):
        counts[keys[j]] = 0   #loop over len of keys, input keys into key slots in count dict and assign 0 to each one


    for tourn in range(N):
        win = simulate_tournament(teams)
        counts[win] +=1


    #first loop throguh teams, and initialize the counts dictionary by assigning 0 to each team
    #then for loop, N times, each N tournament increment the counter for the relevant team

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    for i in range(len(teams)):
        teams = simulate_round(teams)
        if len(teams) == 1:
            return teams[0]['team'] #returns the NAME only, of the winning team. teams is in the form of a single dimention dict inside a list

if __name__ == "__main__":
    main()

    #FOLLOW THE FUNCTIONS SEQUENTIALLY TO DETERMINE HOW TO FORMAT YOUR WORK