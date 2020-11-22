"""
* Assignment name: Type Int Time
* Last update: 2020-11-22
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 8 min

English:
    1. Calculate how many seconds is one day
    2. Calculate how many minutes is one week
    3. Calculate how many hours is in one month
    4. Calculate how many seconds is work day (8 hours)
    5. Calculate how many minutes is work week (5 work days)
    6. Calculate how many hours is work month (22 work days)
    7. In Calculations use truediv (``//``)
    8. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz ile sekund to jedna doba
    2. Oblicz ile minut to jeden tydzień
    3. Oblicz ile godzin to jeden miesiąc
    4. Oblicz ile sekund to dzień pracy (8 godzin)
    5. Oblicz ile minut to tydzień pracy (5 dni pracy)
    6. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    7. W obliczeniach użyj truediv (``//``)
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 h = 60 min
    * 1 min = 60 s

Tests:
    >>> day
    86400
    >>> week
    10080
    >>> month
    744
    >>> workday
    28800
    >>> workweek
    2400
    >>> workmonth
    176
"""

# Given
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# Solution
day = (1*DAY) // SECOND
week = (7*DAY) // MINUTE
month = (31*DAY) // HOUR
workday = (8*HOUR) // SECOND
workweek = (5*workday) // MINUTE
workmonth = (22*workday) // HOUR
