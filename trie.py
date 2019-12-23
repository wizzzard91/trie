class TrieNode:
    """
    Trie node
    """

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 0


class Trie:
    """
    Trie - префиксное дерево
    https://ru.wikipedia.org/wiki/Префиксное_дерево
    Базовая реализация взята тут:
    https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
    """

    def __init__(self):
        self.root = TrieNode('*')
        self.root.counter = 0

    def is_empty(self):
        return not bool(self.root.counter)

    def add(self, word):
        """
        Adding sentence in the trie
        """
        if not word:
            return

        node = self.root
        for char in word:
            # Search for the character among the children:
            node.counter += 1
            if char not in node.children:
                # Adding new child
                next_node = TrieNode(char)
                node.children[char] = next_node
            else:
                next_node = node.children[char]
            node = next_node
        node.counter += 1
        node.word_finished = True

    def delete(self, word):
        """
        Delete word from trie
        """
        if not self.root.counter:
            return False

        node = self.root
        nodes_containing_word = []
        for char in word:
            nodes_containing_word.append(node)
            if char not in node.children:
                return
            else:
                node = node.children[char]
        node.word_finished = False
        node.counter -= 1
        for _node in nodes_containing_word:
            _node.counter -= 1

    def contains_prefixes(self, string: str):
        if not self.root.counter:
            return False

        word = []
        node = self.root
        for char in string:
            # return True if string's substing is word in trie
            if node.word_finished:
                return True, ''.join(word)
            if char not in node.children:
                return False, ''
            else:
                word.append(char)
                node = node.children[char]
        # node.word_finished = True if the string fully loaded to trie
        return node.word_finished, ''.join(word)

    def contains_prefixes_sentence(self, _sentence: str):
        """
        Returns True, if any substring of _sentence is in Trie
        """
        if not self.root.counter:
            return False, ''

        sentence = _sentence.lower()

        for i in range(len(sentence)):
            contains, word = self.contains_prefixes(sentence[i:])
            if contains:
                return True, word
        return False, ''
