# Assingment-4_Llerena

This code aims to analyze the physical proportions of the iris dataset using the pandas library. More specifically, “Sepal_Data.csv” and “Petal_Data.csv” were used.



To begin, both CSV files were read as DataFrames, and the first column containing indexes was removed before combining them using `merge()`. The default join type (`inner`) was used, but the `on` argument was specified to define the join condition, in this case `[sample_id, species]`. 



The preprocessed table contained the following columns: sample_id, species, petal_length, petal_width, sepal_length, and sepal_width. Of these, the last four were used to calculate the following metrics: corr(), mean(), median(), and std().



For mean, median, and std, the “numeric_only” parameter was used to perform operations solely on numeric columns. This was done to avoid slicing the first two columns, which are strings. 



Finally, for step 2, `groupby` was used; as its name suggests, it groups the matrix by a certain factor, which in this case was “species.” This was followed by the conclusion reached by comparing this matrix with the other calculated metrics.
