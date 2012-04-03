import os
import webapp2

from base_handler import BaseHandler

class HomeHandler(BaseHandler):
  def get(self):
    self.template_out('templates/home.html', template_values={
      'hello_world': 'Hello World'
    })

class RevertPostHandler(BaseHandler):
  def post(self):
    id = int(self.request.get('version_id'))

class RobotsTextHandler(BaseHandler):
  def get(self):
    allow = os.environ['HTTP_HOST'] == 'hello_world.appspot.com' # TODO: Change this after copying boilerplate
    self.template_out('html/robots.txt', {'allow': allow})

app = webapp2.WSGIApplication([
  ('/', HomeHandler),
], debug=os.environ['SERVER_SOFTWARE'].startswith('Dev'))