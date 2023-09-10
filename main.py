from pathlib import Path
import fun
import prod_cod

if __name__ == "__main__":
    entry = input("Please provide the PDB_id or file path: ")
    print_or_save = input("save or print ? ")

    if Path(entry).is_file()==True:
        entry_lis = fun.text_procs(entry)
    elif (len(entry)==4
            and entry[0].isnumeric()==True):
        entry_lis= [entry]
        id_value = entry
    else:
        entry_lis = []
        print("Please provide a valid entry")

    if len(entry_lis)!=0:
        out_put = prod_cod.scrappy_fun(entry_lis)
        if print_or_save.lower()=='print':
            all_one = input("all or one ?: ")
            if all_one.lower() == "all":
                print(out_put)
            else:
                fun.file_save(out_put)
                if 'id_value'  in locals():
                    print(id,fun.pickle_read(id_value))

                else:
                    id_value = input("Please provide the pdb id here from the file only: ")
                    print(fun.pickle_read(id_value))
        else:
            print("Please wait processing and saving your queries in a file")
            fun.file_save(out_put)
            fun.save_data()
    else:
        print(f"your entry is this c--> '{entry}'")

    


        