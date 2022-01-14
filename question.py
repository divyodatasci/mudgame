import random
class Question:
    def __init__(self, querylist, answerlist):
        self.querylist = querylist
        self.answerlist = answerlist
    
    def generateQuestion(self):
        return (random.choice(self.querylist))

    def matchAnswer(self, question, answer):
        question_index = self.querylist.index(question)
        if answer == self.answerlist[question_index]:
            match = True
        else: 
            match = False
        return match


class MultipleChoiceQuestion(Question):

    def __init__(self, querylist, answerlist, optionslist):
        super().__init__(querylist, answerlist)
        self.optionslist = optionslist

    def generateQuestion(self):
        query =  random.choice(self.querylist)
        options = self.optionslist[self.querylist.index(query)]
        print(options)
        print(type(options))
        query_dict ={
            'query': query,
            'option_0': options[0],
            'option_1': options[1],
            'option_2': options[2],
            'option_3': options[3],

        }
        return (query_dict)

    def matchAnswer(self, question, answer):
        return super().matchAnswer(question, answer)