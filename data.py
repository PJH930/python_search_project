import pandas as pd

my_dict = {}

file_name_1 = "python_pj1.xlsx"
file_name_2 = "python_pj2.xlsx"


df_1 = pd.read_excel(file_name_1)
df_2 = pd.read_excel(file_name_2)
df_2_list = []

for i in df_2.values:
    df_2_list.append(str(i[0]))

for i, v in enumerate(df_1.values):
    my_dict[str(v[0])] = df_2_list[i]



