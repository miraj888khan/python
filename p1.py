X={"NAME":"ALI","AGE":12}
print(X)
# slicing
b="heeeeeello world"

print(b[2:])

print(b[-5:-2])
a=("hello ,world ,those or Tree")
l=(a.lower())
k=(a.upper())
s=(a.split("o"))
r=(a.replace("o","l"))
print(l)
print(k)
print(s)
print(r)


# format strings

price=12
txt=f"the price is {price +3}"
print(txt)


# escape chararacters in string
another="hi i am \"thomas shelby\" ok?"
# print("hghjgjg\"hi\"bvhgcgf")
print(another)
# confusion
x=3^2
print(x)

# list
l=["apple","banana","orange"]
l.insert(2,"peanut")
l.insert(0,"peanut")
print(l)

# match
day =3
match day:
    case 3:
        print("hi")
    case 1:
        print("itd \"working\"ok")    

for x in range(1,12,2):
    print(x)
