import trie
import json
import platform
import sys
import abc
import subprocess


class Context:
    def __init__(self, args):
        self.args = args
        self.system = platform.system()

class Action(metaclass = abc.ABCMeta):
    def __init__(self, key, config):
        self.value = config
        self.key = key
        self.pathlength = len(self.key.split(' '))

    @abc.abstractmethod
    def act(self, context=None):
        raise SyntaxError("Implement this method in subclasses.")

    @classmethod
    def factory(cls, key, action_config):
        try:
            getattr(cls, 'FACTORY_MAP')
        except Exception as e:
            setattr(cls, 'FACTORY_MAP', {i.CONFIG_NAME:i for i in get_all_subclasses(cls)})

        return cls.FACTORY_MAP[action_config['action']](key, action_config)


class OpenUrlAction(Action):
    CONFIG_NAME = 'open_url'
    SYSTEM_OPEN_URL = {
            'Darwin': 'open',
            'Linux': 'xdg-open',
            'Windows': 'explorer'
            }

    def act(self, context):
        try:
            subprocess.call([self.SYSTEM_OPEN_URL[context.system], self.value['value']])
        except Exception as e:
            print("Problem opening that URL. Sorry.")
            raise

class OpenTemplateUrl(OpenUrlAction):
    CONFIG_NAME = 'open_template_url'

    def act(self, context):
        template = self.value['value']
        injection = ' '.join(context.args[self.pathlength:])
        value = template.format(VALUE = injection)
        self.value['value'] = value
        super().act(context)


def make_trie(config):
    shortcut_trie = trie.Trie()
    for k, v in config.get('shortcuts').items():
        shortcut_trie.add(k, Action.factory(k, v))
    return shortcut_trie


def load_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

def perform_action(action, context):
    try:
        action.act(context)
    except Exception as e:
        print("Encountered an error. Shutting down.")
        print(e)
        sys.exit(1)

def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses
