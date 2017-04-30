import abc
import util
import subprocess
import logging

class Action(metaclass = abc.ABCMeta):
    def __init__(self, key, config):
        self.config = config
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
            setattr(cls, 'FACTORY_MAP', {i.CONFIG_NAME:i for i in util.get_all_subclasses(cls)})

        return cls.FACTORY_MAP[action_config['action']](key, action_config)


class OpenUrlAction(Action):
    CONFIG_NAME = 'open_url'
    SYSTEM_OPEN_URL = {
            'Darwin': 'open',
            'Linux': 'xdg-open',
            'Windows': 'explorer'
            }

    def __init__(self, key, config):
        super().__init__(key, config)
        self.address = self.config['value']

    def act(self, context):
        try:
            command = [self.SYSTEM_OPEN_URL[context.system], self.address]
            logging.info("Attempting to make call: %s", command)
            subprocess.call(command)
        except Exception as e:
            print("Problem opening that URL. Sorry.")
            raise

class OpenTemplateUrl(OpenUrlAction):
    CONFIG_NAME = 'open_template_url'

    def act(self, context):
        template = self.config['value']
        try:
            format_dict = {parameter:context.args[self.pathlength + i] for i, parameter in enumerate(self.config['ordered_parameters'])}
        except KeyError:
            format_dict = {'VALUE': '+'.join(context.args[self.pathlength:])}
        formatted_address = template.format(**format_dict)
        self.address = formatted_address
        super().act(context)
