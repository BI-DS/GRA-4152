##
#  This program shows a simple quiz with two question types.
#

from questions import Question
from choicequestions import ChoiceQuestion

def main() :
   first = Question()
   first.setText("Who was the inventor of Python?")
   first.setAnswer("Guido van Rossum")

   second = ChoiceQuestion()
   second.setText("In which country was the inventor of Python born?")
   second.addChoice("Australia", False)
   second.addChoice("Canada", False)
   second.addChoice("Netherlands", True)
   second.addChoice("United States", False)

   presentQuestion(first)
   presentQuestion(second)

## Presents a question to the user and checks the response.
#  @param q the question
#
def presentQuestion(q) :
   q.display()   # Uses dynamic method lookup.
   response = input("Your answer: ")
   print(q.checkAnswer(response))   # checkAnswer uses dynamic method lookup.
   
# Start the program.
main()

