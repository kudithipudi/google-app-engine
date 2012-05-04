import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
#      self.response.out.write('Hello, Samurai!')
      self.response.out.write(self.request.headers['User-Agent'])
	  
class SecondPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, second!')

app = webapp2.WSGIApplication([('/', MainPage),
			       ('/second',SecondPage)],
                              debug=True)