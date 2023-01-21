#Sets
#There should only be one copy of an item in a set 

name1 = {"Roger", "Syd"}
name2 = {"Roger"}

intersect = name1 & name2
print(intersect) 

union = name1 | name2 #union
print(union)

diff = name2 - name1
print(diff)

#superset

sup = name1 > name2
print(sup)

print(list(name1))