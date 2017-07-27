
import os
import csv
from datetime import datetime

class Write():
        
    def WriteToCategorizedCSV(self,data,csvcategory):
        csvcategory += 1
        FilePath="output_\categorized\Category No {}.csv".format(csvcategory)
        if(os.path.exists(FilePath)):
            file_object = open(FilePath,'a',50000000,newline='')
            writer = csv.writer(file_object)
            writer.writerows([data])
            file_object.close()
        
        else:
            file_object = open(FilePath,'w',50000000, newline='')
            writer = csv.writer(file_object)
            writer.writerows([data])
            file_object.close()
            
    def WriteToCSV(self,data):
        FilePath="output_\CountResult.csv"
        if(os.path.exists(FilePath)):
            file_object = open(FilePath,'a',50000000,newline='')
            file_object.write(data)
            file_object.close()
        else:
            file_object = open(FilePath,'w',newline='')
            file_object.write(data)
            file_object.close()
            
    def DeleteFile(self):
        FilePath = "output_\CountResult.csv"
        if(os.path.exists(FilePath)):
            os.remove(FilePath)
            
                
    def DeleteCategorizedFile(self,csvcategory):   
        csvcategory += 1        
        for i in range (csvcategory):
            FilePath = "output_\categorized\Category No {}.csv".format(i)
            if(os.path.exists(FilePath)):
                os.remove(FilePath)     