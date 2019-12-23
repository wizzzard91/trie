# coding=utf8
from trie.trie import Trie
from unittest import TestCase


class TrieTest(TestCase):

    def test_adding_words(self):
        trie = Trie()
        trie.add('кок')
        assert trie.root.counter == 1

        trie.add('кот')
        assert trie.root.counter == 2

        trie.add('коты')
        assert trie.root.counter == 3

        assert trie.root.children['к'].children['о'].children['к'].word_finished is True
        assert trie.root.children['к'].children['о'].children['т'].word_finished is True
        assert trie.root.children['к'].children['о'].children['т'].children['ы'].word_finished is True

    def test_add_empty(self):
        trie = Trie()
        trie.add('')
        assert trie.is_empty() is True

    def test_deleting_words(self):
        trie = Trie()
        trie.add('кот')
        assert trie.root.counter == 1

        trie.add('коты')
        assert trie.root.counter == 2

        trie.delete('кот')
        assert trie.root.counter == 1

        assert trie.root.children['к'].children['о'].children['т'].word_finished is False
        assert trie.root.children['к'].children['о'].children['т'].children['ы'].word_finished is True

    def test_delete_from_empty(self):
        trie = Trie()
        trie.delete('Сложносочиненный')
        assert trie.is_empty() is True

    def test_contains_prefixes(self):
        trie = Trie()
        trie.add('кек')
        trie.add('кок')
        assert trie.contains_prefixes('ко')[0] is False
        assert trie.contains_prefixes('кок')[0] is True
        assert trie.contains_prefixes('кока')[0] is True
        assert trie.contains_prefixes('кока')[1] == 'кок'
        assert trie.contains_prefixes('Коктамышь')[0] is False

    def test_contains_prefixes_sentence(self):
        trie = Trie()
        trie.add('перельман')
        assert trie.contains_prefixes_sentence('Григорий Перельман - светило мировой математики')[0] is True
        assert trie.contains_prefixes_sentence('Лев Ландау - светило мировой физики')[0] is False
