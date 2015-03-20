# !/usr/bin/python

import os
#this imports a module that lets me read all of the files within a specific folder later in this code

def build_dict():
    dict = {}
    with open("associated_gene_names.txt") as file:
#build a dictionary using the associated_gene_names.txt file as its input
        for line in file:        
            arr = line.split("\t")
            if len(arr) > 1:
                locus = arr[0].lower()
                associated_gene = arr[1].lower() 
                dict[locus] = associated_gene
    return dict   
#whatever values i'm going to want to call from this dictionary will look up in the locus column
#then it will just spit out whatever value is associated with that locus column entry from the associated_gene column 

for root, dirs, files in os.walk("./transcript_reads",topdown=True):
#reading everything inside the folder transcript_reads
    dict = build_dict()
#creates a dictionary that is comprised of the build_dict() from above 
    with open("garbage.txt","w") as garbagefile:
        garbagefile.truncate()
#creates a file called garbage.txt where some errors will go
#truncate clears out the file every time it's running so that way there aren't duplicates 
    for name in files:
        filename = os.path.join(root, name)
        with open(filename) as file:
        	print "------"+filename+"-------"
        	lines = file.readlines()
        	column_names = lines[0].strip().split("\t")
        	locus_index = column_names.index("locus")
        	TPM_index = column_names.index("TPM")
        	outfilename = os.path.join("./associated_genes","output_"+name)
#within each file that is opened it takes the locus and the TPM columns from the files within transcript_reads
#outfilename section is specifying that the output files from this script will go here with each file being called
#output_name of the original file.txt
        with open(outfilename,"w") as outfile:
            for i,line in enumerate(lines):
        	    if i !=0 and len(lines[i].strip().split("\t"))>=max(locus_index,TPM_index):
#ignore line 0 (column names), makes sure that the index being accessed is within the range of the line
        		    locus = lines[i].strip().split("\t")[locus_index].lower()
        		    TPM = float(lines[i].strip().split("\t")[TPM_index])
#parse the locus and the TPM columns
        		    if locus in dict:  
        		        if TPM > 2 and dict[locus].strip() != "":
        		            associated_gene = dict[locus]
        		            outfile.write(associated_gene)
#look at all of the corresponding locus entries and pull out the locus name is the TPM value is greater than 2
#then use that locus name to lookup the associated gene name in the dictionary function written above
#print out the gene name of that locus with a value into the file output_name of the file.txt
        		    else:
        		        with open("garbage.txt","a") as garbagefile:
        		            garbagefile.write("~~filename:")
        		            garbagefile.write(filename)
        		            garbagefile.write(" ~~locus:")
        		            garbagefile.write(locus) 
        		            garbagefile.write("\n")
#however, sometimes the locus in the single files might not have a corresponding gene name in the dictionary
#if this is the case, print them out into this file called garbage.txt
#this file also includes the name of the file and the locus name so i can later see what "failed"         		        
        
    '''print "---dirs---"
    for name in dirs:
    	print root 
    	print name
        print(os.path.join(root, name))'''
print "END"

    
        
          
    

	