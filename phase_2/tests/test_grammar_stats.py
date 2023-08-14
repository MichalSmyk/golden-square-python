from lib.grammar_stats import GrammarStats


"""
Given a valid sentence with a capital letter and a full stop
Returns true
"""
def test_with_valid_sentence():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    assert result == True

"""
Given a sentence with capital letter but not fill stop or other mark
Returns false 
"""
def test_with_capital_letter_but_no_end_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is incorrect sentence")
    assert result == False

"""
Given a valid sentence with a capital letter and a question mark
Returns true
"""
def test_with_capital_letter_and_question_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence?")
    assert result == True


"""
Given a valid sentence with a capital letter and a exclamation mark
Returns true
"""
def test_with_capital_letter_and_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence!")
    assert result == True

"""
Given a sentence with capittal letter but ends with a coma 
Returns false 
"""
def test_with_capital_letter_but_ending_with_comma():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is incorrect sentence,")
    assert result == False


"""
Given with no capital letter and a full stop
Returns false
"""
def test_with_lower_letter_and_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello, this is incorrect sentence.")
    assert result == False


"""
Given 2 sentences, one good and one wrong
Returns a number 50
"""
def test_given_one_good_and_one_bad_text_returns_fifty():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    result = grammar_stats.check("hello, this is not correct sentence.")
    assert grammar_stats.percentage_good() == 50

"""
Gien 1 good sentence 
Returns 100
"""
def test_one_good_sentence_results_in_one_hundred():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    assert grammar_stats.percentage_good() == 100

"""
Given 3 sentences, two good and one wrong
Returns a number 66
"""
def test_given_one_good_and_one_bad_text_returns_sixtysix():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    result = grammar_stats.check("Hello, this is correct sentence as well.")
    result = grammar_stats.check("hello, this is not correct sentence.")
    assert grammar_stats.percentage_good() == 66

"""
Given 4 sentences, one good and three wrong
Returns a number 25
"""
def test_given_one_good_and_one_bad_text_returns_twentyfive():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    result = grammar_stats.check("Hello, this is not correct sentence")
    result = grammar_stats.check("Hello, this is correct sentence too")
    result = grammar_stats.check("hello, this is not correct sentence as well.")
    assert grammar_stats.percentage_good() == 25