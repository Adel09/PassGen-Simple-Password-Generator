from django.shortcuts import render


import random

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             '1', '2', '3','4','5','6','7','8','9','0', '!', '@', '$', '&', '?']





# Create your views here.



def home(request):
    chars = alphabets
    thepassword = ''
    choices = [10, 11, 12]
    lent = random.choice(choices)
    for x in range(lent):
      thepassword += random.choice(alphabets)
    return render(request, 'gen/index.html', {"password": thepassword})
