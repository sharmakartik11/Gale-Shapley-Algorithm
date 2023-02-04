#Ques 10(E)

#Double the size of the lists in problem A several times (you can make up team names like team1, team2, etc.) and measure the amount of time it takes to create stable matches.  How fast does the execution time grow in relation to the size of the lists?

#It takes 0.387ms (0.250ms - 0.387ms) to execute a list of 16 teams in 2 groups, which is more than what it took for 8 teams in a group (0.083ms). When you divide, you can see that it takes approximately 4 times the time to execute when the list is doubled,

#Execute below code to check the time

import time

def stableMatching(group1, group2):
    startTime = time.time()
    teamsInGroupOne = {
        0: 'Argentina',
        1: 'Brazil',
        2: 'Germany',
        3: 'France',
        4: 'Canada',
        5: 'Paraguay',
        6: 'Croatia',
        7: 'Wales',
        8: 'Chile',
        9: 'Australia',
        10: 'Japan',
        11: 'Belgium',
        12: 'Northern Ireland',
        13: 'China',
        14: 'South Korea',
        15: 'Czech Republic'
    }
    teamsInGroupTwo = {
        0: 'England',
        1: 'Italy',
        2: 'Denmark',
        3: 'Uruguay',
        4: 'Mexico',
        5: 'Iran',
        6: 'Saudi Arabia',
        7: 'Ghana',
        8: 'India',
        9: 'Morocco',
        10: 'Egypt',
        11: 'Qatar',
        12: 'Russia',
        13: 'Poland',
        14: 'Serbia',
        15: 'Ukraine'
    }

    n = len(group1)
    unpairedTeams = list(range(n))
    teamOnePair = [None] * n
    teamTwoPair = [None] * n
    proposalsMadeByTeamOne = [0] * n
    while unpairedTeams:
        selectedTeamFromGroupOne = unpairedTeams[0]
        preferencesOfSelectedTeam = group1[selectedTeamFromGroupOne]  # array of preferences, eg. [[0, 1, 2]]
        oppositionTeamFromGroupTwo = preferencesOfSelectedTeam[proposalsMadeByTeamOne[selectedTeamFromGroupOne]]
        preferencesOfOppositionTeamGroupTwo = group2[oppositionTeamFromGroupTwo]
        currentPairOfOppositionTeam = teamTwoPair[oppositionTeamFromGroupTwo]

        if currentPairOfOppositionTeam is None:
            teamTwoPair[oppositionTeamFromGroupTwo] = selectedTeamFromGroupOne
            teamOnePair[selectedTeamFromGroupOne] = oppositionTeamFromGroupTwo
            proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
            unpairedTeams.pop(0)

        else:
            preferenceNumberOfCurrentPairedTeam = preferencesOfOppositionTeamGroupTwo.index(
                currentPairOfOppositionTeam)
            preferenceNumberOfSelectedTeamGroup1 = preferencesOfOppositionTeamGroupTwo.index(selectedTeamFromGroupOne)

            if preferenceNumberOfSelectedTeamGroup1 > preferenceNumberOfCurrentPairedTeam:
                teamTwoPair[oppositionTeamFromGroupTwo] = selectedTeamFromGroupOne
                teamOnePair[selectedTeamFromGroupOne] = oppositionTeamFromGroupTwo
                proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
                unpairedTeams.pop(0)
                unpairedTeams.insert(0, currentPairOfOppositionTeam)
            else:
                proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
    for i, num in enumerate(teamOnePair):
        print(teamsInGroupOne[i] + ' v/s ' + teamsInGroupTwo[num])

    endTime = time.time()
    print(f"\n Time taken for creating a fixture list with 32 teams: \t: {(endTime-startTime)*10**3:.03f}ms")


