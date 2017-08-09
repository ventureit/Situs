from faker import Factory
import pandas as pd
import random


def create_fake_stuff(fake):
    df = pd.DataFrame(pd.np.empty((2,1)))

    stuff = [fake.name()
        , fake.email()
        , fake.bs()
        , fake.address()
        , fake.city()
        , fake.state()
        , fake.date_time()
        , fake.paragraph()
        , fake.catch_phrase()
        , random.randint(1000, 2000)]

    for i,j in range(0, 10):
        df.loc[i,j] = [stuff[i]]
    print(df)


if __name__ == '__main__':
    fake = Factory.create()
    create_fake_stuff(fake)
