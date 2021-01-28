i = 1500
div_5 = []
div_7 = []
while i <= 2700:
    if i % 5 == 0:
        div_5.append(i)
    elif i % 7 == 0:
        div_7.append(i)
    i += 1
print("Divisores de 5 " + str(div_5))
print("Divisores de 7 " + str(div_7))
