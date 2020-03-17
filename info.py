# This program assumes that all 5 digits area codes are of 11 digit phone numebers

import pandas as pd
df = pd.read_csv("phonetocountry.csv")

newarr = []

def geographic():
    user_input = input("enter your number")
    if len(user_input) == 13:
        area_code3 = user_input[3:6]
        found = df[df['Area Code'].str.contains(area_code3, na=False)]
        found = (found.loc[found["Area Code"].str.len() == 4])
        newarr.append([user_input, list(found.values)])
        print(newarr)       
    elif len(user_input) == 12:
        area_code3 = user_input[2:5]
        found = df[df['Area Code'].str.contains(area_code3, na=False)]
        newarr.append([user_input, list(found.values)])
        print(found.loc[found["Country"] != "UK"])
    elif len(user_input) == 11:
        area_code5 = user_input[0:5]
        found = df[df['Area Code'].str.contains(area_code5, na=False)]
        if found["Country"].count() == 0:
            print("No info found")
        else:
            newarr.append([user_input, list(found.values)])
            print(newarr)
    elif len(user_input) == 10:
            area_code3 = user_input[0:3]
            found = df[df['Area Code'].str.contains(area_code3, na=False)]
            if found["Country"].count() < 1:
                print("No info found")
            elif found["Country"].count() > 1:
                area_code4 = user_input[0:4]
                found = df[df['Area Code'].str.contains(area_code4, na=False)]
                if found["Country"].count() == 0:
                    found = df[df['Area Code'].str.contains(area_code3, na=False)]
                    if found["Country"].count() > 1:
                        found = found.loc[found["Country"] != "UK"]
                        newarr.append([user_input, list(found.values)])
                        print(newarr)
                else:
                    newarr.append([user_input, list(found.values)])
                    print(newarr)
            elif found["Country"].count() == 1:
                newarr.append([user_input, list(found.values)])
                print(newarr)
    else:
        print("Number should be 10 or 11 digits long")

geographic() 



