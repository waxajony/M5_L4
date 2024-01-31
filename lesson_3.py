def oyinGolibBoLishi(N):
    if N % 2 == 0:
        return "First player"
    else:
        return "Second player"

with open('INPUT.TXT', 'r') as file:
    N = int(file.read(2))

result = oyinGolibBoLishi(N)

with open('OUTPUT.TXT', 'w') as file:
    file.write(result)
