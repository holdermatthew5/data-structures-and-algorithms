import pytest
from repeated_word import first_word, gather, check

def test_gather1():
    assert gather("Once upon a time, there was a brave princess who...") == ['Once', 'upon', 'a', 'time,', 'there', 'was', 'a', 'brave', 'princess', 'who...']

def test_check1():
    assert check('Once') == 'once' and check('time,') == 'time'

def test_first_word1():
    assert first_word("Once upon a time, there was a brave princess who...") == 'a'

def test_gather2():
    print(gather("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")) == ['It', 'was', 'the', 'best', 'of', 'times,', 'it', 'was', 'the', 'worst', 'of', 'times,', 'it', 'was', 'the', 'age', 'of', 'wisdom,', 'it', 'was', 'the', 'age', 'of', 'foolishness,', 'it', 'was', 'the', 'epoch', 'of', 'belief,', 'it', 'was', 'the', 'epoch', 'of', 'incredulity,', 'it', 'was', 'the', 'season', 'of', 'Light,', 'it', 'was', 'the', 'season', 'of', 'Darkness,', 'it', 'was', 'the', 'spring', 'of', 'hope,', 'it', 'was', 'the', 'winter', 'of', 'despair,', 'we', 'had', 'everything', 'before', 'us,', 'we', 'had', 'nothing', 'before', 'us,', 'we', 'were', 'all', 'going', 'direct', 'to', 'Heaven,', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', '–', 'in', 'short,', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period,', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received,', 'for', 'good', 'or', 'for', 'evil,', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only...']

def test_check2():
    assert check('Light,') == 'light'

def test_first_word2():
    assert first_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'

def test_gather3():
    assert gather("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == ['It', 'was', 'a', 'queer,', 'sultry', 'summer,', 'the', 'summer', 'they', 'electrocuted', 'the', 'Rosenbergs,', 'and', 'I', 'didn’t', 'know', 'what', 'I', 'was', 'doing', 'in', 'New', 'York...']

def test_check3():
    assert check('Rosenburgs,') == 'rosenburgs'

def test_first_word3():
    assert first_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == 'summer'