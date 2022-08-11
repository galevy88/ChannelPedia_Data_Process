
import os
import h5py
import csv
import Directory_Manager

def create_ls():
    ls = []
    for i in range (0,18):
        ls.append(i)
    return ls
    


def generete_csv_from_nwb_file(Dict):

    ls = create_ls()

    channel_type = Dict["channel_type"]
    Kv_type = Dict["Kv_type"]
    Kv_sub_type = Dict["Kv_sub_type"]
    temprature = Dict["temprature"]
    cell_id = Dict["cell_id"]

    if(Directory_Manager.Manage_Directories(Dict)):
        print(f'The Cell: {cell_id}, Already Exist!')
        

    else:
        generete(ls, channel_type, Kv_type, Kv_sub_type, temprature, cell_id)





def generete(ls, channel_type, Kv_type, Kv_sub_type, temprature, cell_id):

    with h5py.File(f'NWB_files\\{cell_id}\\rCell{cell_id}.nwb' , 'r') as hdf:
        repetition1_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition1/data')
        repetition2_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition2/data')
        repetition3_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition3/data')

        

        with open(f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_rep1.csv' , 'w') as csv_rep_1:
            writer = csv.writer(csv_rep_1)
            writer.writerow(ls)
            writer.writerows(repetition1_data)

        with open(f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_rep2.csv' , 'w') as csv_rep_2:
            writer = csv.writer(csv_rep_2)
            writer.writerow(ls)
            writer.writerows(repetition2_data)   

        with open(f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}\\data_{cell_id}_rep3.csv' , 'w') as csv_rep_3:
            writer = csv.writer(csv_rep_3)
            writer.writerow(ls)
            writer.writerows(repetition3_data) 

