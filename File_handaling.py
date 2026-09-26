import os
import csv
#f=open("demo.txt" ,"rt")
#print(f.read())
#f.close()
#with open("demo.txt", "a") as f:
 #f. write("\n Now it is ")    

#with open("demo.txt") as f:
 #print(f.read())    

#with open("demo.txt", "w") as f:
 #f. write("\n Python easy !! ")    

#with open("demo.txt") as f:
 #print(f.read())    
# create  a file 
#g=open("program.txt" , "x")
#with open( "program.txt" , "w" ) as g :
 
# g.write("hello  new file is created ")
#with open("program.txt" , "r") as g :
# with open( "Myfile.txt" , "a" ) as g :
  #g.write("append")
# print(g.read())
 # delete file
#os.remove("Myfile.txt")
#if file exists or not
#if os.path.exists("rafa.txt"):
 #os.remove("rafa.txt")
#else:
 #print("file doesnot exist")   
# Read csv file
with open("try.csv" , "r") as file :
   reader= csv.reader(file)
   for row in reader:
     print(row)  