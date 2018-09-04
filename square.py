class Square:
  side=0
  def __init__(self,side):
    self.side = side
  def area(self):
    return self.side * self.side


# from flask import Flask
# from square import Square
# app = Flask(__name__)

# @app.route("/square/<int:side>")
# @app.route("/square/<float:side>")
# def square(side = 0,):
#   squ = Square(side)
#   return "Area of Square is {}".format(squ.area())
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8080)