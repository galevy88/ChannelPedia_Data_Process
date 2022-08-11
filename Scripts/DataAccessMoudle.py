import csv_to_DataFrame as DF_Generator
import pandas as pd
import matplotlib.pyplot as plt
import os

class DataAccess:

    def __init__(self):
        pass

    def draw_plot_for_avarage(self, Dict):
        channel_type = Dict["channel_type"]
        Kv_type = Dict["Kv_type"]
        Kv_sub_type = Dict["Kv_sub_type"]
        temprature = Dict["temprature"]
        cell_id = Dict["cell_id"]
        
        path_for_no_index = f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_avarage_no_index.csv'
        df_no_index = DF_Generator.adjust_csv_to_DataFrame(path_for_no_index)

        return df_no_index.plot()

    def draw_plot_for_repetition(self, Dict, rep):
        channel_type = Dict["channel_type"]
        Kv_type = Dict["Kv_type"]
        Kv_sub_type = Dict["Kv_sub_type"]
        temprature = Dict["temprature"]
        cell_id = Dict["cell_id"]
        
        path_for_no_index = f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_rep{rep}.csv'
        df_no_index = DF_Generator.adjust_csv_to_DataFrame(path_for_no_index)
        
        return df_no_index.plot()



List_Cells_Test = [{
"channel_type" : "K",
"Kv_type" : "1",
"Kv_sub_type" : "1.1",
"temprature" : "15",
"cell_id" : "9412"
},
{
"channel_type" : "K",
"Kv_type" : "1",
"Kv_sub_type" : "1.1",
"temprature" : "15",
"cell_id" : "9413"
},
{
"channel_type" : "K",
"Kv_type" : "1",
"Kv_sub_type" : "1.1",
"temprature" : "15",
"cell_id" : "9414"
},
{
"channel_type" : "K",
"Kv_type" : "1",
"Kv_sub_type" : "1.1",
"temprature" : "15",
"cell_id" : "9416"
}
]



data_access = DataAccess()

data_access.draw_plot_for_avarage(List_Cells_Test[0])
data_access.draw_plot_for_repetition(List_Cells_Test[0], 1)
data_access.draw_plot_for_repetition(List_Cells_Test[0], 2)
data_access.draw_plot_for_repetition(List_Cells_Test[0], 3)
plt.show()