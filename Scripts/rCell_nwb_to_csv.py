
import os
import h5py
import numpy as np
import pandas as pd
import csv




def generete_csv_from_neb_file(Dict):
    ls = []
    for i in range (0,18):
        ls.append(i)
    
    cell_id = Dict["cell_id"]

    with h5py.File(f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\NWB_files\\{cell_id}\\rCell{cell_id}.nwb' , 'r') as hdf:
        repetition1_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition1/data')
        repetition2_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition2/data')
        repetition3_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition3/data')

        os.mkdir(f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_id}')

        with open(f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_id}\\data_{cell_id}_rep1.csv' , 'w') as csv_rep_1:
            writer = csv.writer(csv_rep_1)
            writer.writerow(ls)
            writer.writerows(repetition1_data)

        with open(f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_id}\\data_{cell_id}_rep2.csv' , 'w') as csv_rep_2:
            writer = csv.writer(csv_rep_2)
            writer.writerow(ls)
            writer.writerows(repetition2_data)   

        with open(f'C:\\Users\\galle\\OneDrive\\Desktop\\Project\\Alon Project\\Production\\CSV\\{cell_id}\\data_{cell_id}_rep3.csv' , 'w') as csv_rep_3:
            writer = csv.writer(csv_rep_3)
            writer.writerow(ls)
            writer.writerows(repetition3_data) 





























    # pandas_df1 = pd.DataFrame(np.array(repetition1_data))
    # pandas_df2 = pd.DataFrame(np.array(repetition2_data))
    # pandas_df3 = pd.DataFrame(np.array(repetition3_data))

    # print(pandas_df1.head())
    # print(pandas_df2.head())
    # print(pandas_df3.head())

    




# with h5py.File('C:\\Users\\galle\\OneDrive\\Desktop\\Learning\\Learningh5py\\rCell9416.nwb' , 'r') as hdf:
#     ls = list(hdf.items())
#     # print("List of datasets in this file:\n" , ls)
#     data_acquisition = hdf.get('acquisition')
#     data_acquisition_timeSeries = hdf.get('acquisition/timeseries')
#     data_acquisition_timeSeries_Activation_repetitions = hdf.get('acquisition/timeseries/Activation/repetitions')

#     repetition1 = hdf.get('acquisition/timeseries/Activation/repetitions/repetition1')
#     repetition2 = hdf.get('acquisition/timeseries/Activation/repetitions/repetition2')
#     repetition3 = hdf.get('acquisition/timeseries/Activation/repetitions/repetition3')


#     print(repetition1)
#     print(repetition2)
#     print(repetition3)

    # repetition1_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition1/data')
    # repetition2_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition2/data')
    # repetition3_data = hdf.get('acquisition/timeseries/Activation/repetitions/repetition3/data')



#     print(type(repetition1_data))
#     print(repetition2_data)
#     print(repetition3_data)