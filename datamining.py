import random



def userlocation(firstname, lastname, street, city, state):
    print(firstname, lastname, street, city, state)
    print("*********************")
    return 'hello'


def companies(listcompanies, n):
    random.seed(42)
    sampledata = random.sample(listcompanies, n)
    return sampledata
    



