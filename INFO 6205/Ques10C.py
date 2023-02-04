#Question 10(C)

#Randomly assume certain teams win and lose each round and eliminate the losers from the preference lists for each team. Can the Gale-Shapley matching algorithm be applied over and over in each round (16 teams, 8 teams, 4 teams, 2 teams) to create stable matches?

#Answer

#If we remove teams equally from both the groups, i.e. 1 from each, 2 from each, ..., n from each, then the Gale-Shapley Algorithm can be applied over and over till we have 2 teams left (1 in each group). If the removal of teams is not equal, then there will be a mismatch between the count of group1 and group2 and hence the Gale-Shapley Algorithm won't apply.

#Below I have removed equal number of teams from both the groups and hence Gale Shapley Algorithm works till 2 teams are left (1 from each group)

import random

def stable_matching(group1, group2):
    roundOfEight = []
    semiFinal = []
    finalTeams = []

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

    # First round
    print("Round of 16\n")
    teamOnePair = stableWorldCupRounds(group1, group2)

    for i, num in enumerate(teamOnePair):
        print(teamsInOne[i] + ' vs ' + teamsInTwo[num])
        teamsPaired = [teamsInOne[i], teamsInTwo[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("\n")
        roundOfEight.append(winner)

    random.shuffle(roundOfEight)

    # Second Quarters
    print("Quarter Finals\n")
    quarterFinalsOne = [roundOfEight.pop() for i in range(8) if i < 4]
    quarterFinalsTwo = [roundOfEight.pop() for i in range(4)]
    quartersOneGrouping = {}
    quartersTwoGrouping = {}

    for index, team in enumerate(quarterFinalsOne):
        quartersOneGrouping[index] = team

    for index, team in enumerate(quarterFinalsTwo):
        quartersTwoGrouping[index] = team

    indexes = list(range(4))
    groupOnePreference = []
    groupTwoPreference = []
    for x in range(4):
        shuffledList = random.sample(indexes, len(indexes))
        groupOnePreference.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        groupTwoPreference.append(shuffledList2)

    print("\n")

    team1PairingsForQuarters = stableWorldCupRounds(groupOnePreference, groupTwoPreference)
    for i, num in enumerate(team1PairingsForQuarters):
        print(quartersOneGrouping[i] + ' vs ' + quartersTwoGrouping[num])
        teamsPaired = [quartersOneGrouping[i], quartersTwoGrouping[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("\n")
        semiFinal.append(winner)

    # For Semis
    print("Semi Finals\n")
    groupOneSemis = [semiFinal.pop() for i in range(4) if i < 2]
    groupTwoSemis = [semiFinal.pop() for i in range(2)]

    mappingForGroupOneSemis = {}
    mappingForGroupTwoSemis = {}

    for index, team in enumerate(groupOneSemis):
        mappingForGroupOneSemis[index] = team

    for index, team in enumerate(groupTwoSemis):
        mappingForGroupTwoSemis[index] = team

    indexes = list(range(2))
    preferencesForGroupOneSemis = []
    preferencesForGroupTwoSemis = []

    for x in range(2):
        shuffledList = random.sample(indexes, len(indexes))
        preferencesForGroupOneSemis.append(shuffledList)

        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferencesForGroupTwoSemis.append(shuffledList2)

    print("\n")

    team1PairingsForSemis = stableWorldCupRounds(preferencesForGroupOneSemis, preferencesForGroupTwoSemis)
    for i, num in enumerate(team1PairingsForSemis):
        print(mappingForGroupOneSemis[i] + ' vs ' + mappingForGroupTwoSemis[num])
        teamsPaired = [mappingForGroupOneSemis[i], mappingForGroupTwoSemis[num]]
        winner = random.choice(teamsPaired)
        print("Winner is: " + winner)
        print("\n")
        finalTeams.append(winner)

    print("Finals: " + finalTeams[0] + " vs " + finalTeams[1])


def stableWorldCupRounds(group1, group2):

    n = len(group1)
    unPairedTeams = list(range(n))
    team1Pairings = [None] * n
    team2Pairings = [None] * n
    proposalsMadeMyTeam1 = [0] * n
    while unPairedTeams:
        selectedTeamFromGroup1 = unPairedTeams[0]
        preferencesOfSelectedTeam = group1[selectedTeamFromGroup1]
        oppositionTeamFromGroup2 = preferencesOfSelectedTeam[proposalsMadeMyTeam1[selectedTeamFromGroup1]]
        preferencesOfOppositionTeamGroup2 = group2[oppositionTeamFromGroup2]
        currentPairingOfOppositionTeam = team2Pairings[oppositionTeamFromGroup2]

        if currentPairingOfOppositionTeam is None:
            team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1
            team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2
            proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
            unPairedTeams.pop(0)

        else:
            preferenceNumberOfCurrentPairedTeam = preferencesOfOppositionTeamGroup2.index(
                currentPairingOfOppositionTeam)
            preferenceNumberOfSelectedTeamGroup1 = preferencesOfOppositionTeamGroup2.index(selectedTeamFromGroup1)

            if preferenceNumberOfSelectedTeamGroup1 > preferenceNumberOfCurrentPairedTeam:
                team2Pairings[oppositionTeamFromGroup2] = selectedTeamFromGroup1
                team1Pairings[selectedTeamFromGroup1] = oppositionTeamFromGroup2
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
                unPairedTeams.pop(0)
                unPairedTeams.insert(0, currentPairingOfOppositionTeam)
            else:
                proposalsMadeMyTeam1[selectedTeamFromGroup1] += 1
    return team1Pairings

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

stable_matching(superGroup1, superGroup2)


# reference - https://github.com/Vishal-Kancharla/Gale-Shapley-Algorithm
