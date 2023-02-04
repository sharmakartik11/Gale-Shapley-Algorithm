#Ques 10(A)

#Find a Gale-Shapley implementation in python on Github and modify it so that the eight Super Group 1 teams will be matched against the eight Super Group 2 teams. You can make up the preference lists for each team. Make sure you cite any code you use or state that you wrote it from scratch if you did.

import time


def doStableMatching(group1, group2):
    startTime = time.time()
    n = len(group1)

    teamsInOne = {
        0: 'Argentina',
        1: 'Brazil',
        2: 'Germany',
        3: 'France',
        4: 'Canada',
        5: 'Paraguay',
        6: 'Croatia',
        7: 'Wales',
    }
    teamsInTwo = {
        0: 'England',
        1: 'Italy',
        2: 'Denmark',
        3: 'Uruguay',
        4: 'Mexico',
        5: 'Iran',
        6: 'Saudi Arabia',
        7: 'Ghana',
    }

    unpairedTeams = list(range(n))
    teamOnePair = [None] * n
    teamTwoPair = [None] * n
    proposalsMadeByTeamOne = [0] * n
    while unpairedTeams:
        selectedTeamFromGroupOne = unpairedTeams[0]
        preferencesOfSelectedTeam = group1[selectedTeamFromGroupOne]  # array of preferences, eg. [[0,1,2]]
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
            preferenceNumberOfSelectedTeamGroupOne = preferencesOfOppositionTeamGroupTwo.index(selectedTeamFromGroupOne)

            if preferenceNumberOfSelectedTeamGroupOne > preferenceNumberOfCurrentPairedTeam:
                teamTwoPair[oppositionTeamFromGroupTwo] = selectedTeamFromGroupOne
                teamOnePair[selectedTeamFromGroupOne] = oppositionTeamFromGroupTwo
                proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
                unpairedTeams.pop(0)
                unpairedTeams.insert(0, currentPairOfOppositionTeam)
            else:
                proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1

    for i, num in enumerate(teamOnePair):
        print(teamsInOne[i] + ' v/s ' + teamsInTwo[num])
    endTime = time.time()
    print(f"Time elapsed with 16 teams: \t: {(endTime - startTime) * 10 ** 3:.03f}ms")


superGroup1 = [
  [1, 6, 5, 4, 0, 3, 7, 2],
  [5, 6, 1, 2, 0, 4, 3, 7],
  [2, 0, 4, 5, 1, 6, 7, 3],
  [3, 5, 2, 4, 0, 6, 1, 7],
  [1, 6, 2, 3, 7, 0, 5, 4],
  [6, 0, 4, 7, 2, 1, 3, 5],
  [5, 0, 1, 4, 7, 6, 3, 2],
  [5, 2, 4, 3, 1, 6, 7, 0]
]
superGroup2 = [
  [4, 1, 2, 0, 6, 7, 5, 3],
  [4, 6, 2, 0, 3, 1, 5, 7],
  [5, 3, 0, 7, 6, 4, 1, 2],
  [4, 0, 6, 3, 5, 1, 7, 2],
  [1, 6, 7, 5, 0, 4, 3, 2],
  [0, 6, 1, 3, 2, 4, 7, 5],
  [7, 6, 4, 1, 0, 5, 2, 3],
  [7, 3, 4, 0, 2, 5, 1, 6]
]

doStableMatching(superGroup1, superGroup2)

# reference - https://github.com/Vishal-Kancharla/Gale-Shapley-Algorithm