import random
import string
import hashlib

#def make_salt():
#    result = ''.join((random.choice(string.letters) for i in xrange(5)))
#    return result
def make_salt():
        return ''.join(random.choice(string.letters) for x in xrange(5))

# Implement the function valid_pw() that returns True if a user's password 
# # matches its hash. You will need to modify make_pw_hash.
#
def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    value,salt = h.split(",")
    print salt
    if  value == hashlib.sha256(name+pw+salt).hexdigest():
        return True
    return False
h = make_pw_hash('spez', 'hunter2')
print h
print valid_pw('spez', 'hunter2', h)
