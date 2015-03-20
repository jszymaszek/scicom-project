#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import os
#imports operating system module to be able to read the list of files within a directory 

def build_list(filename):
    list = []
    file = open(filename,'r')
    for line in file:
        line = line.strip()
        list.append(line)
    file.close()
    return list

#this builds a function called build_list that takes the input from the directory associated_genes
#it builds a set with them

def get_intersect(listoffilenames):
	flag = 1
	for filename in listoffilenames:
		print filename
		if flag == 1:
			s = set(build_list(filename))
			flag = 0
		s &= set(build_list(filename))
		print '\n'.join(s)
	return s

#this builds a function called get_intersect of all of the filenames set
#starts with a file and it takes the intersection of it with the next file and so forth
#basically takes the intersection of the files in sequence, and joins them together

def build_output(listoffilenames,outputfilename):
    file = open(outputfilename,'w')
    intersect = get_intersect(listoffilenames)
    for i in intersect:
        file.write('%s\n' % i)
    file.close
#taking the output of the get_intersect function and writes it to file

if __name__ == "__main__":
	listoffilenames = []
	for root, dirs, files in os.walk("./associated_genes",topdown=True):
		for name in files:
			filename = os.path.join(root, name)
			listoffilenames.append(filename)
	build_output(listoffilenames,'intersection_of_expressedgenes.txt')
#this uses the main function and os to take all of the files in the folder "associated_genes"
#and uses the list of filenames as the input for this script
#then it builds the output of this script into a file called "intersection of expressed genes
	