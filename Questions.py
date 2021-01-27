qanda = {"1+1=":2,"1+2=":3, "2+2=":4}

class Questions:
    nQuestions = 0
    nCorrect = 0

    def __init__(self, query, correct_answer):
        self.query = query
        self.correctAnswer = correct_answer.upper()


    def check(self, answer):
        if answer == self.correctAnswer:
            print("Correct!")
            Questions.nCorrect += 1
        else:
            print("Incorrect. ")

    def ask(self):
        Questions.nQuestions += 1
        print(self.query)
        answer = input("")
        answer = answer.upper()
        return answer


p1 = Questions("盲目", "Blindness")   #test
p1.check(p1.ask())
#print(Questions.nCorrect, "/", Questions.nQuestions)

# seeing as in the future there may be more than 1 type of question,
#I wanted to have msq inherit the
class MultipleChoiceQuestion(Questions):

    def __init__(self):
        pass

    def msq (self, a, b, c, d, e):
        pass



#recycle bin:

#for i, j in qanda.items():
#    print(i)
#    answer = input("Please type your answer: ")
#    if int(answer) == j:
#        print("Correct!")
#        Questions.nCorrect += 1
#    else:
#        print("Incorrect.")
#        print(answer, j)
#    Questions.nQuestions += 1
#print("Correct answers: ", Questions.nCorrect, "/", Questions.nQuestions)








