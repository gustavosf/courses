import webapp2
import string
import cgi

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


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.write(form % '')
  def post(self):
    rot13 = string.maketrans(
      "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
      "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    rot13 = string.translate(self.request.get('text').encode('ascii', 'replace'), rot13)
    self.response.write(form % cgi.escape(rot13))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)