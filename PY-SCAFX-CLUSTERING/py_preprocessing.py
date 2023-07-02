import os
import re

## FAZ A LEITURA DOS CÓDIGOS
#---------------------------------------
def load_file(fname):
    try:
        with open(fname, 'r', encoding='windows-1252') as f:
            text = f.readlines()    
        f.close()
    except UnicodeDecodeError:
        with open(fname, encoding="utf8") as f:
            text = f.readlines()    
        f.close()
    #---------------------------------------
    # remove espaços do inicio e do fim de uma linha 
    # remove os espaços duplicados no meio da linha
    text = [re.sub(r"[\s]{2,}", " ", x).strip() for x in text]
    #---------------------------------------
    # remove quebras de linha
    text = [x for x in text if not x == '']
    #---------------------------------------
    return text
    
def clear_dir(diretorio):
    lixo = ".DS_Store"
    try:
        os.remove(os.path.join(diretorio,lixo))
        print("removed trash: {}".format(diretorio))
    except FileNotFoundError:
        pass

def write_file(fname, texto, cont):
    nome = "{}/a{:02d}.txt".format(fname, cont)
    arq = open(nome, "w")
    arq.write(texto)
    arq.close()
    #print("Arquivo salvo em {}".format(fname))     
    
def write_csv(texto):
    texto_f = ""
    for t in texto:
        texto_f +="{}\n".format(t)
    
    arq = open(output_file, "w")
    arq.write(texto_f.replace("[","").replace("]","").replace(" ", ""))
    arq.close()

def mapear_dir_raiz(root_input):    
    arquivos = [nome for nome in os.listdir(root_input)]
    return sorted(arquivos)

def read_code(database, output_folder):
    lista = []
    for count, file in enumerate(database):
        lista.append(load_file(os.path.join(output_folder,file)))
    return lista

def write_join(lista, cont, output_folder):
    clear_dir(output_folder)
    write_file(output_folder, str(lista), cont)
    
def join_tasks(folder_entrada, output_folder, printador):
    #lista: [[1.c][2.c]] [[1.c][2.c][3.c]]...
    lista = []
    ls_bib = []
    contFiles = 0
    
    clear_dir(folder_entrada)

    # diretorio com o nome do aluno: davi, joao, maria, etc
    dataset = [nome for nome in os.listdir(folder_entrada)]
    dataset = sorted(dataset)

    for cont, cam in enumerate(dataset):
    
        #codes: dataset/nome_do_aluno/
        codes = os.path.join(folder_entrada, cam)
        
        clear_dir(codes)
        
        #files: 1.c, 2.c, 3.c, etc
        files = [nome for nome in os.listdir(codes)]
        files = sorted(files)

        if printador:
            # saida: 0-ericson cesar: ['3.c', '4.C', '1.C', '5.C', '2.C', 'veiculo.c']
            print("{}-{}: {}".format(cont, cam.lower(), files))

        linha = []
        for f in files:
            try:
                contFiles += 1
                linha.append(load_file(os.path.join(codes,f)))
            except UnicodeDecodeError:
                print("\n>>>> {}\n".format(os.path.join(cam,f)))
                
        ls_bib.append(files)
        lista.append(linha)
        write_join(linha, cont, output_folder)

    print(">> Total of source codes: {}".format(contFiles))
    print("------------------------------------------------------------")
    return(lista, ls_bib)

## PEGAR COMENTARIOS
##-------------------------------------------------------------------------------
## INPUT: recebe um código-fonte (formato lista)
## BODY: transforma todos os comentários de linha em "comm-line"
## OUTPUT: retorna um novo código-fonte (formato lista)
## OUTPUT: retorna a contagem de comentários de linha
def removeLineComment(codigo):        
    flag = 1
    lista = []
    count_comm = 0
    textoCC = ""

    for i, frase in enumerate(codigo):
        # O início de linha pode ser uma instrução, por isso é necessário encontrar o ponto exato 
        #em que um comentário começa.
        if "//" in frase:
            count_comm += 1
            for palavra in frase.split(" "):
                #print(">>{}".format(palavra))
                if "//" in palavra[:2]:
                    #lista.append("//comm-line\n")
                    if not textoCC == "":
                        lista.append("{}\n".format(textoCC))
                        textoCC = ""
                    break;
                else:
                    if not textoCC == "":
                        textoCC += " {}".format(palavra)
                    else:
                        textoCC += "{}".format(palavra)
        else:
            lista.append(frase)

    # count_comm: contador de comentários
    return (lista)


## INPUT: recebe um código-fonte (formato lista)
## BODY: transforma todas as linhas de um comentário em bloco em "comm-block"
## OUTPUT: retorna um novo código-fonte (formato lista)
## OUTPUT: retorna a contagem de comentários em bloco
def removeBlockComment(codigo):        
    flag = 1
    lista = []
    count_comm = 0

    for i, frase in enumerate(codigo):
        if flag: 
            # Verificar comentário composto antes de qualquer outra coisa, eles podem se extender por várias linhas.
            # A FLAG faz o controle de quando um bloco de comentários iniciou.
            if "/*" in frase: #??# Um comentário em bloco pode iniciar no meio da linha?
                flag = 0
                count_comm += 1
                #lista.append("/*comm-block*/\n")
            else:
                lista.append(frase)
        if "*/" in frase:
            flag = 1

    # count_comm: contador de comentários
    return (lista)