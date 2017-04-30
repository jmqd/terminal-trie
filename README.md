# terminal-trie

### for people annoyed by guis

A shortcut system for doing things quickly via CLI.

__Goal is to do as much in CLI as possible, with short user-defined shortcuts.__

## Usage

Right now, usage isn't very convenient. It's still in POC stages.

However, here's the general guidance:

- Right now, installation is only tested on Mac OS, and assumes UNIX-like system.
- `install.sh` script will make ~/.tt dir and install the runtime there
- Recommend adding this to your `~/.bashrc` or `~/.zshrc`: `alias tt=~/.tt/main.py`
- Use with alfred via defining workflows that invoke tt.
- Use with keepassx (support is coming to quickly retrieve and paste passwords)
- All shortcuts are configurable and extensible by adding to the `config.json` file.

### Phase 1 is URL shortcuts.

- open a browser to hackernews: `$ tt hn`
- google search for "sea turtles": `$ tt g sea turtles`
- more features to come...

### Phase 2 might be email, calendar, to-do, etc.


### Phase 3 might be making it into a daemon to save the trie in memory instead of building each time
