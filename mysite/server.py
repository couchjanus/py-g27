import os
import cherrypy
from models.blog import Blog

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
global_conf = os.path.join(HTTP_ROOT, 'config/global.conf')

class Server(object):
    @cherrypy.expose
    def index(self):
        return open('./views/index.html')
    @cherrypy.expose
    def about(self):
        return open('./views/about.html')
    @cherrypy.expose
    def blog(self):
        return open('./views/blog.html')
    @cherrypy.expose
    def contact(self):
        return open('./views/contact.html')
    @cherrypy.expose
    def admin(self):
        return open('./views/admin.html')
    @cherrypy.expose
    def store(self, title, category, content, cover):
        cover = 'https://picsum.photos/id/'+cover+'/200'
        blog = Blog()
        blog.new((title, category, content, cover))
        return '<h1>Happy blogging!</h1>'


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
    server = Server()
    cherrypy.tree.mount(server, '/', config=global_conf)
    
    cherrypy.quickstart(server, '/', config=app_conf)