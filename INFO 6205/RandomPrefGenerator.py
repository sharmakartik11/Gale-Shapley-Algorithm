import random


def randomListGenerator(n):
    indexes = list(range(n))
    preferencesForGroupOne = []
    preferencesForGroupTwo = []
    for x in range(n):
        shuffledList = random.sample(indexes, len(indexes))
        preferencesForGroupOne.append(shuffledList)
        shuffledList2 = random.sample(shuffledList, len(indexes))
        preferencesForGroupTwo.append(shuffledList2)

    print(preferencesForGroupOne)
    print(preferencesForGroupTwo)


randomListGenerator(16)