import string
import cgi
import os
import re
import webapp2
import jinja2

from google.appengine.ext import db

# including a simple template engine provided by TAs

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


class RotPage(webapp2.RequestHandler):
  def get(self):
    self.response.write(form % '')
  def post(self):
    text = self.request.get('text')
    self.render('rot13.html', text = text.encode('rot13'))

class SignupPage(webapp2.RequestHandler):
  def get(self):
    self.response.write(form % '')
  def post(self):
    rot13 = string.maketrans(
      "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
      "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    rot13 = string.translate(self.request.get('text').encode('ascii', 'replace'), rot13)
    self.response.write(form % cgi.escape(rot13))

app = webapp2.WSGIApplication([
  ('/unit2/rot13', RotPage),
  ('/unit2/signup', SignupPage)
], debug=True)