import os
import sys
import argparse

parser = argparse.ArgumentParser(prog = sys.argv[1] , description = 'Script description goes here')
parser.add_argument("-p", "--path", help = "Path to regression folder" , required = True)
parser.add_argument("-o", "--output",help = "Name of output file", required = True)
args = parser.parse_args()

lib_name = args.path
result = open(args.output,'w+')
list_dir = os.listdir(os.chdir(lib_name))

for name in list_dir:
    path = os.getcwd()
    if os.path.exists(path + '/' + name + '/spyglass/spyglass.html'):
        with open(path + '/' + name + '/spyglass/spyglass.html') as source:
            text = source.read()
            text = text.replace('Change this by directory name', name)
            result.write(text)
    else:
        print('There is not html file in ' + name + ' directory')
