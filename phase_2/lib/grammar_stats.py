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
        return text[0].isupper() and text[-1] in ".?!"
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass