import webapp2
import string
import cgi
import re

form = """
<!DOCTYPE html>
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>
  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;">%s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>
</html>
"""
class Rot13Page(webapp2.RequestHandler):
  def get(self):
    self.response.write(form % '')
  def post(self):
    rot13 = string.maketrans(
      "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
      "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    rot13 = string.translate(self.request.get('text').encode('ascii', 'replace'), rot13)
    self.response.write(form % cgi.escape(rot13))


login_page = """
<!DOCTYPE html>
<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>
  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">Username</td>
          <td><input type="text" name="username" value="%(value_username)s"></td>
          <td class="error">%(error_username)s</td>
        </tr>
        <tr>
          <td class="label">Password</td>
          <td><input type="password" name="password" value=""></td>
          <td class="error">%(error_password)s</td>
        </tr>

        <tr>
          <td class="label">Verify Password</td>
          <td><input type="password" name="verify" value=""></td>
          <td class="error">%(error_verify)s</td>
        </tr>
        <tr>
          <td class="label">Email (optional)</td>
          <td><input type="text" name="email" value="%(value_email)s"></td>
          <td class="error">%(error_email)s</td>
        </tr>
      </table>
      <input type="submit">
    </form>
  </body>
</html>
"""
class SignupPage(webapp2.RequestHandler):
  resp = {
    'value_username': '',
    'value_email': '',
    'error_username': '',
    'error_email': '',
    'error_password': '',
    'error_verify': ''
  }
  def get(self):
    self.response.write(login_page % self.resp)
  def post(self):
    self.resp['value_username'] = self.request.get('username')
    self.resp['value_email'] = self.request.get('email')
    errors = self.resp.copy()

    if (not re.match(r"^[a-zA-Z0-9_-]{3,20}$", self.request.get('username'))):
      errors['error_username'] = "That's not a valid username."
    if (not re.match(r"^.{3,20}$", self.request.get('password'))):
      errors['error_password'] = "That's not a valid password."
    if (self.request.get('password') != self.request.get('verify')):
      errors['error_verify'] = "Your passwords didn't match."
    if (not re.match(r"^[\S]+@[\S]+\.[\S]+$", self.request.get('email'))):
      errors['error_email'] = "That's not a valid email."

    if (errors != self.resp):
      self.response.write(login_page % errors)
    else:
      self.redirect("/unit2/welcome?username="+errors['value_username'])


class WelcomePage(webapp2.RequestHandler):
  def get(self):
    self.response.write("Welcome, " + self.request.get('username'))

app = webapp2.WSGIApplication([
  ('/unit2/rot13', Rot13Page),
  ('/unit2/signup', SignupPage),
  ('/unit2/welcome', WelcomePage)
], debug=True)