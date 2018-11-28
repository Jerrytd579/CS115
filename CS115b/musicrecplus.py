'''
Nov 16, 2018

I pledge my honor that I have abided by the Stevens Honor System

@authors: Reilly Fitzgerald, and Jerry Cheng

usernames: rfitzge2, jcheng15

CS115 - Hw 10

'''

FILE = "musicrecplus.txt"


def main():
    ''' The main recommendation function '''
    userMap = loadUsers(FILE)
    userName = input("Enter your name " + 
    "(put a $ symbol after your name if you wish your preferences to remain private):")
    if userName not in userMap:
        prefs = newPreferences()
        saveUserPreferences(userName, prefs, userMap, FILE)
    menuLoop(userName, userMap)


def menuLoop(userName, userMap):
    while True:
        print("Enter a letter to choose an option:")
        print("e - enter preferences")
        print("r - get recommendations")
        print("p - show most popular artists")
        print("h - how popular is the most popular")
        print("m - which user has the most likes")
        print("q - save and quit")
        decision = input()
        
        if decision == "e":
            prefs = newPreferences()
            saveUserPreferences(userName, prefs, userMap, FILE)
        elif decision == "r":
            prefs = getPreferences(userName, userMap)
            recs = getRecommendations(userName, prefs, userMap)
            printRecs(recs, userName)
            saveUserPreferences(userName, prefs, userMap, FILE)
        elif decision == "p":
                printMostPopularArtists(userMap)
        elif decision == "h":
                print(howPopular(userMap))
        elif decision == "m":
                print(mostLikes(userMap))
        elif decision == "q":
            try:
                saveUserPreferences(userName, prefs, userMap, FILE)
                break
            except:
                break
        else:
            print("Invalid option, try again")
            menuLoop(userName, userMap)



def printRecs(recs, userName):
    '''Print the user's recommendations'''
    if len(recs) == 0:
        print("No recommendations available at this time.")
    else:
        for artist in recs:
            print(artist)


def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    try:
        file = open(fileName, 'r')
    except:
        file = open(fileName, 'w')
        userDict = {}
        file.close()
        return userDict 
    userDict = {}
    for line in file:
        username, artists = line.strip().split(":")
        artist_list = artists.split(",")
        artist_list.sort()
        userDict[username] = artist_list
    file.close()
    return userDict 


def newPreferences():
    '''Asks the system for the user's preferred artists'''
    newPref = input("Enter an artist that you like (Enter to finish):")
    prefs = []
    while newPref != '':
        prefs.append(newPref.strip().title())
        newPref = input("Enter an artist that you like (Enter to finish):")
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getPreferences(userName, userMap):
    if userName in userMap:
        return userMap[userName]
    else:
        return newPreferences()


def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations


def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user and userMap[currUser] != userMap[user] and user[-1] != '$':
            bestScore = score
            bestUser = user
    return bestUser


def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    return list3


def numMatches(list1, list2):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def mostPopularArtists(userMap):
    '''Returns the most popular artist or artists'''
    users = userMap.keys()
    Freqs = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        if user[-1] != '$':
            for artist in userMap[user]:
                if artist in Freqs:
                    popularity_count = Freqs[artist]
                    popularity_count += 1
                    Freqs[artist] = popularity_count
                else:
                    Freqs[artist] = 1
    for artist in Freqs:
        if Freqs[artist] > maxlikes:
            maxlikes = Freqs[artist]

    for artist in Freqs:
        if Freqs[artist] == maxlikes:
            mostpop += [artist]
    return mostpop


def printMostPopularArtists(userMap):
    '''Prints the most popular artist or artists.'''
    mostpop = mostPopularArtists(userMap)
    if len(mostpop) == 1:
        print(str(mostpop[0]))
    else:
        print(str(mostpop))


def howPopular(userMap):
    '''Prints the number of users that like the most popular artist.'''
    users = userMap.keys()
    Freqs = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        if user[-1] != '$':
            for artist in userMap[user]:
                if artist in Freqs:
                    popularity_count = Freqs[artist]
                    popularity_count += 1
                    Freqs[artist] = popularity_count
                else:
                    Freqs[artist] = 1
    for artist in Freqs:
        if Freqs[artist] > maxlikes:
            maxlikes = Freqs[artist]

    for artist in Freqs:
        if Freqs[artist] == maxlikes:
            mostpop += [artist]

    if len(mostpop) > 1 or len(mostpop) == 0:
        print("Sorry, there is no single-most popular artist.")
    else:
        print(str(Freqs[mostpop[0]]))


def mostLikes(userMap):
    '''Finds the user with the most likes
    (assuming they're public) and prints their username and preferences.'''
    users = userMap.keys()
    max = 0
    result = []
    for user in users:
        if len(userMap[user]) > max and user[-1] != '$':
            result = [user]
            max = len(userMap[user])
        if len(userMap[user]) == max and user[-1] != '$' and user not in result:
            result = result + [user] 
    if max == []:
        print('Sorry, no user found')
    else:
        for x in range(len(result)):
            print(result[x])


def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                 "\n"
        file.write(toSave)
    file.close()


if __name__ == "__main__": main()