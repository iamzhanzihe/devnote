[TOC]

# 基本資料類型

**Python 內建函數**（Built-in Functions）是 Python 解釋器預先定義好的函數，無需匯入任何模組就可以直接使用。這些函數是 Python 語言核心的一部分，提供了最基本和最常用的功能

|      函數       |      ==       |       ==       |       ==       |        ==        |
| :-------------: | :-----------: | :------------: | :------------: | :--------------: |
|     `abs()`     |  `delattr()`  |    `hash()`    | `memoryview()` |     `set()`      |
|     `all()`     |   `dict()`    |    `help()`    |    `min()`     |   `setattr()`    |
|     `any()`     |    `dir()`    |    `hex()`     |    `next()`    |    `slice()`     |
|    `ascii()`    |  `divmod()`   |     `id()`     |   `object()`   |    `sorted()`    |
|     `bin()`     | `enumerate()` |   `input()`    |    `oct()`     | `staticmethod()` |
|    `bool()`     |   `eval()`    |    `int()`     |    `open()`    |     `str()`      |
| `breakpoint()`  |   `exec()`    | `isinstance()` |    `ord()`     |     `sum()`      |
|  `bytearray()`  |  `filter()`   | `issubclass()` |    `pow()`     |    `super()`     |
|    `bytes()`    |   `float()`   |    `iter()`    |   `print()`    |    `tuple()`     |
|  `callable()`   |  `format()`   |    `len()`     |  `property()`  |     `type()`     |
|     `chr()`     | `frozenset()` |    `list()`    |   `range()`    |     `vars()`     |
| `classmethod()` |  `getattr()`  |   `locals()`   |    `repr()`    |     `zip()`      |
|   `compile()`   |  `globals()`  |    `map()`     |  `reversed()`  |  `__import__()`  |
|   `complex()`   |  `hasattr()`  |    `max()`     |   `round()`    |                  |

> [!warning]
>
> 避免重新定義內建函數，這樣會導致原本內建的函數無法使用
>
> ```python
> # ❌ 錯誤示範 - 重新定義內建函數
> list = [1, 2, 3]  # 覆蓋了內建的 list() 函數
> print = "hello"   # 覆蓋了內建的 print() 函數
> 
> # 現在無法使用原本的函數了
> # list([1, 2, 3])  # TypeError: 'list' object is not callable
> # print("hello")   # TypeError: 'str' object is not callable
> 
> # ✅ 正確做法
> my_list = [1, 2, 3]
> message = "hello"
> print(my_list)
> ```
>
> 