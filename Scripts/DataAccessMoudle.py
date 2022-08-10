import csv_to_DataFrame as DF_Generator
import pandas as pd
import matplotlib.pyplot as plt

cell_ID = "9416"
path_for_no_index = f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_ID}\\data_{cell_ID}_avarage_no_index.csv'
path_for_with_index = f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_ID}\\data_{cell_ID}_avarage_with_index.csv'


df_no_index = DF_Generator.adjust_csv_to_DataFrame(path_for_no_index)
df_with_index = DF_Generator.adjust_csv_to_DataFrame(path_for_with_index)

print(df_no_index)

df_no_index.plot()
plt.show()