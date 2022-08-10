from CellMoudle import Cell




class DataGenerator:
    def __init__(self):
        self.cell_list = []
    
    def add_list_of_cells_dict_to_list(self, list_of_Dict):
        for cell_Dict in list_of_Dict:
            self.add_new_cell_to_list(cell_Dict)

    def add_new_cell_to_list(self, cell_payload_Dict):
        cell_object = Cell(cell_payload_Dict)
        self.cell_list.append(cell_object)

    def generate_data_one_time(self, cell_object):
        cell_object.produce_csv_from_nwb()
        cell_object.convert_csv_to_dataFrame_for_all_repetitions()

    def genertae_all_data(self):
        for cell_object in self.cell_list:
            self.generate_data_one_time(cell_object)



List_Cells_Test = [{
"channel_type" : "K",
"Kv_type" : "",
"Kv_sub_type" : "",
"temprature" : "",
"cell_id" : "9412"
},
{
"channel_type" : "K",
"Kv_type" : "",
"Kv_sub_type" : "",
"temprature" : "",
"cell_id" : "9413"
},
{
"channel_type" : "K",
"Kv_type" : "",
"Kv_sub_type" : "",
"temprature" : "",
"cell_id" : "9414"
},
{
"channel_type" : "K",
"Kv_type" : "",
"Kv_sub_type" : "",
"temprature" : "",
"cell_id" : "9416"
}
]


data_generator = DataGenerator()
data_generator.add_list_of_cells_dict_to_list(List_Cells_Test)
data_generator.genertae_all_data()