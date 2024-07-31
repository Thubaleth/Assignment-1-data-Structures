#problem 1
f = "fullstackslp"

print(f[0])

print(f[-1])

print(f[4:9])

print(f[-3:12])

print(f[7:10])

#problem 2

l = [3,7,[5,[1,4,"hello"]]]
l[2][1][2] = "goodbye"
print(l[2][1][2])

#problem
d = {"simple key":"hello"}

print(d["simple key"])

d = {"k1":{"k2":"hello"}}
print(d["k1"]["k2"])

d = {"k1":[{"nest_kay":["this is deep",["hello"]]}]}

#problem 4
myList = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,]
new_set = set(myList)
print(new_set)


#problem 5

age = 45
name = "kyle"
print( "my dog name is  {}  and he looks {} years old".format(name,age))