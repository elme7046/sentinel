import threading

num = 1
def testfunc(startnumber):
    startnumber = startnumber + 1
    print(startnumber)
    pass
counter = 0
while True:
    print(num)
    
    try:
        threading.Thread(target=testfunc,args=[num]).start()
    except ValueError:
        pass
    counter = counter + 1
    