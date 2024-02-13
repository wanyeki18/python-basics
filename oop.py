class Fruits:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
    def onyesha(self):
        print(f"My favourite fruit is {self.name} and it costs Ksh. {self.price} and its colour is {self.colour}")
myobj=Fruits("Orange", 50, "orange" )
myobj.onyesha()
myobj2=Fruits("Mango", 30, "yellow")
myobj2.onyesha()
myobj3=Fruits("Banana", 10, "yellow" )
myobj3.onyesha()


