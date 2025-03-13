#!/usr/bin/env python
import sys
 
#sys.stdin = open("mapout.txt","r")
#sys.stdout = open("smapout.txt","w")
A = []
for line in sys.stdin:
  weekday, zone, package_num, client_num = line.strip().split('\t')
  A.append([weekday, zone, package_num, client_num])

sorted_data = sorted(A, key=lambda x: (x[0], x[1]))
for el in sorted_data:
  print("%s\t%s\t%s\t%s" % (el[0], el[1], el[2], el[3]))