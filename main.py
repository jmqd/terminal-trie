import sys
import core

def main():
    path = sys.argv[1:]
    context = core.Context(path)
    config = core.load_config('./config.json')
    trie = core.make_trie(config)
    node = trie.get_node(path)
    action = node.value

    core.perform_action(action, context)

if __name__ == '__main__':
    main()
