#write in CSV file
#import csv
#data=[
 # ["name" , "roll" , "marks"],
  #["rafa" , 1 , 100],
  #["raha ", 2,  80],
 #]
#with open("new_students.csv" , "w" , newline="") as file :
 #   writer=csv.writer(file)
  #  writer.writerows(data)

#mark_list=[]
#students=[]

#with open("students.csv" ,"r" ) as file :
   # reader= csv.DictReader(file)
 

    #print(reader.fieldnames)
    #for row in reader :
    #  marks=int(row["marks"])
     # students.append((row["name"], marks))
      #mark_list.append(marks)

#avg=sum(mark_list) / len(mark_list)
#print ( "avg ", avg)
#for  name, marks in students :
 #if marks > avg :
  #    print(f"name: {name}" , f"marks: {marks}")

# python file to json file 
import json

student = {
   "name" :" rafa",
   "roll" : 102,
   "marks":80,
   "subjects": ["Math" , "Science" ,"Ënglish"],
   "is_passed" :True

}  
with open(" student.json" ,"w") as file:
   json.dump(student, file, indent= 4)
