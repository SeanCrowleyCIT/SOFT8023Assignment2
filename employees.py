

#database
employees20 = {
    "A10" : {
        "name": "Emile Smith Rowe",
        "currentSalary" : 50000,
        "overtime" : 5000,
        "leave" : 5,
    },
    "A7" : {
        "name": "Buyako Saka",
        "currentSalary" : 55000,
        "overtime" : 4000,
        "leave" : 4,
    },
    "A35" : {
        "name": "Gabriel Martinelli",
        "currentSalary" : 30000,
        "overtime" : 4500,
        "leave" : 1,
    },
    "A3" : {
        "name": "Kieran Tierney",
        "currentSalary" : 60000,
        "overtime" : 6000,
        "leave" : 9,
    },
    "A5" : {
        "name": "Thomas Partey",
        "currentSalary" : 80000,
        "overtime" : 4000,
        "leave" : 10
    }
}
employees19 = {
    "A10" : {
        "name": "Emile Smith Rowe",
        "currentSalary" : 12000,
        "overtime" : 6000,
        "leave" : 8,
    },
    "A7" : {
        "name": "Buyako Saka",
        "currentSalary" : 55000,
        "overtime" : 2000,
        "leave" : 7,
    },
    "A35" : {
        "name": "Gabriel Martinelli",
        "currentSalary" : 30000,
        "overtime" : 1500,
        "leave" : 8,
    },
    "A3" : {
        "name": "Kieran Tierney",
        "currentSalary" : 40000,
        "overtime" : 2500,
        "leave" : 5,
    },
    "A5" : {
        "name": "Thomas Partey",
        "currentSalary" : 80000,
        "overtime" : 4000,
        "leave" : 3
    }
}
employees18 = {
    "A10" : {
        "name": "Emile Smith Rowe",
        "currentSalary" : 12000,
        "overtime" : 2000,
        "leave" : 9,
    },
    "A7" : {
        "name": "Buyako Saka",
        "currentSalary" : 10000,
        "overtime" : 1500,
        "leave" : 6,
    },
    "A35" : {
        "name": "Gabriel Martinelli",
        "currentSalary" : 30000,
        "overtime" : 400,
        "leave" : 11,
    },
    "A3" : {
        "name": "Kieran Tierney",
        "currentSalary" : 40000,
        "overtime" : 5000,
        "leave" : 3,
    },
    "A5" : {
        "name": "Thomas Partey",
        "currentSalary" : 80000,
        "overtime" : 3000,
        "leave" : 7
    }

}
employees17 = {
    "A10" : {
        "name": "Emile Smith Rowe",
        "currentSalary" : 5000,
        "overtime" : 1000,
        "leave" : 10,
    },
    "A7" : {
        "name": "Buyako Saka",
        "currentSalary" : 5000,
        "overtime" : 1000,
        "leave" : 3,
    },
    "A35" : {
        "name": "Gabriel Martinelli",
        "currentSalary" : 15000,
        "overtime" : 3000,
        "leave" : 9,
    },
    "A3" : {
        "name": "Kieran Tierney",
        "currentSalary" : 40000,
        "overtime" : 4000,
        "leave" : 7,
    },
    "A5" : {
        "name": "Thomas Partey",
        "currentSalary" : 80000,
        "overtime" : 2000,
        "leave" : 3
    }
}


#Functions
def getYear(year):
    if year == "2020":
        return employees20
    elif year == "2019":
        return employees19
    elif year == "2018":
        return employees18
    elif year == "2017":
        return employees17
    else:
        return "Invalid Entry. Please choose year, 2020, 2019, 2018, 2017"

def getTotalSalary(dic, playerID):
    dic = getYear(dic)
    return dic[playerID]['currentSalary']

def getLeaveTaken(dic, playerID):
    dic = getYear(dic)
    return dic[playerID]['leave']

def getTotalSalary(dic, playerID):
    dic = getYear(dic)
    base = dic[playerID]['currentSalary']
    ot = dic[playerID]['overtime']
    total = base + ot
    return total


