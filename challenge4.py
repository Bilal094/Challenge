def lovefunc( flower1, flower2 ):
    flw1, flw2 = flower1 % 2, flower2 % 2
    
    return print(True) if flw1 == 1 and flw2 == 0 or flw1 == 0 and flw2 == 1 else print(False)

lovefunc(6,4)