import csv
import itertools
import json
from nltk.stem import PorterStemmer
from Tokenizing import IOoperations
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

english_stopwords = stopwords.words('english')


class TicketJson: 
    counter = 0
    global row
    row = 204401
    global KeyRows
    KeyRows =10
    

    def jsonCreator(self,path):    
        csvfile = open(path, 'r')
        reader = csv.DictReader(csvfile)
        out =str(json.dumps( [ row for row in reader ] ))
        return json.loads(out)
      
    
    def KeyGen(self,data,feild):
        stemmer = PorterStemmer()
        arrKeys = []
        
        
        for i in range(0,KeyRows):
                KeysToken=[]
                for token in word_tokenize(data[i][feild]):              
                    stemmed_token =  stemmer.stem(token)       
                    KeysToken.append(stemmed_token.lower())
                arrKeys.append(KeysToken)
        return arrKeys

    def countAppearance(self,keys,SummaryIntoToken):
        arrRowAppeared = []
        global arrRow
        arrRow = []
        arrCount = [0]*len(keys)
        for k in range(0,len(keys)):
            arrRowAppeared[:]=[]
            counter = 0
            i = 0
            while i < len(SummaryIntoToken):
                if (set(keys[k]).issubset(SummaryIntoToken[i]))==True:
                    counter+=1   
                    SummaryIntoToken[i] =  " "
                    indexVal = i
                    #print(indexVal)          
                    arrRowAppeared.append(indexVal)
                    
                newArrRowAppeared = arrRowAppeared[:] 
                i += 1
            
            arrRow.append(newArrRowAppeared)
            arrCount[k]=counter

        #print("arrRow {} ".format(arrRow))
        return arrCount
        
    
    def FinalOut(self, counterValue,FinalKeySet):
        delt = IOoperations.Write()
        delt.DeleteFile()
        get = IOoperations.Write()
        tocsv = get.WriteToCSV
        
        tocsv("Total number of records : {}\n".format(row))
        print("Total number of records {}\n".format(row))
        print(" ")
        tocsv("Keysets,Count,Percent\n")      
        for i in range(0,len(counterValue)):
            a = 1
            a=counterValue[i]
            perc = (a/row)*100   
    
            tocsv(""""{}",{},{}%\n""".format(FinalKeySet[i],counterValue[i],format(perc)))
            print("{} - {} - {}%\n".format(FinalKeySet[i],counterValue[i],format(perc)))      
        return arrRow
    
    
    
    def CreateCategorizedFiles(self,Index):    
        delt = IOoperations.Write()
        delt.DeleteCategorizedFile(len(Index))
                   
        abc = []
        new_list = []
        for i in range(len(Index)):
            new_list = [x+1 for x in Index[i]]
            abc.append(new_list)
            abc[i]=[0] + abc[i]
        #print(abc)# this is the index of the csv file not the row number
    
        toCategorizedcsv = IOoperations.Write()
       
        
        for category in range(len(abc)):
            print(" ")
            
            for l in range(len(abc[category])):            
                i = 0
                the_file = open('C:\\Users\\36474\\Desktop\\ServiceReport1.csv', 'r',50000000)
                reader = csv.reader(the_file)
                for row in reader:
                    if i == abc[category][l]:
                        #print(row)
                        toCategorizedcsv.WriteToCategorizedCSV(row,category)
                        break
                
                    i += 1
                
                the_file.close()          
        print("Ticket Analysis done. Please check the root directory for files ")                    
            
            
        
    
    
















