my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
t = tuple([(k,v) for k,v in my_dict.iteritems()])
print t
