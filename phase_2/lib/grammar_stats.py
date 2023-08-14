import math

class GrammarStats:
    def __init__(self):
        self._text_checked = 0
        self._text_failed = 0
        self._text_passed = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        # return text[0].isupper() and text[-1] in ".?!"

        if text[0].isupper() and text[-1] in ".?!":
            self._text_passed += 1
            return True
        else:
            self._text_failed += 1
            return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        self._text_checked = self._text_passed + self._text_failed
        integer_as_procentage = (self._text_passed / self._text_checked) * 100

        return math.floor(integer_as_procentage)