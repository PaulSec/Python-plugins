
class Plugin:

    def __init__(self, app):
        app.register_plugin('reverse', self)

    def process(self, string):
        return string[::-1]