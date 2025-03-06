import dask.dataframe as dd

# Read a large CSV file using Dask (replace file with the correct path)
df = dd.read_csv("file.csv")

# Perform a groupby operation in parallel
result = df.groupby("Age").mean().compute()
print(result)
