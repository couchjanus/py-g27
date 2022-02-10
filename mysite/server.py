import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

from controllers.app import App

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
global_conf = os.path.join(HTTP_ROOT, 'config/global.conf')

if __name__ == '__main__':
    app_conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/generator':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers':[('Content-Type', 'text/plain')]
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    
    cherrypy.config.update(global_conf)
    env = Environment(loader=FileSystemLoader('views'))
    
    server = App(env)
    cherrypy.tree.mount(server, '/', config=global_conf)
    
    cherrypy.quickstart(server, '/', config=app_conf)