import pandas as pd
import os
import copy
import pdb

from LoadingBar import LoadingBar

class DataPipeline():
    #Will hold all of the data handling functions
    #
    #Each of which will work in conjunction with outer functions to achieve the goal
    #of a seemless transition from one element of the full project to the next

    def __init__(self):
        self.data_dict = {}

    def __del__(self):
        #print("--- DataPipeline Close ---")
        pass

    def test(self):
        #General Testing Function for Initialization
        self.data_dict = copy.deepcopy(self.import_directory_as_dictionary(".\\data\\MDataFiles_Stage1"))
        print(self.data_dict.keys())

    def import_directory_as_dictionary(self, path):
        '''
        Imports a given directory as a dictionary of dataframes for easy access
        '''
        l = LoadingBar()

        output_dict = {}
        l.start_loading_bar("Importing Directory")
        for name in os.listdir(path):
            data_point = self.import_file(os.path.join(path, name))
            output_dict[name] = data_point
            l.update_loading_bar()
        l.end_loading_bar()

        return output_dict

    def import_file(self, file_path):
        '''
        Imports and individual file via a file path
        '''
        return pd.read_csv(file_path)
