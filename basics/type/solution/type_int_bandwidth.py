"""

Type Int Bandwidth
------------------
* Last update: 2020-11-22
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 3 min

English:
    1. Having internet connection with speed 100 Mb/s
    2. How long will take to download 100 MB?
    3. In Calculations use truediv (``//``)
    4. Compare result with "Tests" section (see below)

Polish:
    1. Mając łącze internetowe 100 Mb/s
    2. Ile zajmie ściągnięcie pliku 100 MB?
    3. W obliczeniach użyj truediv (``//``)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> int(duration // SECOND)
    8

"""

# Given
SECOND = 1


# Solution
b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

speed = 100 * Mb / SECOND
size = 100 * MB
duration = size // speed
