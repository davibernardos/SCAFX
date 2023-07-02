# UTILITIES
# ------------------------------------------------------------

import os

def get_printador(features):
    print(features)
    
def get_printador_cab(id_aluno):
    print("\nAluno {}".format(id_aluno))
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
    if ls_turma == "T1":
        start_stud = 101
    elif ls_turma == "T2":
        start_stud = 201
    elif ls_turma == "T3":
        start_stud = 301
    # ---------------------        
    return(start_stud)

def columnsIdentifier(ls_lista):    
    if ls_lista == "Lista01":
        column_names = ['NF','NP','NC','NR','Cluster']
    elif ls_lista == "Lista02":
        column_names = ['NPt_s','NAdd_s','NPt_ds','NAdd_ds','Cluster']
    elif ls_lista == "Lista03":
        column_names = ['NStr','NStrM','NStrT','NStrI','NStrC','Cluster'] 
    elif ls_lista == "Lista04":
        column_names = ['NFRec','NCRec','NIFPar','NRRec','NRNRec','Cluster']
    elif ls_lista == "Lista05":
        column_names = ['NSizeof','NMalloc','NFree','Cluster']                
    # ---------------------  
    return(column_names)

def writeHierarchicalCSV(df, column_names, output_file, dfx):
    # write submissions on CSV
    df = df.reindex(columns=column_names)
    df.to_csv(output_file, mode = 'a', sep = ",")
    # ------------------------------------------  
    # write not-aplication (NA) on CSV
    dfx["Cluster"] = "NA"
    dfx.replace(0,"-").to_csv(output_file, mode = 'a', sep = ",", header=False)