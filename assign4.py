import pandas as pd

petal_df= pd.read_csv("Petal_Data.csv")
petal_df = petal_df.drop(petal_df.columns[0], axis=1)

sepal_df = pd.read_csv("Sepal_Data.csv")
sepal_df = sepal_df.drop(sepal_df.columns[0], axis=1)


#A)Combining both datasets
df3 = pd.merge(petal_df,sepal_df, on=["sample_id","species"])
print(df3)

#B)Average 
print("Petal length - Petal Width corr: " + str(df3["petal_length"].corr(df3["petal_width"])))

print("Petal length - Sepal length corr: " + str(df3["petal_length"].corr(df3["sepal_length"])))

print("Petal length - Sepal width corr: " + str(df3["petal_length"].corr(df3["sepal_width"])))

print("Petal Width - Sepal length corr: " + str(df3["petal_width"].corr(df3["sepal_length"])))

print("Petal Width - Sepal width corr: " + str(df3["petal_width"].corr(df3["sepal_width"])))

print("Sepal length - Sepal width corr: " + str(df3["sepal_length"].corr(df3["sepal_width"])))

#C)Average

print("Average: \n" + str(df3.mean(numeric_only=True)))

#D)Median

print("Median: \n " + str(df3.median(numeric_only=True)))

#E)Sd

print("Standard Deviation: \n" + str(df3.std(numeric_only=True)))

#2)
species_df = df3.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].mean()
print(species_df)

"""The calculation of the mean shows that the overall sample mean for petal_length and petal width is 3.75 cm and 1.19 cm, respectively. 
Looking at the mean data by group, it can be seen that the two most similar species are Versicolor and Virginica. 
In terms of petal length, both are above the mean, with a difference of 1.18 cm. On the other hand, regarding petal width, 
those belonging to Versicolor and Virginica are also notably larger, with a difference of 0.64 cm. 
Iris setosa is by far the least similar of the entire group; not only is it farther from the overall mean than the other 
groups in terms of petal length, but also in terms of sepal width."""