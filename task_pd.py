import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Reza", "Sara", "Amir"],
    "age": [20, 22, 19, 14]
})

# task 1
# print(df)

#  task2
# print(df["name"])

#  task3
# print(df.iloc[2])

#  task4
# print(df.loc[2,"age"])

# Task 2

# df["score"]=[20,18,17]

# print(df)

# df=df.drop("score",axis=1)
# print(df)


# Task 3

# print(df["age"].mean())

# print(df["age"].max())

# print(df["age"].min())

# print(df["age"].sum())


# Task 4


# print(df[df["age"] > 18])

# print(df[df["age"] < 20])

# Task 5

# df = pd.DataFrame({
#     "city": [
#         "Tehran",
#         "Mashhad",
#         "Tehran",
#         "Shiraz",
#         "Mashhad"
#     ]
# })

# un_city = df["city"].unique()
# print(len(un_city))
# print(df["city"].value_counts())

# Task 6

# df = pd.DataFrame({
#     "name": ["Ali", "Reza", "Sara"],
#     "age": [20, None, 19]
# })

# print(df.isnull())
# print(df)

# # df["age"]=df["age"].fillna(0)
# print(df)

# df=df.dropna()
# print(df)


# Task 7
df = pd.DataFrame({
    "name": ["Ali", "Reza", "Sara", "Amir"],
    "city": ["Tehran", "Mashhad", "Tehran", "Shiraz"],
    "score": [20, 18, 17, 19]
})

print("miangin nomre:  ",df["score"].mean())

print("shahr haye yakta:  ",df["city"].unique())

print(df["city"].value_counts())

print(df[df["score"] > 18])

print(df.sort_values("score",ascending=False))
