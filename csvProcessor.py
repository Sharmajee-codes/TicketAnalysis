
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import Tokenizing.jsonKey

english_stopwords = stopwords.words('english') 
#SummaryIntoTokens =[]
counter = 0
global row
row = 204401

def LenCalc(feild):
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
    return SummaryLength

if __name__ == '__main__':
    
    Selector = Tokenizing.jsonKey.TicketJson()
    Result = Selector.jsonCreator('input_/ServiceReport1.csv')
    SummaryLength = LenCalc("Title")
    Keysjson = Selector.jsonCreator(path='input_/KeySets.csv')   
    KeySets = Selector.KeyGen(Keysjson,"Keys")
    counterValue = Selector.countAppearance(KeySets,SummaryIntoTokens)
    ResultOutput = Selector.FinalOut(counterValue=counterValue,FinalKeySet=KeySets)
    Categorize = Selector.CreateCategorizedFiles(ResultOutput)
                
        