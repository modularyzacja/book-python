.. _Loop For:

********
Loop For
********


Syntax
======
.. highlights::
    * ``ITERABLE`` must implement ``iterator`` interface
    * More information in :ref:`Iterators`

.. code-block:: python
    :caption: ``for`` loop syntax
    :force:

    for <variable> in <iterable> :
        <do something>


Naming Convention
=================
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Prefer locally meaningfull name over generic names
* Generic names:

    * ``obj`` - generic name (in Python everything is an object)
    * ``element`` - generic name
    * ``item`` - generic name
    * ``e`` - bad, if scope is more than one line
    * ``l`` - bad, for letter
    * ``o`` - bad
    * ``d`` - for digit

* Locally meaningfull name:

    * ``letter``
    * ``feature``
    * ``digit``
    * ``person``
    * ``color``
    * ``username``
    * etc.

* Special meaning:

    * ``i`` - for loop counter


Iterating sequences
===================
.. code-block:: python
    :caption: Iterating over ``str`` will get character on each iteration

    for obj in 'setosa':
        print(obj)

    # s
    # e
    # t
    # o
    # s
    # a

.. code-block:: python
    :caption: Iterating over ``list`` will get one element on each iteration

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``tuple`` will get one element on each iteration

    DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``set`` will get one element on each iteration

    DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

.. code-block:: python
    :caption: Iterating over ``frozenset`` will get one element on each iteration

    DATA = frozenset({5.1, 3.5, 1.4, 0.2, 'setosa'})

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Range
=====
.. highlights::
    * ``range(start, stop, step)``
    * ``range(0, 3)`` will generate ``(0, 1, 2)``
    * ``start`` is inclusive, default: ``0``
    * ``stop`` is exclusive, required
    * ``step`` default: ``1``

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(0, 3):
        print(number)

    # 0
    # 1
    # 2

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(4, 11, 2):
        print(number)

    # 4
    # 6
    # 8
    # 10


Enumerate
=========
.. highlights::
    * Pythonic way
    * Preferred over ``i=0`` and ``i+=1`` for every iteration
    * ``enumerate()`` will return ``counter`` and ``value`` for every iteration

.. code-block:: python

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # a
    # b
    # c

.. code-block:: python
    :caption: ``enumerate()`` will return ``counter`` and ``value`` for every iteration

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA):
        print(i, letter)

    # 0 a
    # 1 b
    # 2 c

.. code-block:: python
    :caption: ``enumerate()`` can start with custom number

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA, start=5):
        print(i, letter)

    # 5 a
    # 6 b
    # 7 c


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_for_example.py`

:English:
    #. Use data from "Input" section (see below)
    #. Count occurrences of each color
    #. Compare results with "Output" section below

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zlicz wystąpienia każdego z kolorów
    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: python

        DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

:Output:
    .. code-block:: python

        result: Dict[str, int]
        # {'red': 3, 'green': 2, 'blue': 2}

:Solution:
    .. literalinclude:: solution/loop_for_example.py
        :language: python

Loop For Counter
----------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_for_counter.py`

:English:
    #. Use data from "Input" section (see below)
    #. Iterate over ``DATA``
    #. Count occurrences of each number
    #. Create empty ``result: Dict[int, int]``:

        * key - digit
        * value - number of occurrences

    #. Iterating over numbers check if number is already in ``result``

        * If first occurrence, then add it to ``result`` with value 1
        * If exists, then increment the value by 1

    #. Compare results with "Output" section below

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Iteruj po ``DATA``
    #. Policz wystąpienia każdej z cyfr
    #. Stwórz pusty ``result: Dict[int, int]``:

        * klucz - cyfra
        * wartość - liczba wystąpień

    #. Iterując po cyfrach sprawdź czy cyfra znajduje się już w ``result``

        * Jeżeli pierwsze wystąpienie, to dodaj ją do ``result`` z wartością 1
        * Jeżeli istnieje, to zwiększ w wartość o 1

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: python

        DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
                0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
                1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                4, 8, 1, 9, 6, 3]

:Output:
    .. code-block:: python

        result: Dict[int, int]
        # {1: 7, 4: 8, 6: 4, 7: 4, 5: 4, 0: 7, 9: 5, 8: 6, 2: 2, 3: 3}

:The whys and wherefores:
    * Defining ``dict`` :ref:`Mapping Dict`
    * Updating ``dict``
    * Iterating over sequences

