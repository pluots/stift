# stift

An awesome module for parsing strings to functions,

## Parser

The par

### Parser Example

```python
from stift import Parser

s = r"""banana(apple,fruit(1,2,"\"yes\" or \"no\"",sauce[0]"""
parsed = Parser().parse(s)

# Returns the following:
# [
#     [
#         {
#             "type": ParseTypes.function,
#             "value": "b",
#             "argc": 2,
#             "argv": [(1, 0), (1, 1)],
#         }
#     ],
#     [
#         {"type": str, "value": "a"},
#         {"type": ParseTypes.array, "value": "s", "index": (2, 0)},
#     ],
#     [{"type": int, "value": 0}],
# ]
```

## Functions (WIP)
