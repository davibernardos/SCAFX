## TEXT-BASED FEATURES
####################################################################
def aux_Text_Based_Count(ls_codigo, commands):
    dict_text = {}
    for cmd in commands:
        count = 0
        for frase in ls_codigo:
            if cmd == "if":
                if "if(" in frase or "if (" in frase:
                    count+=1
            elif cmd == "for":
                if "for(" in frase or "for (" in frase:
                    count+=1
            elif cmd in frase:
                count+=1
        dict_text.update({cmd: count})
    return dict_text

## QUALITY-BASED FEATURES
####################################################################
def aux_Contar_LOC(codigo):
    count = 0
    for c in codigo:
        if "" == c:
            count+=1
    return len(codigo)-count

def aux_Contar_NOM(codigo):
    count = 0
    tipo = "void,int,long,float,double,char"

    ## TRATAR: está contando a assinatura da função no inicio do código
    for frase in codigo:
        for t in tipo.split(","):
            if t in frase[0:len(t)] and "(" in frase and ")" in frase:
                count+=1
                break #se encontrar um tipo, pode sair do laço porque não vai ter duas funções na mesma linha
    return count

def aux_Contar_Variaveis(codigo):
    count = 0
    tipo = "int,long,float,double,char"
    
    for frase in codigo:
        for t in tipo.split(","):
            if t in frase[0:len(t)] and not "(" in frase:
                count+=len(frase.split(","))
                break #se encontrar um tipo, pode sair do laço porque não vai ter dois tipos na mesma linha
    return count

def aux_Contar_NOSM(codigo):
    count = 0
    for frase in codigo:
        if "include" in frase:
            count+=1
    return count

def aux_Contar_NOSA(codigo):
    count = 0
    for frase in codigo:
        if "define" in frase:
            count+=1
    return count

def aux_Contar_NOP(codigo):
    count = 0
    tipo = "void,int,long,float,double,char"

    ## TRATAR: está contando a assinatura da função no inicio do código
    for frase in codigo:
        for t in tipo.split(","):
            if t in frase[0:len(t)] and "(" in frase and ")" in frase:
                if not frase[frase.find('(')+1:frase.find(')')-1] == "":
                    count += len(frase.split(","))
                break #se encontrar um tipo, pode sair do laço porque não vai ter duas funções na mesma linha
    return count 


## OUTROS
####################################################################
def aux_Compilar(file):
    caminho = os.path.join(root_input, file)
    os.system('gcc {} -o z-prog 2> z-compilacao.log'.format(caminho))
    print(caminho)
    
    # ver se da para trocar load
    if not Load_File("z-compilacao.log"):
        return 0
    return (sum(x.count(file) for x in Load_File("z-compilacao.log")))
      

def aux_Encontrar_Funcoes(codigo):
    lista = []
    count_sum = 0
    tipo = "void,int,long,float,double,char"
    
    for i, c in enumerate(codigo):
        frase = codigo[i]
        for t in tipo.split(","):
            if t in frase[0:len(t)] and "(" in frase and ")" in frase:
                l = []
                count = 0
                abrefecha = 0
                for linha_func in codigo[i:len(codigo)]:
                    if "{" in linha_func:
                        abrefecha+=1
                    elif "}" in linha_func:
                        abrefecha-=1
                    
                    l.append(linha_func)
                    i+=1 #estou passando as linhas, precisa interar i
                    count+=1
                    
                    if abrefecha == 0:
                        lista.append(l)
                        #print(count)
                        count_sum+=count
                        break ## se abrefecha for zero, terminou a função e vai iniciar outras.
                #print(abrefecha)
                break #já entrou 1x no IF, não precisa testar outros tipos. Voltar para buscar outras funções  
    try:
        return round(count_sum/len(lista),2)
    except:
        return 0
    
def aux_extrair_sqm(ls_codigo):
    dict_quality = {
        'LOC': Contar_LOC(ls_codigo),
        'NOM': Contar_NOM(ls_codigo),
        'MLOC': Encontrar_Funcoes(ls_codigo),
        'NOA': Contar_Variaveis(ls_codigo),
        'NOP': Contar_NOP(ls_codigo),
        'NOSM': Contar_NOSM(ls_codigo),
        'NOSA': Contar_NOSA(ls_codigo),
        'Line-com': Contar_Line_com(ls_codigo),
        'Block-com': Contar_Block_com(ls_codigo)
    }
    return dict_quality