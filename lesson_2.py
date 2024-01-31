
def baholash(baho):
    if baho <= 40:
        return 40 
    elif (baho + 5) % 5 < 3:
        return baho
    else:
        return baho + (5 - (baho + 5) % 5)


with open('INPUT.txt', 'r') as file:
    talaba_bahosi = int(file.read())


yangi_baho = baholash(talaba_bahosi)


with open('OUTPUT.txt', 'w') as file:
    file.write(str(yangi_baho))
