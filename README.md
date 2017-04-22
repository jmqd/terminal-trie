# terminal-trie

## for people annoyed by guis

A trie-based shortcut system for doing things that normally require leaving the terminal.

Goal is to do as much in CLI as possible.

## usage

- right now, usage isn't very convenient. It's still in POC stages.
- generally, I currently do this: alias tt="/path/to/main.py"

### Phase 1 is URL shortcuts.

- open a browser to hackernews: `$ tt hn`
- google search for "sea turtles": `$ tt g sea turtles`
- more features to come...

### Phase 2 might be email, calendar, to-do, etc.


### Phase 3 might be making it into a daemon to save the trie in memory instead of building each time
