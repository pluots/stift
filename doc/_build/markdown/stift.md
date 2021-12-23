# stift package

## Submodules

## stift.compiles module

compiles.py

Compiled regex statements

## stift.exceptions module

exceptions.py

Custom exception classes


### exception stift.exceptions.ParserError()
Bases: `Exception`

Some error parsing a function string.

## stift.parser module


### class stift.parser.ParseTypes()
Bases: `object`


#### array( = 'array')

#### function( = 'function')

#### variable( = 'variable')

### class stift.parser.Parser(s=None)
Bases: `object`

Class used to parse strings with functions, array elements, strings, and variables.

The main method is “parse”


#### \__init__(s=None)

#### create_token()
Add a token to the current level.


* **Return type**

    `None`



#### property current_token(: stift.parser.Token)
Return the currently active token


* **Return type**

    `Token`



#### decrease_level()
Decrease the depth level and set index properly.


* **Return type**

    `None`



#### decrease_token_index()
Decrease token index, nothing special.


* **Return type**

    `None`



#### dump_tokens()
Go through two levels of nesting to get a dict.


* **Return type**

    `list`



#### finalize_current_token(identifier=False)
Convert numeric values if possible. Also verify identifiers


* **Return type**

    `None`



#### increase_level()
Add an empty level and set us to that depth.


* **Return type**

    `None`



#### increase_token_index()
Increase token index, nothing special.


* **Return type**

    `None`



#### property parent_token(: stift.parser.Token)
Return parent token if it exists. Otherwise, create one with no type.


* **Return type**

    `Token`



#### parse(s)
Parse a string with functions, strings, variables, and arrays.

A tool to use these arguments should start at the end of the returned array (lowest level)
and work upwards. Anything of type “str”, “int”, or “float” can be used as-is.


* **Parameters**

    **s** (*str*) – String to be parsed



* **Raises**

    **ParserError** – Issue with parsing somewhere along the line



* **Returns**

    Returns a nested list of “Token” dictionaries. These always include a value and a type.
    For functions, there will also be an argc and argv element (see example)
    For arrays, there will also be an index element (See example)
    {

    > type: ParseTypes.function,  # Type can be str, int, float, or a ParseTypes element
    > value: “ceiling”            # Variable value or function/array name
    > argc: 2,                    # (Functions only) number of arguments
    > argv: [(1,2), (1,3)],       # (Functions only) pointer to arg locations e.g. parsed[1][2]

    }




* **Return type**

    List[List[dict]]



### class stift.parser.Token(type='variable')
Bases: `object`

A token member of a perser.


#### \__init__(type='variable')

#### set_val(val)

* **Return type**

    `None`



#### to_dict()

* **Return type**

    `dict`


## stift.stift module


### class stift.stift.BaseFunction()
Bases: `object`


#### check_types()
Check arg types. If len arg_types = 1, all args must be of that type


#### eval()
This function will evaluate a portion of another function.


#### init(\*args)

### class stift.stift.Ceiling()
Bases: `stift.stift.BaseFunction`


#### arg_counts( = (1, 2))

#### arg_types()
alias of `Union`[`int`, `float`]


#### process()

* **Return type**

    `Union`[`int`, `float`]



### class stift.stift.Coalesce()
Bases: `stift.stift.BaseFunction`

Not technically a spreadsheet function, but possibly very useful


### class stift.stift.Concatenate()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Floor()
Bases: `stift.stift.BaseFunction`


#### arg_counts( = (1, 2))

#### arg_types()
alias of `Union`[`int`, `float`]


#### process()

* **Return type**

    `Union`[`int`, `float`]



### class stift.stift.Hour()
Bases: `stift.stift.BaseFunction`


### class stift.stift.If()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Len()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Minute()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Month()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Round()
Bases: `stift.stift.BaseFunction`


#### arg_counts( = (1, 2))

#### arg_types()
alias of `Union`[`int`, `float`]


#### process()

* **Return type**

    `Union`[`int`, `float`]



### class stift.stift.Stift(s, allowed_variables=None)
Bases: `object`

Parent class.


#### \__init__(s, allowed_variables=None)

#### add_function()

#### function_cls_map( = {'sum': <class 'stift.stift.Sum'>})

#### parse()
Find lowest level functions, execute those first.

Then work up.


### class stift.stift.Sum()
Bases: `stift.stift.BaseFunction`


#### arg_counts( = 'ANY_NUM_ARGS')

#### arg_types()
alias of `Union`[`int`, `float`]


#### process()

### class stift.stift.Today()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Trim()
Bases: `stift.stift.BaseFunction`


### class stift.stift.Trunc()
Bases: `stift.stift.BaseFunction`


#### arg_counts( = (1, 2))

#### process()

### stift.stift.typechecker(x)
## Module contents
