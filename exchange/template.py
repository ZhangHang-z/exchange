from jinja2 import Template

class Render(object):
    def __init__(self, src, **args):
        self.read(src=src)
        template = Template(self.unrender)
        template.render(**args)
    
    def read(self, src):
        with open(src) as f:
            self.unrender = f.read()

