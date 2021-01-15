"""
* Assignment: Protocol Descriptor Simple
* Filename: protocol_descriptor_simple.py
* Complexity: easy
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define descriptor class `Kelvin`
    2. Temperature must always be positive
    3. Use descriptors to check boundaries at each value modification
    4. All tests must pass
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę deskryptor `Kelvin`
    2. Temperatura musi być zawsze być dodatnia
    3. Użyj deskryptorów do sprawdzania wartości granicznych przy każdej modyfikacji
    4. Wszystkie testy muszą przejść
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> class Temperature:
    ...     kelvin = Kelvin()

    >>> t = Temperature()
    >>> t.kelvin = 1
    >>> t.kelvin
    1
    >>> t.kelvin = -1
    Traceback (most recent call last):
    ValueError: Negative temperature
"""


# Solution
class Kelvin:
    def __get__(self, parent, parent_type):
        return parent._value

    def __set__(self, parent, new_value):
        if new_value < 0:
            raise ValueError('Negative temperature')
        else:
            parent._value = new_value


