import abc
import util
import subprocess

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
            setattr(cls, 'FACTORY_MAP', {i.CONFIG_NAME:i for i in util.get_all_subclasses(cls)})

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

