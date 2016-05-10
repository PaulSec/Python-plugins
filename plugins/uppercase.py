
class Plugin:

    def __init__(self, app):
        app.register_plugin('uppercase', self)

    def process(self, string):
        return string.upper()