#Write a function that returns the total surface area and volume of a box as an array: [area, volume]

#********************************************

def get_size(w, h, d):
     volume = d * w * h
     area = 2*(h * w) + 2*(h * d) + 2*(w * d)
     print((w, h, d),[area,volume])
get_size(10, 10, 10)