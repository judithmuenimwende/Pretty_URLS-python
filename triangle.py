class Triangle:
  base=0
  height=0
  def __init__(self,base,height):
    self.base = base
    self.height = height
  def area(self):
    return self.base * self.height * 0.5



from flask import Flask
from triangle import Triangle
app = Flask(__name__)

@app.route("/triangle/<int:base>/<int:height>")
@app.route("/triangle/<float:base>/<float:height>")
@app.route("/triangle/<int:base>/<float:height>")
@app.route("/triangle/<float:base>/<int:height>")
def triangle(base = 0, height = 0):
  tri = Triangle(base,height)
  return "Area of triangle is {}".format(tri.area())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)