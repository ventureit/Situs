from faker import Factory
import pandas as pd
import numpy as np
import random, decimal
import xlsxwriter


def write_df_to_excel(excelname, dataframename, sheetname):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(excelname + '.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    dataframename.to_excel(writer, sheet_name=sheetname)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def create_fake_stuff(fake):
    df = pd.read_excel('FieldCodeImport.xlsx', sheetname='Code', header=None)
    # df = pd.DataFrame(columns=('name'
    #                            , 'email'
    #                            , 'bs'
    #                            , 'address'
    #                            , 'city'
    #                            , 'state'
    #                            , 'date_time'
    #                            , 'paragraph'
    #                            , 'Conrad'
    #                            , 'randomdata'))

    for i in range(10):
        # df = pd.read_excel('FieldCodeImport.xlsx', sheetname='Field', header=None)
        # stuff = [
        #      random.randint(1, 2)
        #     , fake.name()
        #     , fake.credit_card_number()
        #     , fake.credit_card_number()
        #     , fake.credit_card_number()
        #     , np.random.choice(['Y', 'N'])
        #     , np.random.choice(['Good', 'Okay', 'Poor'])
        #     , random.randint(1950, 2000)
        #     , random.randint(1, 2)
        #     , random.randint(1950, 2000)
        #     , np.random.choice(['Employed', 'Unemployed'])
        # , np.random.choice(['Y', 'N'])
        # , np.random.choice(['Y', 'N'])
        # , np.random.choice(['Low', 'High'])
        # , fake.credit_card_number()
        # , fake.credit_card_number()
        # , np.random.choice(['Y', 'N'])
        # , random.randint(1, 10)
        # , fake.credit_card_number()
        # ]
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
        df.loc[i] = [item for item in stuff]
        print(df)

        write_df_to_excel('FakeDataSheet', df, 'Loan Data')

if __name__ == '__main__':
    fake = Factory.create()
    create_fake_stuff(fake)


