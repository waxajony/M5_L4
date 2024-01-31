def xil_usullar_soni(N):

    if N % 2 == 0 or N == 0:
        return 0
    else:
        return 1

with open('INPUT.txt', 'r') as file:
    N = int(file.read())

result = xil_usullar_soni(N)

with open('OUTPUT.txt', 'w') as file:
    file.write(str(result))
