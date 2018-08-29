#coding:utf-8
#! /usr/bin/python

# 文件操作

import os
import filecmp

def isdir(path):
	return os.path.isdir(path)

def isfile(path):
	return os.path.isfile(path)

def exists(path):
	return os.path.exists(path)

def is_same_file(path1, path2):
	return filecmp.cmp(path1, path2)

def join(path, name):
	return os.path.join(path, name)

def dirandfiles(path):
	folders = []
	files = []
	for name in os.listdir(path):
		subpath = join(path, name)
		if isdir(subpath): 
			folders.append(name)
		elif isfile(subpath):
			files.append(name)
	return (folders, files)