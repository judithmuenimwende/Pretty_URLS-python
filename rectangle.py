class Rectangle:
  base=0
  height=0
  def __init__(self,base,height):
    self.base = base
    self.height = height
  def area(self):
    return self.base * self.height

from flask import Flask
from rectangle import Rectangle
app = Flask(__name__)

@app.route("/rectangle/<int:base>/<int:height>")
@app.route("/rectangle/<float:base>/<float:height>")
@app.route("/rectangle/<int:base>/<float:height>")
@app.route("/rectangle/<float:base>/<int:height>")
def rectangle(base = 0, height = 0):
  rec = Rectangle(base,height)
  return "Area of rectangle is {}".format(rec.area())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)