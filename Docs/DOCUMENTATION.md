<h1 align="center" id="top">🕉️ SutraLang Documentation</h1>

<p align="center">
    <strong>
        This document lists all the Sanskrit keywords and built-in function names recognized by SutraLang and their corresponding Python equivalents.
    </strong>
</p>

## 📖 Table of Contents

*   [📜 Keywords](#keywords)
    *   [🌿 Boolean & None](#boolean--none)
    *   [✨ Logical Operators](#logical-operators)
    *   [⚖️ Conditional Statements](#conditional-statements)
    *   [🔄 Looping Constructs](#looping-constructs)
    *   [📐 Functions and Lambdas](#functions-and-lambdas)
    *   [🛡️ Exception Handling](#exception-handling)
    *   [📥 Importing Modules](#importing-modules)
    *   [🌍 Scope and Memory](#scope-and-memory)
    *   [🔱 Classes & Asynchronous Operations](#classes--asynchronous-operations)
    *   [🔍 Pattern Matching (Python 3.10+)](#pattern-matching-python-310)
    *   [➡️ Other Keywords](#other-keywords)
*   [⚙️ Built-in Functions](#built-in-functions)
    *   [🔢 Type Conversion](#type-conversion)
    *   [⌨️ Input/Output](#inputoutput)
    *   [🧮 Mathematical Operations](#mathematical-operations)
    *   [⛓️ Working with Iterables/Sequences](#working-with-iterablessequences)
    *   [🤔 Object Introspection & Attributes](#object-introspection--attributes)
    *   [⚡ Asynchronous Operations](#asynchronous-operations)
    *   [🛠️ Code Execution & Debugging](#code-execution--debugging)
    *   [🏗️ Class-related](#class-related)
    *   [ℹ️ Other / Informational](#other--informational)
*   [🧩 Wrapped Modules](#wrapped-modules)
    *   [📐 गणित (Math Module)](#गणित-math-module)
    *   [🎲 यादृच्छिक (Random Module)](#यादृच्छिक-random-module)
    *   [🕰️ समय (Time/Datetime Module)](#समय-timedatetime-module)

---

## 📜 Keywords

Keywords are the fundamental building blocks for program structure and logic.

### 🌿 Boolean & None

These represent truth values and the concept of null.

| Sanskrit | Python  | Meaning / Use Case in SutraLang                      |
|----------|---------|----------------------------------------------------|
| सत्      | `True`  | Represents the boolean True value.                 |
| असत्     | `False` | Represents the boolean False value.                |
| नास्ति   | `None`  | Represents the absence of a value, or null object. |

### ✨ Logical Operators

Used for combining conditional statements.

| Sanskrit | Python | Meaning / Use Case in SutraLang        |
|----------|--------|--------------------------------------|
| च        | `and`  | Logical AND - true if both operands are true. |
| वा       | `or`   | Logical OR - true if at least one operand is true. |
| न        | `not`  | Logical NOT - inverts the truth value. |

### ⚖️ Conditional Statements

Used for making decisions in your code.

| Sanskrit | Python | Meaning / Use Case in SutraLang              |
|----------|--------|------------------------------------------|
| यदि     | `if`   | Primary conditional statement.           |
| अथयदि   | `elif` | Else-if conditional, for multiple checks.|
| अथ      | `else` | Else block, if no preceding conditions are met. |

### 🔄 Looping Constructs

Used for repeating blocks of code.

| Sanskrit | Python     | Meaning / Use Case in SutraLang                     |
|----------|------------|---------------------------------------------------|
| परिहरन   | `for`      | Iterates over a sequence (like a list or range).  |
| यावत्    | `while`    | Repeats a block as long as a condition is true.   |
| अग्रिम   | `break`    | Exits the current loop prematurely.               |
| विराम    | `continue` | Skips the rest of the current loop iteration and proceeds to the next. |
| गच्छतु   | `pass`     | A null operation; a placeholder where syntax requires a statement but no action is needed. |

### 📐 Functions and Lambdas

Used for defining reusable blocks of code.

| Sanskrit   | Python   | Meaning / Use Case in SutraLang                     |
|------------|----------|---------------------------------------------------|
| नियोग      | `def`    | Defines a named function.                         |
| निर्वतनम्  | `return` | Exits a function, optionally passing back a value. |
| अनाम       | `lambda` | Defines a small, anonymous (unnamed) function.    |

### 🛡️ Exception Handling

Used for managing errors and exceptional situations gracefully.

| Sanskrit   | Python    | Meaning / Use Case in SutraLang                        |
|------------|-----------|------------------------------------------------------|
| प्रयततु    | `try`     | Block of code to be attempted (may raise an error).  |
| विहाय      | `except`  | Block to handle specific errors raised in the `try` block. |
| अन्ततः     | `finally` | Block that always executes after `try` and `except`, regardless of errors. |
| विगर्हते   | `raise`   | Manually triggers an exception.                      |
| निश्चितयति | `assert`  | Checks a condition; if false, raises an AssertionError for debugging. |

### 📥 Importing Modules

Used for bringing external code and libraries into your script.

| Sanskrit | Python   | Meaning / Use Case in SutraLang                         |
|----------|----------|-------------------------------------------------------|
| आयात     | `import` | Imports an entire module.                             |
| यतः      | `from`   | Imports specific names (functions, classes) from a module. |
| नाम्ना    | `as`     | Assigns an alias (alternative name) to an imported module or name. |

### 🌍 Scope and Memory

Used for managing variable visibility and object lifetime.

| Sanskrit   | Python     | Meaning / Use Case in SutraLang                       |
|------------|------------|-----------------------------------------------------|
| सर्वत्रगम् | `global`   | Declares that a variable inside a function refers to a global variable. |
| असामीपिक  | `nonlocal` | Declares that a variable inside a nested function refers to a variable in an enclosing function (but not global). |
| अपनयति    | `del`      | Deletes a variable, object, or item from a list/dictionary. |

### 🔱 Classes & Asynchronous Operations

For object-oriented programming and concurrent code.

| Sanskrit   | Python  | Meaning / Use Case in SutraLang                        |
|------------|---------|------------------------------------------------------|
| विधि       | `class` | Defines a new class for creating objects.            |
| सह        | `with`  | Used with context managers for resource management (e.g., opening files). |
| यत्नतः     | `async` | Defines an asynchronous function (coroutine).        |
| प्रतीक्षेत् | `await` | Pauses execution of an `async` function until an awaitable operation completes. |

### 🔍 Pattern Matching (Python 3.10+)

For advanced structural comparisons.

| Sanskrit | Python  | Meaning / Use Case in SutraLang |
|----------|---------|-------------------------------|
| समानम्   | `match` | Begins a structural pattern matching block. |
| प्रकरणम्  | `case`  | Defines a specific pattern case within a `match` block. |

### ➡️ Other Keywords

Miscellaneous keywords.

| Sanskrit | Python | Meaning / Use Case in SutraLang |
|----------|--------|-------------------------------|
| इति     | `in`   | Checks for membership in a sequence or other iterable. |
| अस्ति    | `is`   | Tests if two variables refer to the same object (identity). |
| दत्ते    | `yield`| Used in generator functions to produce a sequence of values. |

## ⚙️ Built-in Functions

These functions are available globally in SutraLang.

### 🔢 Type Conversion

Functions for converting between different data types.

| Sanskrit         | Python         | Description                               |
|------------------|----------------|-------------------------------------------|
| सत्यासत्य       | `bool`         | Convert value to Boolean                  |
| बाइटसमूह        | `bytearray`    | Mutable sequence of bytes                 |
| बाइट           | `bytes`        | Immutable sequence of bytes               |
| संयुक्तसंख्या   | `complex`      | Create complex number                     |
| शब्दकोश        | `dict`         | Create dictionary                         |
| दशमलव         | `float`        | Convert to floating-point number          |
| अपरिवर्तनीयसमुच्चय | `frozenset` | Immutable set                             |
| पूर्णांक        | `int`          | Convert to integer                        |
| सूची           | `list`         | Create list                               |
| समुच्चय         | `set`          | Create set                                |
| अक्षरसमूह       | `str`          | String representation / convert to string |
| अनुक्रम         | `tuple`        | Create tuple                              |

### ⌨️ Input/Output

Functions for interacting with the user or files.

| Sanskrit   | Python  | Description               |
|------------|---------|---------------------------|
| प्रवेशयति  | `input` | Read input from console   |
| उद्घाटन   | `open`  | Open a file               |
| मुद्रण     | `print` | Print objects to console  |

### 🧮 Mathematical Operations

Functions for performing mathematical calculations.

| Sanskrit   | Python   | Description              |
|------------|----------|--------------------------|
| मूल्यमान  | `abs`    | Absolute value           |
| भागशेष   | `divmod` | Quotient and remainder   |
| अधिकतम    | `max`    | Maximum value            |
| न्यूनतम    | `min`    | Minimum value            |
| घात       | `pow`    | Raise number to power    |
| परिवर्तन   | `round`  | Round a number           |
| योग       | `sum`    | Sum of iterable items    |

### ⛓️ Working with Iterables/Sequences

Functions for operating on lists, tuples, strings, and other sequences or iterables.

| Sanskrit     | Python     | Description                         |
|--------------|------------|-------------------------------------|
| सर्वे        | `all`      | Check if all elements are true      |
| कश्चित्     | `any`      | Check if any element is true        |
| गणना       | `enumerate`| Iterator with index and value       |
| शोधन       | `filter`   | Filter elements from iterable       |
| पुनरावृत्ति | `iter`     | Get an iterator from an object      |
| दैर्घ्य     | `len`      | Length of an object                 |
| मानचित्र    | `map`      | Apply function to iterable elements |
| उत्तरम्     | `next`     | Get next item from iterator         |
| पङ्क्तिः   | `range`    | Sequence of numbers                 |
| विपरीत     | `reversed` | Reverse iterator                    |
| खण्ड        | `slice`    | Slice object                        |
| क्रमित     | `sorted`   | Sorted list from iterable           |
| संयोजन     | `zip`      | Combine iterables                   |

### 🤔 Object Introspection & Attributes

Functions for examining objects, their types, and attributes.

| Sanskrit     | Python         | Description                           |
|--------------|----------------|---------------------------------------|
| अक्षर       | `ascii`        | ASCII representation of an object     |
| आह्वानयोग्य | `callable`     | Check if object is callable           |
| गुणापहरण  | `delattr`      | Delete an attribute                   |
| गुणसूची     | `dir`          | List attributes of an object          |
| रूपण       | `format`       | Format a value                        |
| गुणप्राप्ति | `getattr`      | Get an attribute                      |
| सर्वत्रगवत् | `globals`      | Global symbol table dictionary        |
| गुणास्ति    | `hasattr`      | Check if object has attribute         |
| हैश        | `hash`         | Hash value of an object               |
| पहचान      | `id`           | Identity of an object                 |
| उदाहरणास्ति | `isinstance`   | Check if object is instance of class  |
| उपवर्गास्ति | `issubclass`   | Check if class is subclass            |
| स्थानीय     | `locals`       | Local symbol table dictionary         |
| वस्तु       | `object`       | Base class for all classes            |
| यूनिकोडअङ्क | `ord`          | Integer code point from character     |
| प्रतिनिधित्व| `repr`         | String representation of an object    |
| गुणस्थापन  | `setattr`      | Set an attribute                      |
| प्रकार      | `type`         | Type of an object / create type       |
| गुणशब्दकोश  | `vars`         | __dict__ attribute of object          |

### ⚡ Asynchronous Operations

Functions specific to asynchronous programming.

| Sanskrit       | Python  | Description                         |
|----------------|---------|-------------------------------------|
| असङ्ग्रहणक्रमः | `aiter` | Get asynchronous iterator           |
| अग्रहणम्       | `anext` | Get next item from async iterator   |

### 🛠️ Code Execution & Debugging

Functions related to executing code dynamically or helping with debugging.

| Sanskrit     | Python       | Description                         |
|--------------|--------------|-------------------------------------|
| विरामबिन्दु  | `breakpoint` | Enter debugger                      |
| संकलन      | `compile`    | Compile source into code object     |
| मूल्याङ्कन | `eval`       | Evaluate Python expression string   |
| निष्पादन    | `exec`       | Execute Python code string          |
| सहाय       | `help`       | Invoke built-in help system         |

### 🏗️ Class-related

Functions and decorators used primarily within class definitions.

| Sanskrit     | Python        | Description                         |
|--------------|---------------|-------------------------------------|
| वर्गविधि    | `classmethod` | Decorator for class methods         |
| गुण        | `property`    | Decorator for properties            |
| स्थिरविधि   | `staticmethod`| Decorator for static methods        |
| उपरि       | `super`       | Access parent/sibling class methods |

### ℹ️ Other / Informational

Miscellaneous utility and informational functions.

| Sanskrit         | Python       | Description                               |
|------------------|--------------|-------------------------------------------|
| अक्षरप्राप्ति   | `chr`        | Character from integer code point         |
| श्रेयांसि        | `credits`    | Display credits                           |
| प्रतिलिपिअधिकारः | `copyright`  | Display copyright                         |
| अनुज्ञा         | `license`    | Display license information               |
| स्मृतिदृश्य     | `memoryview` | Memory view of an object                  |
| अष्टांक         | `oct`        | Octal representation of integer           |
| षोडशांक         | `hex`        | Hexadecimal representation of integer     |
| त्यजति          | `quit`       | Exit interpreter (if site module enabled) |
| निर्गमः         | `exit`       | Exit interpreter (if site module enabled) |

## 🧩 Wrapped Modules

SutraLang provides wrappers around some standard Python modules to allow using their functionalities with Sanskrit names.

### 📐 गणित (Math Module)

The `गणित` module provides access to mathematical functions defined in the C standard.

**Import Example:**
```sanskrit
# गणितम् आनेतुं (To import math)
यतः घटकः.गणित आयात पाई, वर्गमूलम्

मानम् त्रिज्या = 7
मानम् क्षेत्रम् = पाई * (त्रिज्या ** 2)
छापय(f"वृत्तस्य क्षेत्रम्: {क्षेत्रम्}")
छापय(f"16 इत्यस्य वर्गमूलम्: {वर्गमूलम्(16)}")
```

#### 🌿 Constants

| Sanskrit | Python Equivalent | Description                  |
|----------|-------------------|------------------------------|
| पाई       | `math.pi`         | Mathematical constant Pi (π) |
| ई        | `math.e`          | Mathematical constant e      |
| अनन्तः    | `math.inf`        | Floating-point positive infinity |
| नाङ्कः    | `math.nan`        | Floating-point "Not a Number" |

#### ✨ Functions

| Sanskrit             | Python Equivalent      | Description                                       |
|----------------------|------------------------|---------------------------------------------------|
| पूर्णाङ्क_ऊर्ध्वम्    | `math.ceil(x)`         | Return the ceiling of x (smallest integer >= x).  |
| पूर्णाङ्क_अधः     | `math.floor(x)`        | Return the floor of x (largest integer <= x).     |
| निरपेक्ष_मूल्यम्    | `math.fabs(x)`         | Return the absolute value of x as a float.        |
| क्रमगुणितम्          | `math.factorial(x)`    | Return x factorial as an integer.                 |
| शक्ति                | `math.pow(x, y)`       | Return x raised to the power y (x**y).            |
| वर्गमूलम्            | `math.sqrt(x)`         | Return the square root of x.                      |
| लघुगणकः             | `math.log(x, base)`    | Return the logarithm of x to the given base.      |
| लघुगणकः_द्वि        | `math.log2(x)`         | Return the base-2 logarithm of x.                 |
| लघुगणकः_दश         | `math.log10(x)`        | Return the base-10 logarithm of x.                |
| ज्या                 | `math.sin(x)`          | Return the sine of x radians.                     |
| कोज्या               | `math.cos(x)`          | Return the cosine of x radians.                   |
| स्पर्शज्या           | `math.tan(x)`          | Return the tangent of x radians.                  |
| प्रतिलोम_ज्या       | `math.asin(x)`         | Return the arc sine of x, in radians.             |
| प्रतिलोम_कोज्या      | `math.acos(x)`         | Return the arc cosine of x, in radians.           |
| प्रतिलोम_स्पर्शज्या  | `math.atan(x)`         | Return the arc tangent of x, in radians.          |
| अंश_परिणतिः         | `math.degrees(x)`      | Convert angle x from radians to degrees.          |
| रेडियन_परिणतिः      | `math.radians(x)`      | Convert angle x from degrees to radians.          |
| हाइपरबोलिक_ज्या    | `math.sinh(x)`         | Return the hyperbolic sine of x.                  |

### 🎲 यादृच्छिक (Random Module)

The `यादृच्छिक` module implements pseudo-random number generators for various distributions.

**Import Example:**
```sanskrit
# यादृच्छिकम् आनेतुं (To import random)
यतः घटकः.यादृच्छिक आयात यादृच्छिक_पूर्णाङ्कः, चयनम्

मानम् संख्या = यादृच्छिक_पूर्णाङ्कः(1, 100)
छापय(f"एका यादृच्छिकी संख्या (1-100): {संख्या}")

मानम् मम_फलानि = ["आम्रम्", "कदलीफलम्", "सेवफलम्"]
मानम् एकम्_फलम् = चयनम्(मम_फलानि)
छापय(f"एकं यादृच्छिकं फलम्: {एकम्_फलम्}")
```

#### ✨ Functions

| Sanskrit             | Python Equivalent       | Description                                               |
|----------------------|-------------------------|-----------------------------------------------------------|
| बीजारोपणम्           | `random.seed(a=None)`   | Initialize the random number generator.                   |
| यादृच्छिकम्           | `random.random()`       | Return the next random floating point number in [0.0, 1.0).|
| यादृच्छिक_पूर्णाङ्कः | `random.randint(a, b)`  | Return a random integer N such that a <= N <= b.          |
| चयनम्                | `random.choice(seq)`    | Return a random element from the non-empty sequence seq.  |
| मिश्रणम्             | `random.shuffle(x)`     | Shuffle the sequence x in place.                          |
| समरूपम्              | `random.uniform(a, b)`  | Return a random floating point number N such that a <= N <= b or b <= N <= a. |
| प्रतिचयनम्           | `random.sample(pop, k)` | Return a k length list of unique elements chosen from the population sequence or set. |

### 🕰️ समय (Time/Datetime Module)

The `समय` module provides various functions to work with dates and times.

**Import Example:**
```sanskrit
# समयम् आनेतुं (To import time/datetime)
यतः घटकः.समय आयात अद्यतनः, कालवस्तु_रूपणम्

मानम् वर्तमानकालः = अद्यतनः()
छापय(f"वर्तमानः कालः: {वर्तमानकालः}")

मानम् स्वरूपितः_कालः = कालवस्तु_रूपणम्(वर्तमानकालः, "%Y-%m-%d %H:%M:%S")
छापय(f"स्वरूपितः कालः: {स्वरूपितः_कालः}")
```

#### 🌿 Constants

| Sanskrit         | Python Equivalent      | Description                  |
|------------------|------------------------|------------------------------|
| न्यूनतम_वर्षः    | `datetime.MINYEAR`     | The smallest year number allowed in a date or datetime object. |
| अधिकतम_वर्षः    | `datetime.MAXYEAR`     | The largest year number allowed in a date or datetime object.  |

#### ✨ Object Creation Functions

| Sanskrit             | Python Equivalent                            | Description                                                                 |
|----------------------|----------------------------------------------|-----------------------------------------------------------------------------|
| अद्यतनः              | `datetime.datetime.now()`                    | Return the current local date and time.                                     |
| रचय_तिथिम्           | `datetime.date(year, month, day)`            | Create a date object.                                                       |
| रचय_कालम्            | `datetime.time(h, m, s, us)`               | Create a time object.                                                       |
| रचय_सम्पूर्णकालम्    | `datetime.datetime(y, m, d, h, min, s, us)` | Create a datetime object.                                                   |
| रचय_समयान्तरम्       | `datetime.timedelta(...)`                    | Represents a duration, the difference between two dates or times.           |

#### ✨ Formatting, Parsing & Component Access Functions

These functions generally operate on a date, time, or datetime object passed as the first argument (`कालवस्तु`).

| Sanskrit                        | Python Equivalent (Method on object) | Description                                                                 |
|---------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| कालवस्तु_रूपणम्                 | `obj.strftime(format)`               | Format an object (date, datetime, time) into a string.                      |
| कालज्ञानम्_अक्षरशः              | `datetime.datetime.strptime(str, fmt)`| Parse a string into a datetime object.                                      |
| वर्षः_प्राप्नुहि                 | `obj.year`                           | Get the year.                                                               |
| मासः_प्राप्नुहि                  | `obj.month`                          | Get the month.                                                              |
| दिनम्_प्राप्नुहि                  | `obj.day`                            | Get the day.                                                                |
| घण्टा_प्राप्नुहि                 | `obj.hour`                           | Get the hour.                                                               |
| कला_प्राप्नुहि                   | `obj.minute`                         | Get the minute.                                                             |
| विकला_प्राप्नुहि                 | `obj.second`                         | Get the second.                                                             |
| दिनसप्ताहः_प्राप्नुहि           | `obj.weekday()`                      | Return the day of the week as an integer (Monday=0, Sunday=6).              |
| दिनवर्षस्य_प्राप्नुहि             | `obj.timetuple().tm_yday`            | Return the day of the year (1-366).                                         |
| कालवस्तु_परिवर्तय             | `obj.replace(...)`                   | Return a datetime with the same attributes, except for those attributes given new values by whichever keyword arguments are specified. |
| अन्तर्राष्ट्रिय_मानकस्वरूपम्      | `obj.isoformat(sep='T')`             | Return a string representing the date/datetime in ISO 8601 format.        |
| अन्तर्राष्ट्रिय_दिनसप्ताहक्रमाङ्कः | `obj.isoweekday()`                   | Return the day of the week as an integer (Monday=1, Sunday=7).              |
