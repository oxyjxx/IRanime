import random

class IRanime():
  
  @property
  def senko_pictures(self):
    try:
      images = random.choice(list(open("iranime/senko_pictures.txt"))
      return images
    except:
      print("IRanime Error")
      return None
