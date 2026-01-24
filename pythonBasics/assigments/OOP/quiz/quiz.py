import requests
import html
from unicodedata import category


class Question:
    def __init__(self, category, question, correctAns):
        self.category = category
        self.questionStr = question
        self.correctAns = correctAns

class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))

        if response.ok:
            # print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1']

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\n Welcome in Quiz \n")
        numCorrectAnswers = 0
        n = 0
        numQuestions = len(self.questionsList)

        while n < numQuestions:
            q = self.questionsList[n]
            print("\nQuestion: " + str(n) + "\n" + q.questionStr + "\n")
            print("Correct Answer: " + str(q.correctAns) + "\n")

            answer = input("Give correct answer? (y/n): ")
            answerBool = False

            if answer.lower() == "y": answerBool = True

            if answerBool == q.correctAns:
                print("Correct Answer!")
                numCorrectAnswers += 1
            else:
                print("Incorrect Answer!")

            n += 1

        print(f"Number of correct answers: {numCorrectAnswers} from {len(self.questionsList)} questions.")

quiz = Quiz(10)
quiz.startQuiz()