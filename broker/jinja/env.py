from jinja2.environment import Environment
from broker.jinja.filters import remove_space

class JinjaEnvironment(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.filters['remove_space'] = remove_space