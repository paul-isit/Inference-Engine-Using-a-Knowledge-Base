from iengine import *
from extra import *
class knowledge_base:
    def __init__(self, sentence=None):
        if sentence:
            self.tell(sentence)
        self.clauses = []# contains the KB clauses

    def tell(self, sentence):
        if '||' in sentence:
            sentence = sentence.replace('||', '|')#hardcoding the disjunction symbol 
        converted_horn_sentence = convert_to_horn_form(sentence)#converts the sentence to horn form
        if converted_horn_sentence == None:
            return False, None  #returns false if the sentence cant be converted to horn form
        for sentence in converted_horn_sentence:
            self.clauses.append(sentence)   #appends the sentence to the KB clauses
        
    
    def ask(self, alpha, method):#calls the respective algorithm in iengine.py based on the method
        iengine = InferenceEngine(self.clauses)
        if method == 'TT':
            return iengine.tt_entails(alpha)
        elif method == 'FC':
            return iengine.fc_entails(alpha)
        elif method == 'BC':
            return iengine.bc_entails(alpha)
        

    def get_clauses(self):
        return self.clauses
