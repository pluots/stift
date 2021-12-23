# stift

An awesome module for executing "safe" functions from strings.

## Parser Module

Parse a string with functions, strings, variables, and arrays. This allows an executor to
construct the response of the string execution.

A tool to use these arguments should start at the end of the returned array (lowest level)
and work upwards. Anything of type "str", "int", or "float" can be used as-is. Anything
with type ParseTypes.array, ParseTypes.function, or ParseTypes.variable need to be processed.

```python
:param s: String to be parsed
:type s: str
:raises ParserError: Issue with parsing somewhere along the line
:return: Returns a nested list of "Token" dictionaries. These always include a value and a type.
For functions, there will also be an argc and argv element (see example)
For arrays, there will also be an index element (See example)
{
    type: ParseTypes.function, # Type can be str, int, float, or a ParseTypes element
    value: "ceiling" # Variable value or function/array name
    argc: 2, # (Functions only) number of arguments
    argv: [(1,2), (1,3)], # (Functions only) pointer to arg locations e.g. parsed[1][2]
}

:rtype: List[List[dict]]
```

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