Loop For Segmentation
---------------------
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/loop_for_segmentation.py`

:English:
    #. Use data from "Input" section (see below)
    #. Count occurrences of each group
    #. Define groups:

        * ``small`` - numbers in range [0-3)
        * ``medium`` - numbers in range [3-7)
        * ``large`` - numbers in range [8-9]

    #. Print ``result: Dict[str, int]``:

        * key - group
        * value - number of occurrences

    #. Compare results with "Output" section below

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Policz wystąpienia każdej z group
    #. Zdefiniuj grupy

        * ``small`` - liczby z przedziału <0-3)
        * ``medium`` - liczby z przedziału <3-7)
        * ``large`` - liczby z przedziału <7-9>

    #. Wypisz ``result: Dict[str, int]``:

        * klucz - grupa
        * wartość - liczba wystąpień

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: python

        DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
                0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
                1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                4, 8, 1, 9, 6, 3]

:Output:
    .. code-block:: python

        from typing import Dict

        result: Dict[str, int]
        # {'small': 16, 'medium': 19, 'large': 15}

:The whys and wherefores:
    * Defining ``dict``
    * Updating ``dict``
    * Iterating over sequences

Loop For Newline
----------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_for_newline.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: str``
    #. Use ``for`` to iterate over ``DATA``
    #. Join lines of text with newline (``\n``) character
    #. Do not use ``str.join()``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: str``
    #. Użyj ``for`` do iterowania po ``DATA``
    #. Połącz linie tekstu znakiem końca linii (``\n``)
    #. Nie używaj ``str.join()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Innput:
    .. code-block:: python

        DATA = [
            'We choose to go to the Moon.',
            'We choose to go to the Moon in this decade and do the other things.',
            'Not because they are easy, but because they are hard.']

:Output:
    .. code-block:: python

        result: str
        # 'We choose to go to the Moon.\nWe choose to go to the Moon in this decade and do the other things.\nNot because they are easy, but because they are hard.'

Loop For Substitute
-------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_for_substitute.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list``
    #. Use ``for`` to iterate over ``DATA``
    #. If letter is in ``PL_ASCII`` then use conversion value as letter
    #. Add letter to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj ``for`` do iteracji po ``DATA``
    #. Jeżeli litera jest w ``PL_ASCII`` to użyj przekonwertowanej wartości jako litera
    #. Dodaj literę do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        PL_TO_ASCII = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ż': 'z',
            'ź': 'z',
        }

        DATA = 'zażółć gęślą jaźń'

:Output:
    .. code-block:: python

        result: str
        # 'zazolc gesla jazn'

Loop For Text
-------------
* Complexity level: medium or hard
* Lines of code to write: 30 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/loop_for_text.py`

:English:
    #. Use data from "Input" section (see below)
    #. Given is text of the "Moon Speech" by John F. Kennedy's  :cite:`BasicKennedy1962`
    #. Sentences are separated by period (``.``)
    #. Clean each sentence from whitespaces at the beginning and at the end
    #. Words are separated by spaces
    #. Print the total number in whole text:

        * adverbs (words ending with "ly")
        * sentences
        * words
        * letters
        * characters (including spaces inside sentences, but without periods ``.``)
        * comas (``,``)

    #. Compare results with "Output" section below

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dany jest tekst przemówienia "Moon Speech" wygłoszonej przez John F. Kennedy'ego :cite:`BasicKennedy1962`
    #. Zdania oddzielone są kropkami (``.``)
    #. Każde zdanie oczyść z białych znaków na początku i końcu
    #. Słowa oddzielone są spacjami
    #. Wypisz także ile jest łącznie w całym tekście:

        * przysłówków (słów zakończonych na "ly")
        * zdań
        * słów
        * liter
        * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek ``.``)
        * przecinków (``,``)

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: text
        :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`BasicKennedy1962`

        We choose to go to the Moon.
        We choose to go to the Moon in this decade and do the other things.
        Not because they are easy, but because they are hard.
        Because that goal will serve to organize and measure the best of our energies and skills.
        Because that challenge is one that we are willing to accept.
        One we are unwilling to postpone.
        And one we intend to win

:Output:
    .. code-block:: text

        Sentences: 7
        Words: 71
        Characters: 347
        Letters: 283
        Commas: 1
        Adverbs: 0

:The whys and wherefores:
    * String splitting
    * Calculating lengths
    * Iterating over string
    * Variable naming convention
    * Good variable names