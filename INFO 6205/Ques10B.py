#Question 10 (B)

#Use a loop to shuffle the preference lists for each team 1000 times.  Calculate the percentage of stable playoff matches.  See the function random.shuffle(x[, random])

import random


def doStableMatching(group1, group2):
    n = len(group1)
    numberOfStableMatches = 0
    for x in range(1000):
        random.shuffle(group1)
        random.shuffle(group2)
        unpairedTeams = list(range(n))
        teamOnePair = [None] * n
        teamTwoPair = [None] * n
        proposalsMadeByTeamOne = [0] * n
        while unpairedTeams:
            selectedTeamFromGroupOne = unpairedTeams[0]
            preferencesOfSelectedTeam = group1[selectedTeamFromGroupOne]
            oppositionTeamFromGroupTwo = preferencesOfSelectedTeam[
            proposalsMadeByTeamOne[selectedTeamFromGroupOne]]
            preferencesOfOppositionTeamGroupTwo = group2[oppositionTeamFromGroupTwo]
            currentPairingOfOppositionTeam = teamTwoPair[oppositionTeamFromGroupTwo]

            if currentPairingOfOppositionTeam is None:
                teamTwoPair[oppositionTeamFromGroupTwo] = selectedTeamFromGroupOne
                teamOnePair[selectedTeamFromGroupOne] = oppositionTeamFromGroupTwo
                proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
                unpairedTeams.pop(0)

            else:
                preferenceNumberOfCurrentPairedTeam = preferencesOfOppositionTeamGroupTwo.index(
                    currentPairingOfOppositionTeam)
                preferenceNumberOfSelectedTeamGroup1 = preferencesOfOppositionTeamGroupTwo.index(selectedTeamFromGroupOne)

                if preferenceNumberOfSelectedTeamGroup1 > preferenceNumberOfCurrentPairedTeam:
                    teamTwoPair[oppositionTeamFromGroupTwo] = selectedTeamFromGroupOne
                    teamOnePair[selectedTeamFromGroupOne] = oppositionTeamFromGroupTwo
                    proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1
                    unpairedTeams.pop(0)
                    unpairedTeams.insert(0, currentPairingOfOppositionTeam)
                else:
                    proposalsMadeByTeamOne[selectedTeamFromGroupOne] += 1

        if None not in teamOnePair:
            numberOfStableMatches += 1

    percentSuccessInMatches = (numberOfStableMatches/1000) * 100
    print("Percentage of successful matches post shuffling :", percentSuccessInMatches, "%")



superGroup1 = [
    [0, 2, 4, 6, 7, 3, 5, 1],
    [0, 2, 1, 3, 5, 6, 4, 7],
    [1, 2, 3, 4, 7, 6, 5, 0],
    [7, 6, 1, 3, 4, 2, 5, 0],
    [4, 6, 7, 2, 1, 3, 0, 5],
    [3, 7, 4, 1, 2, 0, 5, 6],
    [5, 7, 1, 0, 2, 4, 3, 6],
    [0, 2, 4, 6, 7, 3, 5, 1],
]
superGroup2 = [
    [0, 1, 4, 7, 6, 3, 5, 2],
    [0, 2, 1, 7, 5, 4, 6, 3],
    [3, 2, 1, 7, 4, 6, 5, 0],
    [1, 5, 7, 3, 4, 2, 6, 0],
    [5, 6, 7, 2, 0, 3, 1, 4],
    [2, 6, 4, 1, 3, 5, 0, 7],
    [4, 6, 1, 0, 7, 5, 3, 2],
    [1, 2, 4, 7, 6, 3, 5, 0],
]

doStableMatching(superGroup1, superGroup2)


# reference - https://github.com/Vishal-Kancharla/Gale-Shapley-Algorithm