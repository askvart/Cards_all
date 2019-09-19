import pickle

class Fruits:
    pass

banana = Fruits()

banana.color = 'yellow'
banana.value = 30



filehandler = open("Fruits.obj","wb")
pickle.dump(banana,filehandler)
filehandler.close()


