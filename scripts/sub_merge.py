import pandas as pd
import os



df = pd.read_csv("../data/curated/house_facilities.csv")

df = df.dropna()

#get the suburb name from address which end by num
df["suburb"] = df["address"].str.extract("(.+?)\d")
df["suburb"] = df["suburb"].str.strip().str.upper()

df1 = pd.read_csv("../data/curated/income_person.csv")
df2 = pd.read_csv("../data/curated/population_by_region.csv")

df1["SA2 NAME"] = df1["SA2 NAME"].str.upper()
df1["suburb"] = df1["SA2 NAME"]

df2["Region"] = df2["Region"].str.upper()
df2["suburb"] = df2["Region"]

#df3 = pd.merge(df, df1, how="left", on="suburb")
#df3 = pd.merge(df3, df2, how="left", on="suburb")

data = []

for i in df.index:
    print(i)
    line = df[df.index==i].values[0]
    for j in df1.index:
        x = df1[df1.index==j].values[0]
        try:
            if line[-1] in x[2]:
                X = line.tolist()+x.tolist()
                data.append(X)
        except:
            pass

DF = pd.DataFrame(data)
DF.columns = df.columns.tolist()+df1.columns.tolist()

DF.to_csv("../data/curated/house_sub_income.csv")

DF = pd.read_csv("../data/curated/house_sub_income.csv")

print(DF.shape)
data = []
for i in DF.index:
    print(i)
    line = DF[DF.index==i].values[0]
    for j in df2.index:
        x = df2[df2.index==j].values[0]
        try:
            if line[14] in x[1]:
                X = line.tolist()+x.tolist()
                data.append(X)
        except:
            pass

DF1 = pd.DataFrame(data)
DF1.columns = DF.columns.tolist()+df2.columns.tolist()

DF1.to_csv("../data/curated/house_sub_income_population.csv")

#df3.to_csv("../data/curated/ab.csv", index=False)
