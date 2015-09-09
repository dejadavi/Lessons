name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % round((height * 2.54),2)
print "He's %r pounds heavy." % round((weight * 0.453592),2)
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r."  % (
age, round(height * 2.54,2), round(weight * 0.453592,2), round(age + height * 2.54 + weight * 0.453592,2))