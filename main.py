import sys
import os

class PluginManager(object):
    
    def __init__(self):
        self.plugins = {}
        self.load_plugins()


    def load_plugins(self):
        path = "plugins/"

        # Load plugins
        sys.path.insert(0, path)
        for f in os.listdir(path):
            fname, ext = os.path.splitext(f)
            if ext == '.py':
                mod = __import__(fname)
                self.plugins[fname] = mod.Plugin(self)


    def register_plugin(self, plugin_name, instance):
        self.plugins[plugin_name] = instance


    def process(self, value, plugin_name=None):
        if (plugin_name is not None and self.plugins[plugin_name] is not None):
            return {plugin_name: self.plugins[plugin_name].process(value)}
        else:
            res = {}
            for plugin in self.plugins:
                res[plugin] = self.plugins[plugin].process(value)
            return res

instance = PluginManager()
result = instance.process('This is a string', 'lowercase')
print result
result = instance.process('This is a string')
print result