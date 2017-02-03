#
# SCORING ANALYSES OF MULTIPLE ALIGNMENTS BY NORMD
#  This script make a NORMD score by slide window using a multiple alignment file in FASTA format
#
#  (!)For to use you need to install some softwares:
#	** NORMD 1.3 ()
#	** EMBOSS toolkit (http://emboss.sourceforge.net/)
#   ** Need copy the SEQRET software for the same folder of this script.

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

# Verify if the parameters exists. Case exist show the message.
if (getparam("-h") != False):
    print("This script make a NORMD score by slide window using a multiple alignment file in FASTA format.")
    print(" (!)For to use you need to install some softwares:")
    print("     ** NORMD 1.3 ()")
    print("     ** EMBOSS toolkit (http://emboss.sourceforge.net/)")
    print("     ** Need copy the SEQRET software for the same folder of this script")
    print("")
    print("See the example command:")
    print(" python SMABSW.py -normd -swsize -fasta -finalpos -stepsize")
else:
    #Verify if the mandatory fields is filled.
    validateparam = True
    if (getparam("-normd") == False):
        print("(!)Please select the NORMD folder")
        validateparam = False
    elif (getparam("-swsize") == False):
        print("(!)Please select a slide window number")
        validateparam = False
    elif (getparam("-fasta") == False):
        print("(!)Please select the multiple alignment file in FASTA format")
        validateparam = False
    elif (getparam("-finalpos") == False):
        print("(!)Please select the final position of the alignment")
        validateparam = False
    elif (getparam("-stepsize") == False):
        print("(!)Please select the step size")
        validateparam = False

    # If every parameters is right, continue the pipeline.
    if (validateparam):
        param_normd = getparam("-normd")
        param_swsize = getparam("-swsize")
        param_fasta = getparam("-fasta")
        param_finalpos = getparam("-finalpos")
        param_stepsize = getparam("-stepsize")

        os.system("rm scores.txt")

        # Build the scores by slide window
        inipos = 0
        endpos = int(param_swsize)

        while (endpos <= int(param_finalpos)):

            # Convert the FASTA file in a temporary MSF file with the slide window sequence.
            os.system("./seqret -auto -stdout -sequence " + param_fasta +
                      " -outseq temp.msf --sbegin " + str(inipos) +" --send "+str(endpos)+" "
                      "-sformat1 fasta -osformat2 msf")

            # Run the NORMD for this slide window and save every pontuation in the scores.txt.
            os.system( param_normd + "/normd temp.msf "+param_normd+"/blosum62.bla 11 1 -v >> scores.txt")

            # Show the actual slide window.
            print ("["+ str(inipos) + "..." + str(endpos) + "][N="+str(param_finalpos)+"]")
            inipos = inipos + int(param_stepsize)
            endpos = endpos + int(param_stepsize)

        # Remove the temporary file
        os.system("rm temp.msf")