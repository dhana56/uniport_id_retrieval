#Importing the required libraries 
from pathlib import Path
import pickle

#Processing file function
def text_procs(file):
    """Function return pdb_id as list from the file
    :File, file path
    """
    path_1 = Path(r"entry_file_error.txt")
    if path_1.is_file()==True:
        path_1.unlink()
    else:
        pass
    data_lis = []
    for i in open(file):
        if len(i.strip())==4 :
            data_lis.append(i.strip())
        else:
            with open(r"entry_file_error.txt", 'a') as file:
                file.write(i + '\n')
                file.close()
    return data_lis

#Saving the Output file:

def file_save(x):
    """Function create json file
    : x, dictionary as a input
    """
    with open("result.pickle",'wb') as file:
        pickle.dump(x,file)

def pickle_read(x):
    """Function return the entry based uniport details"""

    with open("result.pickle", "rb") as pickle_file:
        loaded_data = pickle.load(pickle_file)
    return loaded_data[x.lower()]

def save_data():
    "Function that save the data in text file"

    with open("result.pickle",'rb') as file:
        loaded = pickle.load(file)
    
    with open("result_output.txt",'w') as file_1:
        file_1.write(str(loaded))

        
    

            

