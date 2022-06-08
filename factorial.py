numar = int(input())
suma = 0
produs = 1
for i in range(1, numar + 1):
    produs *= i
    suma += produs
print("rezultatul este", suma)
