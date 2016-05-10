
class Plugin:

    def __init__(self, app):
        app.register_plugin('lowercase', self)

    def process(self, string):
        return string.lower()