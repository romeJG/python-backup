items = ('apple','grapes','peach','ewan')
print(items.count('apple')) #counts howmany apples
print(items.index('apple')) #gets the index of apple
set_items = set(items)
items = list(set_items)
print (items)

#dictionaries
d = dict(one=1,two=2,three=3,four=4)
print (d)
v = d.values()
print (v)
if 'one' in d:
    print('one is in there!')
elif 'five' in d:
    print('five is in there!')
print(2 in v)
print('two' in d)

