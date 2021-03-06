"""
* Assignment: OOP Method Syntax
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Calculator`
    3. Define method `add` in class `Calculator`
    4. Method `add` take `a` and `b` as arguments
    5. Method returns sum of `a` and `b`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Calculator`
    3. Zdefiniuj metodę `add` w klasie `Calculator`
    4. Metoda `add` przyjmuje `a` i `b` jako argumenty
    5. Metoda zwraca sumę `a` i `b`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass, ismethod
    >>> assert isclass(Calculator)
    >>> calc = Calculator()
    >>> assert ismethod(calc.add)
    >>> calc.add(1, 2)
    3
"""


# Solution
class Calculator:
    def add(self, a, b):
        return a + b
