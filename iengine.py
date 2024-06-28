import re
from utils import *
from extra import *

def tt_check_all(clauses, alpha, symbols, model):
    if not symbols:#after all the models have been created
        if all(tt_check(clause, model) for clause in clauses):#checks if a clause in KB is true in the truth table model
            return model.get(alpha, False),1#if one of the clauses are true then we check if we can entail alpha from that clause
        else:
            return False, 0
    else:
        P, rest = symbols[0], symbols[1:]
        
        true_model = extend(model, P, True)
        false_model = extend(model, P, False)
        
        result_true, count_true = tt_check_all(clauses, alpha, rest, true_model)#recursively creates all the truth table models for each symbol in the KB 
        result_false, count_false = tt_check_all(clauses, alpha, rest, false_model)
        
        total_count = 0
        if result_true:
            total_count += count_true#total number of models where result is true
        if result_false:
            total_count += count_false#total number of models where result is false
        
        return (result_true or result_false), total_count


def tt_check(clause, model):#returns true for all the symbols in LHS which are true in the truth table model with respect to the value of RHS in the model
    if '=>' in clause:#splits the clause into two if it has '=>'
        LHS, RHS = clause.split('=>')
        LHS = LHS.split('&')
        if isinstance(LHS, list):
            return all(model.get(symbol.strip(), False) for symbol in LHS) <= model.get(RHS.strip(), False)
        else:
            return model.get(LHS.strip(), False) <= model.get(RHS.strip(), False)
    elif '&' in clause:#splits the clause into two if it has '&'
        return all(tt_check(part.strip(), model) for part in clause.split('&'))
    elif '|' in clause:#splits the clause into two if it has '|'
        return any(tt_check(part.strip(), model) for part in clause.split('|'))
    else:
        return model.get(clause.strip(), None)#checks if the symbol is a known fact or a standalone propositional symbol


class InferenceEngine:
    def __init__(self, clauses):
        self.clauses = clauses
        self.symbols = self.get_symbols()

    def get_symbols(self):#returns a list of symbols based on the KB clause provided
        symbols = set()
        for clause in self.clauses:
            symbols.update(re.findall(r'\b[a-zA-Z]\w*', str(clause)))
        return list(symbols)

    def tt_entails(self, alpha):#calls tt_check_all to create the truth table models and check if KB entails alpha 
        symbols = self.symbols
        result, count = tt_check_all(self.clauses, alpha, symbols, {s: None for s in symbols})
        return result, count


    def fc_entails(self, alpha):
        symbols_entailed = []#consists all the symbols which were entailed by the algorithm
        agenda = []#consists all the symbols that are entailed and check them if they are alpha

        def entail_symbol(symbol):#recursive method to entail a symbol
            if symbol in symbols_entailed:
                return True
            for clause in self.clauses:
                if '=>' in clause:
                    LHS, RHS = clause.split('=>')
                    LHS = LHS.split('&')
                    RHS = RHS.strip()
                    if symbol == RHS:
                        if all(entail_symbol(lhs.strip()) for lhs in LHS):
                            symbols_entailed.append(RHS)
                            agenda.append(RHS)
                            return True
            return False

        for clause in self.clauses:#appends all the known facts to the symbols_entailed list and checks if they are alpha or not
            if '=>' not in clause:
                if clause == alpha:
                    symbols_entailed.append(clause.strip())
                    return True, symbols_entailed
                agenda.append(clause.strip())
                symbols_entailed.append(clause.strip())

        while agenda:#while we have some initial known facts about the KB
            p = agenda.pop(0)
            if p == alpha:#we check if we have the first element in agenda is equal to alpha
                return True, symbols_entailed
            for clause in self.clauses:
                if '=>' in clause:
                    LHS, RHS = clause.split('=>')
                    LHS = LHS.split('&')
                    RHS = RHS.strip()
                    if all(entail_symbol(lhs.strip()) for lhs in LHS):#otherwise for each symbol in the LHS of a clause we entail that symbol and check if it is alpha or not
                        if RHS not in symbols_entailed:#if LHS is entailed and RHS is not
                            symbols_entailed.append(RHS)#we can entail RHS
                            agenda.append(RHS)
                            if RHS == alpha:#check if RHS is alpha
                                return True, symbols_entailed

        return alpha in symbols_entailed, symbols_entailed


    def bc_entails(self, alpha):
        symbols_entailed = []

        def entail_symbol(symbol):#recursively checks if the LHS of the clause which has alpha as the RHS can be entailed or not
            if symbol in symbols_entailed:
                return True
            if symbol in [clause.strip() for clause in self.clauses if '=>' not in clause]:
                symbols_entailed.append(symbol)
                return True
            for clause in self.clauses:
                if '=>' in clause:
                    LHS, RHS = clause.split('=>')
                    LHS = LHS.split('&')
                    RHS = RHS.strip()
                    if symbol == RHS:
                        if all(entail_symbol(lhs.strip()) for lhs in LHS):
                            symbols_entailed.append(RHS)
                            return True
            return False

        if entail_symbol(alpha):
            return True, symbols_entailed
        else:
            return False, symbols_entailed
        