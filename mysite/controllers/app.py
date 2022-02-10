import cherrypy
from models.blog import Blog

class App(object):
    
    def __init__(self, env) -> None:
        self._env = env
    
    def render(self, page, **kwargs):
        keys = {'template': page}
        for key in kwargs:
            keys[key] = kwargs[key]
        tmpl = self._env.get_template('layouts/base.html')    
        return tmpl.render(keys)
    
    @cherrypy.expose
    def index(self):
        return self.render('app/index.html')
    @cherrypy.expose
    def about(self):
        return self.render('app/about.html')
    @cherrypy.expose
    def blog(self):
        posts = Blog().all()
        return self.render('app/blog.html', posts=posts)
    @cherrypy.expose
    def contact(self):
        return self.render('app/contact.html')
    @cherrypy.expose
    def admin(self):
        posts = Blog().all()
        return self.render('app/admin.html', posts=posts)
    @cherrypy.expose
    def create(self):
        return self.render('app/create.html')
    @cherrypy.expose
    def destroy(self, id):
        Blog().remove(id)
        raise cherrypy.HTTPRedirect('/admin')
    @cherrypy.expose
    def store(self, title, category, content, cover):
        cover = 'https://picsum.photos/id/'+cover+'/200'
        blog = Blog()
        blog.new((title, category, cover, content))
        raise cherrypy.HTTPRedirect('/admin')