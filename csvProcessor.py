import Analysis.jsonKey
if __name__ == '__main__':
        Selector = Analysis.jsonKey.TicketJson()
        Result = Selector.jsonCreator('input_/ServiceReport1.csv')
        SummaryLength,SummaryIntoTokens = Selector.LenCalc("Title",Result)
        Keysjson = Selector.jsonCreator(path='input_/KeySets.csv')   
        KeySets = Selector.KeyGen(Keysjson,"Keys")
        counterValue = Selector.countAppearance(KeySets,SummaryIntoTokens)
        ResultOutput = Selector.FinalOut(counterValue=counterValue,FinalKeySet=KeySets)
        Categorize = Selector.CreateCategorizedFiles(ResultOutput)
                    
            