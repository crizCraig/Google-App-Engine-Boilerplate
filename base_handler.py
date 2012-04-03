import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class BaseHandler(webapp2.RequestHandler):
  """Contains convenience and other methods that we generally want access to across all handlers."""
  def out(self, data):
    self.response.out.write(data)

  def get_checkbox(self, name):
    return self.request.get(name) == 'on'

  def set_checkbox(self, checked):
    return 'checked' if checked else ''

  def template_out(self, filename, template_values={}):
    all_template_values = {
      'APP_VERSION': os.environ['CURRENT_VERSION_ID'],
      'HOST': self.request.host,
      'PAGE_URL_FULL': self.request.path_url,
      'QUERY_STRING': self.request.query_string,
      'URL': self.request.url,
      'PATH': self.request.path
    }

    all_template_values.update(template_values)
    template = jinja_environment.get_template(filename)
    self.response.out.write(template.render(all_template_values))