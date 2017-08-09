from faker import Factory
import pandas as pd
import random

def create_fake_stuff(fake):


    df = pd.DataFrame(columns=('name'
        , 'email'
        , 'bs'
        , 'address'
        , 'city'
        , 'state'
        , 'date_time'
        , 'paragraph'
        , 'Conrad'
        ,'randomdata'))
    
    stuff = [fake.name()
        , fake.email()
        , fake.bs()
        , fake.address()
        , fake.city()
        , fake.state()
        , fake.date_time()
        , fake.paragraph()
        , fake.catch_phrase()
        , random.randint(1000,2000)]

    for i in range(10):
            df.loc[i] = [item for item in stuff]
    print(df)

if __name__ == '__main__':
    fake = Factory.create()
    create_fake_stuff(fake)



# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('joshrandom.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()

# fake = Factory.create()
# item = fake.catch_phrase()
# print(isinstance(item, str))
