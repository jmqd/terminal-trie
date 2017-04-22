class Trie(object):
    '''The main Trie object.'''
    def __init__(self):
        '''Takes the text given and creates a Trie.'''
        self.root = Node(None, None, None)

    def get_node(self, keypath):
        node = self.root
        for key in keypath:
            if key not in node.successors:
                return None
            node = node.traverse_to(key)
            #TODO: create a LeafNode type instead of this hack
            if node.value.value.get('is_forced_leaf'): return node
        return node

    def add(self, full_key, value):
        '''Add a word to the Trie.'''
        node = self.root
        for key in full_key.split(' '):
            if key not in node.successors:
                node.add(key, None)
            node = node.traverse_to(key)

        node.value = value

class Node(object):
    '''The nodes, which are characters in the english alphabet, [A-Za-z].'''
    def __init__(self, predecessor, key, value):
        '''Initialize node. Need its predecessor and the char it represents.'''
        self.key = key
        self.value = value
        self.predecessor = predecessor
        self.successors = dict()

    def add(self, key, value):
        self.successors[key] = Node(self, key, value)

    def traverse_to(self, key):
        return self.successors.get(key, None)
