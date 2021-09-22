def helloWorld(amount:int=1) -> str:
    for totLines in range(1, amount+1):
        print(str(totLines) + ". Hello World!")

helloWorld(9)