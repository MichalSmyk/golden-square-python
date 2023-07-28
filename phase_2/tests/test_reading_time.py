from lib.reading_time import *

"""
Given a text 
It returns how long it takes to read it when 200 words takes one minute
"""
def test_given_zero_words():
    result = reading_time("")
    assert result == 0

"""
Given 100 words
It returns 0.5
"""
def test_given_100_words_returns_time_to_read():
    result = reading_time("The a sun was setting behind the mountains casting a warm golden glow over the landscape Birds chirped their evening songs as they flew back to their nests A gentle breeze rustled the leaves of the trees creating a soothing melody People strolled along the winding paths enjoying the peaceful ambiance Children played in the park their laughter echoing in the air Nearby a stream flowed gently reflecting the colors of the setting sun The scent of blooming flowers filled the air adding to the enchanting atmosphere It was a picturesque evening one that would be cherished in memories forever")
    assert result ==  0.5

"""
Given 200 words 
It returns 1
"""
def test_given_200_words_returns_1():
     result = reading_time("The a sun was setting behind the mountains casting a warm golden glow over the landscape Birds chirped their evening songs as they flew back to their nests A gentle breeze rustled the leaves of the trees creating a soothing melody People strolled along the winding paths enjoying the peaceful ambiance Children played in the park their laughter echoing in the air Nearby a stream flowed gently reflecting the colors of the setting sun The scent of blooming flowers filled the air adding to the enchanting atmosphere It was a picturesque evening one that would be cherished in memories forever The a sun was setting behind the mountains casting a warm golden glow over the landscape Birds chirped their evening songs as they flew back to their nests A gentle breeze rustled the leaves of the trees creating a soothing melody People strolled along the winding paths enjoying the peaceful ambiance Children played in the park their laughter echoing in the air Nearby a stream flowed gently reflecting the colors of the setting sun The scent of blooming flowers filled the air adding to the enchanting atmosphere It was a picturesque evening one that would be cherished in memories forever")
     assert result ==  1