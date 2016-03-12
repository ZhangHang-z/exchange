

class BaseRouter(object):
    
    def __init__(self, server, handler):
        self.server = server
        self.HandleClass = handler
        
    def post(self, url, *args):
        pass
    
    def get(self, url, *args):
        pass
    
    
class Router(BaseRouter):
    
    def post(self, url, *args):
        pass 
    
    def get(self, url, *args):
        pass