from nose.tools import *
from ex48.parser import *

def test_match():
	word_list =[('noun', 'bear'), ('verb', 'eat')]
	m = match(word_list,'noun')
	n = match(word_list,'verb')
	assert_equal(m, ('noun', 'bear'))
	assert_equal(n, ('verb', 'eat'))

def test_skip():
	word_list = [('stop', 'the'),('noun', 'bear')]
	skip(word_list,'stop')
	assert_equal(word_list, [('noun', 'bear')])
	
def test_parse_verb():
	word_list = [('verb', 'eat')]
	v = parse_verb(word_list)
	assert_equal(v, ('verb', 'eat'))
	
	wrong_list = [('noun', 'bear')]
	assert_raises(ParserError, parse_verb, wrong_list)

def test_parse_object():
	word_list = [('noun', 'bear')]
	o = parse_object(word_list)
	assert_equal(o, ('noun', 'bear'))
	
	word_list2 = [('direction', 'north')]
	p = parse_object(word_list2)
	assert_equal(p, ('direction', 'north'))
	
	wrong_list = [('verb', 'eat')]
	assert_raises(ParserError, parse_object, wrong_list)
	
def test_parse_subject():
	word_list = [('verb', 'eat'), ('noun', 'honey')]
	s = parse_subject(word_list)
	assert_equal(s, ('noun', 'player'))
	
	word_list2 = [('noun', 'princess'), ('verb', 'faints')]
	t = parse_subject(word_list2)
	assert_equal(t, ('noun', 'princess'))	
	
	wrong_list = [('noun', 'bear'),('noun', 'man')]
	assert_raises(ParserError, parse_verb, wrong_list)
	
def test_parse_sentence():
	word_list = [('stop', 'the'), ('noun', 'bear'), ('verb', 'eats'), ('stop', 'the'), ('noun', 'honey')]
	s = parse_sentence(word_list)
	assert_equal(s.subject, 'bear')
	assert_equal(s.verb, 'eats')
	assert_equal(s.object, 'honey')