#
# ANALISE DE SCORE DE ALINHAMENTOS MULTIPLOS COM NORMAL D POR SW
#  Este script realiza a gera score do NORMD por slidewindow baseado no FASTA de alinhamentos multiplos.
#  (!)Para utilizar ele e necessario ter instalado no servidor os seguintes programas:
#	** NORMD 1.3 ()
#	** EMBOSS toolkit (http://emboss.sourceforge.net/)

import os
import sys

def getparam(param_name):
    name = False
    for param in sys.argv:
        if (name):
            name = False
            return param
        if (param == param_name):
            name = True
    return False

# Verifica variaveis e armazena para o pipeline.
if (getparam("-h") != False):
    print("Este script realiza a gera score do NORMD por slidewindow baseado no FASTA de alinhamentos multiplos.")
    print(" (!)Para utilizar ele e necessario ter instalado no servidor os seguintes programas:")
    print("     ** NORMD 1.3 ()")
    print("     ** EMBOSS toolkit (http://emboss.sourceforge.net/)")
    print("")
    print("Alguns dos nossos parametros:")
    print(" python SMABSW.py -normd -seqread -swsize -fasta -finalpos")
else:
    # Checa se todos os parametros obrigatorios estao preenchidos
    validateparam = True
    if (getparam("-normd") == False):
        print("(!)Precisa selecionar a pasta ou comando do NORMD")
        validateparam = False
    elif (getparam("-seqread") == False):
        print("(!)Precisa selecionar a pasta ou comando do SeqRead")
        validateparam = False
    elif (getparam("-swsize") == False):
        print("(!)Precisa selecionar o tamanho do slide window")
        validateparam = False
    elif (getparam("-fasta") == False):
        print("(!)Precisa selecionar o arquivo FASTA com multiplos alinhamentos")
        validateparam = False
    elif (getparam("-finalpos") == False):
        print("(!)Precisa selecionar a posicao final do NORMD Score")
        validateparam = False
    elif (getparam("-stepsize") == False):
        print("(!)Precisa selecionar a Step size")
        validateparam = False

    # Se todos os parametros obrigatorios estiverem corretos, executa o pipeline
    if (validateparam):
        param_normd = getparam("-normd")
        param_seqread = getparam("-seqread")
        param_swsize = getparam("-swsize")
        param_fasta = getparam("-fasta")
        param_finalpos = getparam("-finalpos")
        param_stepsize = getparam("-stepsize")

        os.system("rm scores.txt")

        # Gera scores para cara slide windows
        inipos = 0
        endpos = int(param_swsize)
        while (endpos <= int(param_finalpos)):
            os.system("./seqret -auto -stdout -sequence " + param_fasta +
                      " -outseq temp.msf --sbegin " + str(inipos) +" --send "+str(endpos)+" "
                      "-sformat1 fasta -osformat2 msf")

            os.system( param_normd + "/normd temp.msf "+param_normd+"/blosum62.bla 11 1 -v >> scores.txt")

            print ("["+ str(inipos) + "..." + str(endpos) + "][N="+str(param_finalpos)+"]")
            inipos = inipos + int(param_stepsize)
            endpos = endpos + int(param_stepsize)
