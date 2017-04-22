import trie
import platform
import sys
import actions

class Context:
    def __init__(self, args):
        self.args = args
        self.system = platform.system()

def make_trie(config):
    shortcut_trie = trie.Trie()
    for k, v in config.get('shortcuts').items():
        shortcut_trie.add(k, actions.Action.factory(k, v))
    return shortcut_trie

def perform_action(action, context):
    try:
        action.act(context)
    except Exception as e:
        print("Encountered an error. Shutting down.")
        print(e)
        sys.exit(1)

def get_node(context, trie):
    node = trie.get_node(context.args)
    if node is None:
        print("That doesn't appear to be a shortcut you've defined.")
        sys.exit(0)
    return node
