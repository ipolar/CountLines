#!/usr/bin/env python
#
# Go through a directory (and sub-directories) and count the number of lines in each file.
#
# Usage:
#
# python count_lines.py --path /www/sites/ --ignoreExtensions gif,png,jpg,swf,ttf,pdf
#
# Version:	0.1
# Author:	Andy Lyon
# Date:		22-05-2011
#

import os
import sys

#
# Check which file extensions to ignore...
#
def shouldIgnore(file, extensionsToIgnore):
	for extension in extensionsToIgnore:
		if file[len(extension)*-1:] == extension:
			return True
	
	return False

#
# Entry point
#
if __name__ == "__main__" :
	
	# Initially set our number of lines to zero
	lines = 0
	
	# Initally set the path to the current directory
	path = "."
	
	# Is the 'path' var set?
	if "--path" in sys.argv:
		path = sys.argv[sys.argv.index('--path') + 1]
	
	# Are there any file extensions we should ignore?
	ignoreExtensions = []
	if "--ignoreExtensions" in sys.argv:
		ignoreExtensions = sys.argv[sys.argv.index('--ignoreExtensions') + 1].split(",")
	
	print "Using path: ", path
	
	for root, dirs, files in os.walk(path):
		for file in files:
			# Ignore .SVN files...
			if ".svn" not in root and ".svn" not in file and not shouldIgnore(file, ignoreExtensions):
				pathToFile = os.path.join(root, file)
				foo = open(pathToFile, "r").readlines()
				lines += len(foo)
				print len(foo), " lines in ", pathToFile
			else:
				print "Ignoring ", os.path.join(root, file)
	
	print "Total lines: ", lines