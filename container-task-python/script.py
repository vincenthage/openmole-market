#!/usr/bin/env python3

import sys

def write_result(result, filepath):
	with open(filepath, 'w') as file:
		file.write(str(result) + "\n")

if len(sys.argv) > 2:
	val = int(sys.argv[1])
	filepath = sys.argv[2]
	write_result(val*2, filepath)
