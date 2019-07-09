expected = 'Jana III Sobieskiego'

a = '  Jana III Sobieskiego '
b = 'ul Jana III SobIESkiego'
c = '\tul. Jana trzeciego Sobieskiego'
d = 'ulicaJana III Sobieskiego'
e = 'UL. JA\tNA 3 SOBIES\tKIEGO'
f = 'UL. jana III SOBiesKIEGO'
g = 'ULICA JANA III SOBIESKIEGO  '
h = 'ULICA. JANA III SOBIeskieGO'
i = ' Jana 3 Sobieskiego  '
j = 'Jana III\tSobieskiego '
k = 'ul.Jana III Sob\n\nieskiego\n'


a = a.strip()
b = b.strip().upper().replace('UL', '').strip().title().replace('Iii', 'III')
c = c.strip().upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
d = d.strip().upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
e = e.strip().upper().replace('UL.', '').strip().replace('\t', '').title().replace('3', 'III')
f = f.strip().upper().replace('UL.', '').strip().title().replace('Iii', 'III')
g = g.strip().upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
h = h.strip().upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
i = i.strip().upper().replace('3', 'III').strip().title().replace('Iii', 'III')
j = j.strip().upper().replace('\t', '').strip().title().replace('Iii', 'III')
k = k.strip().upper().replace('UL.', '').replace('\n', '').title().replace('Iii', 'III')


print(f'{a == expected}\t a: "{a}"')
print(f'{b == expected}\t b: "{b}"')
print(f'{c == expected}\t c: "{c}"')
print(f'{d == expected}\t d: "{d}"')
print(f'{e == expected}\t e: "{e}"')
print(f'{f == expected}\t f: "{f}"')
print(f'{g == expected}\t g: "{g}"')
print(f'{h == expected}\t h: "{h}"')
print(f'{i == expected}\t i: "{i}"')
print(f'{j == expected}\t j: "{j}"')
print(f'{k == expected}\t k: "{k}"')
