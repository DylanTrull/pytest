import wordcount
import pytest

def test_word_count():
    assert wordcount.wordCount("Yellow dogs are cool") == 4

def test_spaces():
    assert wordcount.wordCount("helloIamaCoolmanNamedJerry") == wordcount.wordCount("Hello")

def test_capitals():
    assert wordcount.wordCount("HELLO I AM JEFF") == wordcount.wordCount("hello i am jeff")

def test_wordCountZero():
    assert wordcount.wordCount("                   ") == 0
