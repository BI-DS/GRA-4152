##
#  This module defines a class that extends the base Question class.
#

from questions import Question

## A question with multiple choices.
#
class ChoiceQuestion(Question) :
   # Constructs a choice question with no choices.
   def __init__(self) :
      super().__init__()
      self._choices = []

   ## Adds an answer choice to this question.
   #  @param choice the choice to add
   #  @param correct True if this is the correct choice, False otherwise
   #
   def addChoice(self, choice, correct) :
      self._choices.append(choice)
      if correct :
         # Convert len(choices) to string.
         choiceString = str(len(self._choices))
         self.setAnswer(choiceString)
   
   # Override Question.display().
   def display(self) :
      # Display the question text.
      super().display()
      
      # Display the answer choices.
      for i in range(len(self._choices)) :
         choiceNumber = i + 1
         print("%d: %s" % (choiceNumber, self._choices[i]))
            

