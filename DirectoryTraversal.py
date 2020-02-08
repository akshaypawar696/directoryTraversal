from sys import *
import os

def DirectoryWatcher(path):
	flag = os.path.isabs(path)
	if flag == False:
		path=os.path.abspath(path)
	exists = os.path.isdir(path)
	
	if exists:
		for foldername,subfolder,filename in os.walk(path):
			print('current folder is:'+foldername)
			for subf in subfolder:
				print('sub folder of'+foldername+' is:'+subf)
			for filen in filename:
				print('File inside'+foldername+' is:'+filen)		
			print('')
	else:
		print('Invalid path')
print("Application name:"+argv[0])
if(len(argv)!=2):
	print('Invalid number of arguments')
	exit()

DirectoryWatcher(argv[1])



