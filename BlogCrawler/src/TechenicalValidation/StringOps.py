import sys
str1 = "title"
str = "(2014-09-04 19:06:27)"
print str1+" "+str.replace("(", "").replace(")","").split(" ")[0].replace("-","_")

print str.split(" ")