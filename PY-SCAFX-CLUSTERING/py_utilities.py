# UTILITIES
# ------------------------------------------------------------

import os
from py_constants import T1, T2, T3, T4, T5
from py_constants import C1, C2, C3

def get_printador(features):
    print(features)
    
def get_printador_cab(id_aluno):
    print("\nStudent {}".format(id_aluno))
    print("-------------------------------")
       
def get_migracao(ls_labels):
    print("===============================")
    
    for i in range(0, len(ls_labels[0])):
        print("{} {} {} {} {}".format(i+1, ls_labels[0][i], ls_labels[1][i], ls_labels[2][i], ls_labels[3][i]))
        
def clearOutputCSV(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
        
def outputFilesIdentifier(root_input, root_output, ls_classroom, ls_list, root_tree):
    output_folder = "{}_{}_{}".format(root_output, ls_classroom, ls_list)
    output_tree = "{}/arv-{}-{}.png".format(root_tree, ls_classroom, ls_list)
    output_cluster = "{}/clt-{}-{}.png".format(root_tree, ls_classroom, ls_list)
    input_folder = "{}/{}/{}".format(root_input, ls_classroom, ls_list)
    # ----------------------------------------------------------------
    return (input_folder, output_folder, output_tree, output_cluster)

def mkdirOutputFolder(output_folder):
    if os.path.exists(output_folder):
        print("\n> Folder: {} (ok).".format(output_folder))
    else:
        print("\n> The folder ({}) has been created.".format(output_folder))
        os.mkdir(output_folder)
        
def studentsIdentifier(ls_turma):    
    if ls_turma == C1:
        start_stud = 101
    elif ls_turma == C2:
        start_stud = 201
    elif ls_turma == C3:
        start_stud = 301
    # ---------------------        
    return(start_stud)

def columnsIdentifier(ls_lista):
    
    column_names = {
        T1: ['NF', 'NP', 'NC', 'NR', 'Cluster'],
        T2: ['NPt_s', 'NAdd_s', 'NPt_ds', 'NAdd_ds', 'Cluster'],
        T3: ['NStr', 'NStrM', 'NStrT', 'NStrI', 'NStrC', 'Cluster'],
        T4: ['NFRec', 'NCRec', 'NIFPar', 'NRRec', 'NRNRec', 'Cluster'],
        T5: ['NSizeof', 'NMalloc', 'NFree', 'Cluster']
    }
    ##columns[ls_lista].remove('Cluster')
    #columns[ls_lista].append("Cluster")
    # ---------------------
    return column_names.get(ls_lista, [])


def writeHierarchicalCSV(df, column_names, output_file, dfx):
    # write submissions on CSV
    df = df.reindex(columns=column_names)
    df.to_csv(output_file, mode = 'a', sep = ",")
    # ------------------------------------------  
    # write not-aplication (NA) on CSV
    dfx["Cluster"] = "NA"
    dfx.replace(0,"-").to_csv(output_file, mode = 'a', sep = ",", header=False)