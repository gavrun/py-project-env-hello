# Python 2 

x = 1
y = 2
print 'x is equal to y: %s' % (x == y)

z = 1
print 'x is equal to z: %s' % (x == z)

names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']

if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
    
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s' % (new_names == names)
