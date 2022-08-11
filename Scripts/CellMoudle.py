from asyncio.windows_events import NULL
from unittest.mock import patch
import csv_to_DataFrame as DF_Generator
import rCell_nwb_to_csv as CSV_Generator
import pandas as pd
import csv

REP1 = 1
REP3 = 4

class Cell:
    
    def __init__(self, cell_payload_Dict):
        self.information_Dict = cell_payload_Dict
        self.rep1_dataFrame = NULL
        self.rep2_dataFrame = NULL
        self.rep3_dataFrame = NULL
        self.all_rep_avarage_dataFrame = NULL
    
    def produce_csv_from_nwb(self):
        CSV_Generator.generete_csv_from_nwb_file(self.information_Dict)

    
    def convert_csv_to_dataFrame_for_all_repetitions(self):

        channel_type = self.information_Dict["channel_type"]
        Kv_type = self.information_Dict["Kv_type"]
        Kv_sub_type = self.information_Dict["Kv_sub_type"]
        temprature = self.information_Dict["temprature"]
        cell_id = self.information_Dict["cell_id"]

        for rep in range(REP1, REP3):
            path = f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_rep{rep}.csv'
            df = DF_Generator.adjust_csv_to_DataFrame(path)
            if rep == 1:
                self.rep1_dataFrame = df
            if rep == 2:
                self.rep2_dataFrame = df
            if rep == 3:
                self.rep3_dataFrame = df
        
        self.calculate_avarage_dataFrame_for_all_rep()
    
    def calculate_avarage_dataFrame_for_all_rep(self):
        df1 = self.rep1_dataFrame
        df2 = self.rep2_dataFrame
        df3 = self.rep3_dataFrame
        data_avarage  = pd.concat([df1, df2, df3]).groupby(level=0).mean()
        # print(data_avarage)
        self.convert_to_csv(data_avarage)

    def convert_to_csv(self, data_avarage):

        channel_type = self.information_Dict["channel_type"]
        Kv_type = self.information_Dict["Kv_type"]
        Kv_sub_type = self.information_Dict["Kv_sub_type"]
        temprature = self.information_Dict["temprature"]
        cell_id = self.information_Dict["cell_id"]

        path = f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}'


        data_avarage.to_csv(f'{path}\\data_{cell_id}_avarage_with_index.csv')
        data_avarage.to_csv(f'{path}\\data_{cell_id}_avarage_no_index.csv', index=False)
