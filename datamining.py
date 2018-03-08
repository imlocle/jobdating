import random



def userlocation(firstname, lastname, street, city, state):
    print(firstname, lastname, street, city, state)
    print("*********************")
    return 'hello'


def companies(listcompanies, n):
    random.seed(42)
    sampledata = random.sample(listcompanies, n)
    return sampledata

def scale(twitter):
    scaling_sample = []
    scrape = scrape_twitter.twitter_dataframe(twitter)
    for i in range(100):
        scaling_sample.append(np.random.uniform(-1,2))
    return (scrape - min(scaling_sample))/(max(scaling_sample)-min(scaling_sample))s


