
def extendList(val, list=[]):
    list.append(val)
    return list

print(extendList.__defaults__)
list1 = extendList(10)
print(extendList.__defaults__)
list2 = extendList(123,[])
print(extendList.__defaults__)
list3 = extendList('a')
print(extendList.__defaults__)


print(list1) # [10, 'a']
print(list2) # [123]
print(list3) # [10, 'a']
