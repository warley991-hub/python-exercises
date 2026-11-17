def pairwise_div(Lnum, Ldenom):
  """Lnum and Ldenom are non-empty lists of equal lengths containing numbers.

  Returns a new list whose elements are the pairwise
  division of an element in Lnum by an element in Ldenom.

  Raise a ValueError if Ldenom contains 0.
  """

  assert len(Lnum) == len(Ldenom), 'As listas precisam ter o mesmo tamanho.'
  assert len(Lnum) and len(Ldenom) != 0, 'As listas não podem estar vazias!'
  results = []

  for i in range(len(Lnum)):
    try:
      r = Lnum[i]/Ldenom[i]
      results.append(r)
    except ZeroDivisionError:
      raise ValueError(f'Ldenom não pode conter zero.')
  return results

L1 = [4, 5, 6]
L2 = [1, 2, 3]

print(pairwise_div(L1,L2)) # prints [4.0, 2.5, 2.0]