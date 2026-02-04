import inflect
p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
           print()
           break
print("Adieu, adieu, to ", end="")# the reason why this was not working is because the line should start at very beggining
if len(names) == 1:

     for n in names:
          print(n)

else:
    output_names = p.join(names)
    print(output_names)