superGroup1 = [
  [12, 15, 0, 9, 5, 13, 4, 3, 8, 1, 10, 7, 14, 6, 2, 11],
  [14, 4, 3, 0, 10, 8, 11, 12, 5, 13, 15, 1, 9, 6, 2, 7],
  [13, 4, 14, 3, 0, 12, 2, 10, 1, 7, 11, 9, 15, 8, 5, 6],
  [7, 3, 0, 13, 12, 8, 9, 6, 2, 4, 14, 5, 11, 15, 1, 10],
  [4, 14, 8, 0, 6, 2, 3, 15, 1, 7, 13, 11, 5, 10, 12, 9],
  [4, 15, 13, 6, 3, 1, 8, 11, 10, 9, 12, 0, 14, 5, 2, 7],
  [3, 13, 0, 6, 4, 1, 14, 12, 11, 2, 7, 5, 15, 8, 9, 10],
  [11, 10, 6, 1, 0, 2, 12, 13, 4, 8, 5, 14, 15, 7, 9, 3],
  [8, 3, 12, 13, 10, 4, 7, 5, 0, 2, 6, 11, 1, 9, 15, 14],
  [3, 6, 12, 5, 2, 0, 1, 4, 8, 10, 11, 9, 15, 13, 14, 7],
  [10, 5, 12, 0, 7, 6, 15, 9, 8, 4, 2, 13, 3, 1, 14, 11],
  [10, 8, 13, 12, 1, 5, 7, 0, 2, 6, 15, 3, 4, 9, 14, 11],
  [5, 13, 3, 0, 14, 7, 15, 2, 9, 10, 1, 6, 11, 12, 4, 8],
  [2, 3, 5, 8, 6, 13, 7, 1, 4, 12, 9, 10, 0, 11, 15, 14],
  [3, 15, 8, 10, 14, 5, 9, 13, 6, 2, 12, 1, 11, 7, 0, 4],
  [8, 10, 0, 5, 15, 2, 7, 6, 3, 1, 12, 4, 11, 9, 14, 13]
]

superGroup2 = [
        [15, 1, 4, 9, 3, 10, 12, 5, 11, 0, 2, 6, 14, 7, 13, 8],
        [1, 6, 10, 11, 14, 2, 3, 15, 0, 8, 12, 13, 4, 7, 5, 9],
        [14, 4, 9, 2, 6, 15, 8, 5, 3, 7, 11, 0, 10, 12, 13, 1],
        [3, 0, 8, 7, 5, 13, 15, 12, 11, 6, 14, 4, 2, 1, 10, 9],
        [8, 10, 14, 7, 11, 5, 2, 13, 1, 4, 6, 12, 3, 9, 0, 15],
        [7, 0, 15, 14, 11, 4, 12, 13, 2, 5, 8, 9, 6, 1, 3, 10],
        [4, 0, 11, 9, 10, 5, 7, 6, 13, 8, 14, 12, 2, 15, 3, 1],
        [5, 13, 2, 7, 11, 12, 3, 1, 0, 4, 8, 15, 6, 10, 14, 9],
        [14, 6, 10, 11, 7, 8, 4, 15, 9, 0, 3, 5, 13, 12, 2, 1],
        [13, 5, 1, 0, 10, 2, 8, 3, 11, 14, 4, 15, 7, 9, 6, 12],
        [6, 10, 11, 8, 1, 4, 2, 0, 12, 14, 15, 3, 7, 9, 13, 5],
        [9, 6, 1, 7, 5, 0, 12, 8, 10, 15, 3, 2, 13, 14, 4, 11],
        [12, 13, 7, 9, 2, 0, 4, 1, 14, 15, 6, 10, 8, 3, 11, 5],
        [4, 7, 11, 1, 5, 13, 10, 2, 12, 8, 0, 14, 6, 9, 15, 3],
        [10, 0, 8, 1, 9, 5, 7, 13, 12, 14, 4, 11, 3, 15, 6, 2],
        [1, 4, 6, 8, 5, 13, 14, 3, 9, 11, 0, 2, 12, 7, 15, 10]
    ]

stableMatching(superGroup1, superGroup2)

# reference - https://github.com/Vishal-Kancharla/Gale-Shapley-Algorithm