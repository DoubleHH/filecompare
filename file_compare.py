#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
import glob
import re
from sys import argv
import log
import fileutil

IGNORE_FILES = [".DS_Store"]

def compare_folder(path1, path2):
	notfinddirs = []
	path1list = os.walk(path1)
	path1len = len(path1)
	for root, dirs, files in path1list:
		shouldfilter = False
		for filterdir in notfinddirs:
			if len(filterdir) > len(root): continue
			if root[0:len(filterdir)] == filterdir:
				shouldfilter = True
				break
		if shouldfilter: continue

		log.printstr(root)
		# log.printarr(dirs)
		# log.printarr(files)

		path2root = path2 + root[path1len:]
		(dirs2, files2) = fileutil.dirandfiles(path2root)
		notfinds = []
		for d in dirs:
			if d not in dirs2: 
				notfinddirs.append(fileutil.join(root, d))
				log.printstr("FOLDER: [" + d + "] in 1, not in 2", "b_blue")
		for d in dirs2:
			if d not in dirs: 
				notfinddirs.append(fileutil.join(root, d))
				log.printstr("FOLDER: [" + d + "] in 2, not in 1", "b_blue")
		for f in files:
			if f in IGNORE_FILES: continue
			if f not in files2: 
				notfinds.append(f)
				log.printstr("FILE: [" + f + "] in 1, not in 2", "b_cyan")
		for f in files2:
			if f in IGNORE_FILES: continue
			if f not in files: 
				notfinds.append(f)
				log.printstr("FILE: [" + f + "] in 2, not in 1", "b_cyan")
		for f in files:
			if f in IGNORE_FILES: continue
			if f in notfinds: continue
			file2 = fileutil.join(path2root, f)
			file1 = fileutil.join(root, f)
			if fileutil.is_same_file(file1, file2): 
				samedesc = "SAME: [" + f + "]"
				log.printstr(samedesc, "b_yellow")
			else: 
				diffdesc = "DIFF: [" + f + "]"
				log.printstr(diffdesc, "b_red")
	return True

def compare_file(path1, path2):
	return fileutil.is_same_file(path1, path2)

def compare(path1, path2):
	if fileutil.isdir(path1) and fileutil.isdir(path2):
		return compare_folder(path1, path2)
	elif fileutil.isfile(path1) and fileutil.isfile(path2):
		return compare_file(path1, path2)
	return False

if __name__ == '__main__':
    if len(argv) < 3:
    	log.printstr("Parameters error: Usage: python %s path1 path2" % (__file__), "b_red")
    	exit(0)
    path1 = argv[1]
    path2 = argv[2]
    compare(path1, path2)
    