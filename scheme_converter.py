import os
import sys


primers_file = open(sys.argv[1],"r")
tsv_file = open("original_files/nCoV-2019.tsv","r")
bed_file = open("original_files/nCoV-2019.bed","r")
schemes_file = open("original_files/nCoV-2019.scheme.bed","r")

output_tsv= open("nCoV-2019.tsv","w")
output_bed= open("nCoV-2019.bed","w")
output_scheme= open("nCoV-2019.scheme.bed","w") 

all_primers = []
all_info_tsv = []
all_info_bed = []
all_info_scheme = []


for any_p in primers_file:
    aux = any_p.split("\t")
    all_primers.append(aux[0].replace("\n",""))
    all_primers.append(aux[1].replace("\n",""))

#print (all_primers)

for any_tsv in tsv_file:
    aux_tsv = []
    aux = any_tsv.split("\t")
    aux_tsv.append(aux[0])
    aux_tsv.append(aux[1])
    aux_tsv.append(aux[2])
    aux_tsv.append(aux[3])
    aux_tsv.append(aux[4])
    aux_tsv.append(aux[5].replace("\n",""))
    all_info_tsv.append(aux_tsv)
    #print (any_tsv.replace("\n",""))

for any_bed in bed_file:
    aux_bed = []
    aux = any_bed.split("\t")
    aux_bed.append(aux[0])
    aux_bed.append(aux[1])
    aux_bed.append(aux[2])
    aux_bed.append(aux[3])
    aux_bed.append(aux[4])
    aux_bed.append(aux[5].replace("\n",""))
    all_info_bed.append(aux_bed)

    #print (any_tsv.replace("\n",""))
for any_scheme in schemes_file:
    
    all_info_bed.append(any_scheme)
    aux_scheme = []
    aux = any_scheme.split("\t")
    aux_scheme.append(aux[0])
    aux_scheme.append(aux[1])
    aux_scheme.append(aux[2])
    aux_scheme.append(aux[3])
    aux_scheme.append(aux[4].replace("\n",""))
    all_info_scheme.append(aux_scheme)
    
    
    
    #print (any_tsv.replace("\n",""))
side = 0
pairs = 1
#output_tsv.write(str(all_info_tsv[0])+"\n")
output_tsv.write(str(all_info_tsv[0][0])+"\t"+str(all_info_tsv[0][1])+"\t"
      +str(all_info_tsv[0][2])+"\t"+str(all_info_tsv[0][3])+"\t"
      +str(all_info_tsv[0][4])+"\t"+str(all_info_tsv[0][5])+"\n")

####### NEW TSV FILE #######

for any_primers in all_primers:
    for any_tsv in all_info_tsv:
        
        
        if (any_primers == any_tsv[0]):
            if (side<2):
                pairs
            else:
                pairs +=1
                side = 0
            rename=any_tsv[0].split("_")
            new_name=rename[0]+"_"+str(pairs)+"_"+str(rename[2])
            side +=1

            output_tsv.write(str(new_name)+"\t"+str(any_tsv[1])+"\t"+str(any_tsv[2])
                  +"\t"+str(any_tsv[3])+"\t"+str(any_tsv[4])
                   +"\t"+str(any_tsv[5])+"\n")
output_tsv.close()
######## NEW BED FILE ########
      
side = 0
pairs = 1
strands = ""
for any_primers in all_primers:
    for any_bed in all_info_bed:
        
        
        if (any_primers == any_bed[3]):
            if (side<2):
                pairs
            else:
                pairs +=1
                side = 0
            rename=any_bed[3].split("_")
            new_name=rename[0]+"_"+str(pairs)+"_"+str(rename[2])
            side +=1
            if ("LEFT" in new_name):
                 strands = "+"
            if ("RIGHT" in new_name):
                 strands = "-"
            if ( (pairs % 2) == 0 ):
                 output_bed.write(str(any_bed[0])+"\t"+str(any_bed[1])+"\t"+str(any_bed[2])
                  +"\t"+str(new_name)+"\t"+str("nCoV-2019_2")
                   +"\t"+str(strands)+"\n")
            if ( (pairs % 2) == 1 ):            
                 output_bed.write(str(any_bed[0])+"\t"+str(any_bed[1])+"\t"+str(any_bed[2])
                  +"\t"+str(new_name)+"\t"+str("nCoV-2019_1")
                   +"\t"+str(strands)+"\n")
output_bed.close()
          
            
######## NEW SCHEME FILE ########

side = 0
pairs = 1
for any_primers in all_primers:
    for any_scheme in all_info_scheme:
        
        
        if (any_primers == any_scheme[3]):
            if (side<2):
                pairs
            else:
                pairs +=1
                side = 0
            rename=any_scheme[3].split("_")
            new_name=rename[0]+"_"+str(pairs)+"_"+str(rename[2])
            side +=1
            if ( (pairs % 2) == 0 ):
                  output_scheme.write(str(any_scheme[0])+"\t"+str(any_scheme[1])+"\t"+str(any_scheme[2])
                  +"\t"+str(new_name)+"\t"+str("nCoV-2019_2")+"\n")
            if ( (pairs % 2) == 1 ):
                  output_scheme.write(str(any_scheme[0])+"\t"+str(any_scheme[1])+"\t"+str(any_scheme[2])
                  +"\t"+str(new_name)+"\t"+str("nCoV-2019_1")+"\n")

output_scheme.close()

print ("end")
