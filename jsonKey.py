import csv
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Analysis import IOoperations
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class TicketJson: 
    global row
    row = 204401
    global KeyRows
    KeyRows =12
    global english_stopwords
    english_stopwords = stopwords.words('english') 
    counter = 0

    def LenCalc(self,feild,Result):
        print("Processing Please wait...")
        stemmer = PorterStemmer()
        token = ""
        i = 0
        global SummaryLength
        global SummaryIntoTokens
        SummaryLength = []
        SummaryIntoTokens = []   
        for i in range(0,row):
            SentenceToken=[]
            for token in word_tokenize(Result[i][feild]):
                if token in english_stopwords or len(token)<2:
    
                    continue               
                stemmed_token =  stemmer.stem(token)       
                SentenceToken.append(stemmed_token.lower())
            SummaryIntoTokens.append(SentenceToken)
            SummaryLength.append(len(SentenceToken))
            
        #print(SummaryIntoTokens)
        return (SummaryLength,SummaryIntoTokens)

    
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
        #print("Total number of records {}\n".format(row))
        #print(" ")
        tocsv("Keysets,Count,Percent\n")      
        for i in range(0,len(counterValue)):
            a = 1
            a=counterValue[i]
            perc = (a/row)*100   
    
            tocsv(""""{}",{},{}%\n""".format(FinalKeySet[i],counterValue[i],format(perc)))
            #print("{} - {} - {}%\n".format(FinalKeySet[i],counterValue[i],format(perc)))      
        return arrRow
    
    
    
    def CreateCategorizedFiles(self,Index):    
        delt = IOoperations.Write()
        delt.DeleteCategorizedFile(len(Index))
        x = []         
        abc = []
        new_list = []
        for i in range(len(Index)):
            new_list = [x+1 for x in Index[i]]
            abc.append(new_list)
            abc[i]=[0] + abc[i]
        #print(abc)# this is the index of the csv file not the row number
        toCategorizedcsv = IOoperations.Write()
        the_file = open('C:\\Users\\36474\\Desktop\\ServiceReport1.csv', 'r',50000000)
        reader = csv.reader(the_file)
        #reader = csv.reader(the_file)#, delimiter='\t')
        my_list = list(reader)
        the_file.close()  
        for category in range(len(abc)):
            i = 0
            for l in range(len(abc[category])):
                toCategorizedcsv.WriteToCategorizedCSV(my_list[abc[category][l]],category)        
        #print("Ticket Analysis done. Please check the root directory for files ")                    
            
            
        
    
    
















