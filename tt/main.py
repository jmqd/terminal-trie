import sys
import core
import os
import util
import logging

CONFIG_PATH = os.path.expanduser('~/.tt/config.json')
logging.basicConfig(level = logging.INFO)

def main():
    context = core.Context(sys.argv[1:])
    trie_config = util.load_jsonfile(CONFIG_PATH)
    trie = core.make_trie(trie_config)
    node = core.get_node(context, trie)
    action = node.value
    core.perform_action(action, context)

if __name__ == '__main__':
    main()
