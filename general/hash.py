import hashlib
result = "udacity"+","+hashlib.sha256("udacity").hexdigest()
print result
print result.split(",")
str = result.split(",")
print "test function"
key,value = result.split(",")
print key 
print value

print "right function"
print str[0]
print str[1]

if str[1] == hashlib.sha256("udacity").hexdigest():
    print "it's right"
else:
    print "wrong"
import hmac

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
    ###Your code here
    return hmac.new(SECRET,s,hashlib.sha256).hexdigest()
def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

print make_secure_val("udacity")

