from lib.grammar_stats import GrammarStats

"""
Given a valid sentence with a capital letter and a full stop
Returns true
"""
def test_with_valid_sentence():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is correct sentence.")
    assert result == True