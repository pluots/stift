import pprint

from stift.parser import Parser

pp = pprint.PrettyPrinter(indent=4)

p = Parser()

# s = r"""banana(apple,fruit, 1)"""
# parsed = p.parse(s)
# pp.pprint(parsed)

# s = r"""banana(apple,fruit(1,2,"\"yes\" or \"no\"",sauce[0]))"""
# parsed = p.parse(s)
# pp.pprint(parsed)

s = r"""b("a",s[0])"""
parsed = p.parse(s)
pp.pprint(parsed)

print("done")
