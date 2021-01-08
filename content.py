class Victorina:
    def __init__(self):
        self.quiz = {}
    def fill_variants(self):
        self.questions = []
        self.answers = []
        with open("tasks", "r") as file:
            for i in range(5):  # Just deleting "\n"
                self.questions.append(file.readline().replace("\n", ''))
        with open("answers", "r") as file:
            for i in range(5):
                self.answers.append(file.readline().replace("\n", ''))
        for round in range(len(self.questions)):
            self.quiz.setdefault(self.questions[round], self.answers[round])

    def accepted_variants(self):  # Removing as in hm.py
        self.answers.remove(self.answers[0])
        self.questions.remove(self.questions[0])
        self.clean()
        for round in range(len(self.questions)):
            self.quiz.setdefault(self.questions[round], self.answers[round])

    def read_lines(self):
        first_que = self.questions[0]
        return first_que

    def create_ask(self, question_to_ask):
        ask = None
        while ask not in range(1, 6):
            ask = int(input(question_to_ask))
        return ask

    def return_answers(self):
        rep = '\t'
        for value in self.quiz.values():
            rep += str(self.answers.index(value)+1) + ") " + value + "\t"
        return rep

    def ask_question(self):
        question = self.read_lines()
        print(question)
        response = self.create_ask(self.return_answers() + "\nChoose the number of answer: ")
        if self.quiz[question] == self.answers[response-1]:
            print("True")
        else:
            print("False")
        self.accepted_variants()

    def clean(self):
        self.quiz = {}

if __name__=='__main__':
    print("You're trying to play this module")
    input("Press Enter to exit")