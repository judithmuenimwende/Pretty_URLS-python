from flask import Flask
from circle import Circle
app = Flask(__name__)

@app.route("/circle/<int:radius>")
@app.route("/circle/<float:radius>")
def circle(radius = 0,):
  cir = Circle(radius)
  return "Area of circle is {}".format(cir.area())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)