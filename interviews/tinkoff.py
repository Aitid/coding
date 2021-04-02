# Давали мне в тинькофф Вт 30 март 2021
# Эту же задачу давали в яндексе на собесе
# Даны две строки из латинских символов;
# проверить, что одну из другой можно получить не более чем одной заменой,
# вставкой или удалением одного символа.

# aaa aba => true
# aaa bbb => false
# aaa aa => true
# aa aaa => true

# 1234
# 1334
counter = 3  4 4
# 92345
# 1234
counter 2 5 4

def f(s1, s2):
  '''
  1.
  '''
  i = 0
  counter = 0
  is_ex = True
  '''
  while i < len(s1) and i < len(s2):
    if s1[i] != s2[i]:
      if is_ex:
        is_ex = False
      else:
        counter += 1


    i += 1
  '''

  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:

      if is_ex and len(s2) != len(s1):
        is_ex = False
        if len(s2) > len(s1):
          j += 1
        elif len(s2) == len(s1):
          ...
        else:
          i += 1

      else:
        counter += 1
    i += 1
    j += 1



  if len(s1) == len(s2) and counter == 0:
    return True
  if len(s1) == len(s2) and counter == 1:
    return True

  if abs(len(s1) - len(s2)) == 1  and counter == 0:
    return True
  else:
    return False




assert f('abc', 'abc') == True
assert f('abc', 'aac') == True
assert f('abc', 'zabc') == True
assert f('abc', 'zabca') == False

assert f('abc', 'acd') == False
assert f('abc', 'ach') == False
