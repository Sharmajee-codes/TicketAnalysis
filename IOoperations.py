
import os
import csv
from datetime import datetime

class Write():
    def Writejson(self, message):
        strFilePath ="..\\Tokenizing\\Health-{}.json".format(datetime.now().strftime('%Y-%m-%d'))
        message = (message)
        #print(strFilePath) 
        if(os.path.exists(strFilePath)):
            file_object = open(strFilePath,'w',50000000)
            file_object.write(message)
            file_object.close()
        else:
            file_object = open(strFilePath,'w',50000000)
            file_object.write(message)
            file_object.close()
    
    def WriteToCategorizedCSV(self,data,csvcategory):
        FilePath="output_\categorized\Category No {}.csv".format(csvcategory)
        if(os.path.exists(FilePath)):
            file_object = open(FilePath,'a',50000000,newline='')
            w = csv.writer(file_object)
            w.writerows([data])
            file_object.close()
        else:
            file_object = open(FilePath,'w',newline='')
            w = csv.writer(file_object)
            w.writerows([data])
            file_object.close()
            
    def WriteToCSV(self,data):
        FilePath="output_\CountResult.csv"
        if(os.path.exists(FilePath)):
            file_object = open(FilePath,'a',20000000,newline='')
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
        for i in range (csvcategory):
            FilePath = "output_\categorized\Category No {}.csv".format(i)
            if(os.path.exists(FilePath)):
                os.remove(FilePath)     