from typing import List, TypeVar, Union

T = TypeVar('T', int, float, str)

def multiply_elements(elements: List[T], multiplier: Union[int, float] = 2) -> List[T]:
    
    return [element * multiplier for element in elements]

# Лямбда-функция
multiply_elements_lambda = lambda elements, multiplier=2: list(map(lambda x: x * multiplier, elements))
