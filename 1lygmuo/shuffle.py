#!/usr/bin/env python
import sys
 
#sys.stdin = open("mapout.txt","r")
#sys.stdout = open("smapout.txt","w")
A = []
for line in sys.stdin:
  route, weight, package_num = line.strip().split('\t')
  A.append([ route, weight, package_num])

sorted_data = sorted(A, key=lambda x: (int(x[0])))
for el in sorted_data:
  print("%s\t%s\t%s" % (el[0], el[1], el[2]))