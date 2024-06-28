import sys
from knowledge_base import * 
from extra import *

def main():
    if len(sys.argv) != 3:
        print("Please follow the following prompt format\nC:> python main.py <filename> <method>")
        return
    filename = sys.argv[1]
    method = sys.argv[2]
    
    with open(filename, 'r') as file:
        lines = file.readlines()

        All_sentences = lines[1].strip()
        KB_sentences = All_sentences.split(';')
        alpha = lines[3].strip()# initializes alpha query
        
        KB = knowledge_base()#creates a Knowledge Base instance
        
        if method == 'TT':# if the user method is TT
            for sentence in KB_sentences:
                if sentence.strip():
                    KB.tell(sentence.strip())#we tell our KB each of the sentences that are available to us
            result, no_of_models = KB.ask(alpha, method)#and ask it if the KB entails alpha
            if result:
                print(f"YES: {no_of_models}")
            else:
                print("NO")
        elif method == 'FC' or method == 'BC':#if the user method is FC or BC
            for sentence in KB_sentences:
                if sentence.strip():
                    KB.tell(sentence.strip())#we tell our KB each of the sentences that are available to us
            result, symbols_entailed = KB.ask(alpha, method)#and ask it if the KB entails alpha
            if result:
                print(f"YES: {', '.join(symbols_entailed)}")
            else:
                print("NO")
        else:
            print("Please enter a valid method. I.e. either TT, FC or BC")
    
if __name__ == '__main__':
    main()