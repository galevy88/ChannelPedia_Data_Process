
import os



def Manage_Directories(Dict):
    channel_type = Dict["channel_type"]
    Kv_type = Dict["Kv_type"]
    Kv_sub_type = Dict["Kv_sub_type"]
    temprature = Dict["temprature"]
    cell_id = Dict["cell_id"]

    dir_ls = create_dir_ls(Dict)

    file_path = f'CSV\\{channel_type}\\{Kv_type}\\{Kv_sub_type}\\{temprature}\\{cell_id}'

    if(os.path.exists(file_path)):
        return True

    else:
        open_Directory(dir_ls)
        return False





def open_Directory(dir_ls):
    print(len(dir_ls))
    file_path_channnel_type = f'CSV\\{dir_ls[0]}'
    file_path_Kv_type = f'CSV\\{dir_ls[0]}\\{dir_ls[1]}'
    file_path_Kv_sub_type = f'CSV\\{dir_ls[0]}\\{dir_ls[1]}\\{dir_ls[2]}'
    file_path_temprature = f'CSV\\{dir_ls[0]}\\{dir_ls[1]}\\{dir_ls[2]}\\{dir_ls[3]}'
    file_path_cell_id = f'CSV\\{dir_ls[0]}\\{dir_ls[1]}\\{dir_ls[2]}\\{dir_ls[3]}\\{dir_ls[4]}'
    
    if os.path.exists(file_path_channnel_type):
        pass
    else:
        os.mkdir(file_path_channnel_type)

    if os.path.exists(file_path_Kv_type):
        pass
    else:
        os.mkdir(file_path_Kv_type)

    if os.path.exists(file_path_Kv_sub_type):
        pass
    else:
        os.mkdir(file_path_Kv_sub_type)

    if os.path.exists(file_path_temprature):
        pass
    else:
        os.mkdir(file_path_temprature)

    if os.path.exists(file_path_cell_id):
        pass
    else:
        os.mkdir(file_path_cell_id)



    
def create_dir_ls(Dict):
    channel_type = Dict["channel_type"]
    Kv_type = Dict["Kv_type"]
    Kv_sub_type = Dict["Kv_sub_type"]
    temprature = Dict["temprature"]
    cell_id = Dict["cell_id"]


    dir_ls = []
    dir_ls.append(channel_type)
    dir_ls.append(Kv_type)
    dir_ls.append(Kv_sub_type)
    dir_ls.append(temprature)
    dir_ls.append(cell_id)

    return dir_ls