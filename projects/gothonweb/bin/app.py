import web

urls = (
  '/', 'Index',
  '/foo', 'foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "G'day mate"
        return render.index(greeting = greeting)
        
class foo(object):
    def GET(self):
        BA = "pity"
        return render.foo(BA = BA)

        
if __name__ == "__main__":
    app.run()