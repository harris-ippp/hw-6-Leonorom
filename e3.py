import pandas as pd

from matplotlib import pyplot as plt



df_list = []

for year in range(1924, 2013, 4):
    year = str(year)

    header = pd.read_csv(year +".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df= pd.read_csv( year +".csv", index_col = 0,
            thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year

    df_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

    results = pd.concat(df_list)

    results["Republican Vote Share"] = results["Republican"]/results ["Total Votes Cast"]

graph = results[results.index=="Accomack County"].plot(x="Year", y="Republican Vote Share")
graph.get_figure().savefig('accomack.png')




# df = df.drop('Green', 1)
# df = df.drop('All Others', 1)
# df = df.drop('Blanks', 1)
# df = df.drop('Constitution', 1)
# df = df.drop('Libertarian', 1)


# print(df.ix[1])
# big_df = pd.concat(df_list)
# print(big_df)
