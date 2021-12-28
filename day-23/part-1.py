#!/usr/bin/python3
import numpy as np
from collections import Counter
from copy import deepcopy

state = [
    'E', 'E', ['B', 'C'], 'E', ['A', 'D']
]

A = ['B', 'C']
B = ['A', 'D']
C = ['B', 'D']
D = ['C', 'A']

TOP = ['E'] * 11
initial_state = ({'A': A, 'B': B, 'C': C, 'D': D}, TOP)
COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
EMPTY = "E"

def done(state):
  return state == ({
      'A': ['A', 'A'],
      'B': ['B', 'B'],
      'C': ['C', 'C'],
      'D': ['D', 'D']
  }, TOP)

def only_correct_letter(char, column):
    return len([*filter(lambda c: c not in [char, EMPTY], column)]) == 0

def bot_idx(bot):
  return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]

def top_idx(bot, col):
  for i,c in enumerate(col):
    if c != EMPTY and c != bot:
      return i
  return None

def dest_idx(col):
  return None if "E" not in col else len(col) - col[::-1].index("E") - 1

def clear_path(bot, top_idx, top):
  return top[bot_idx(bot):top_idx:np.sign(top_idx-bot_idx(bot))] == ['E'] * abs(top_idx - bot_idx(bot))

DP = {}
def calculate_min_energy(state):
  bot, top = state
  key = (tuple((k, tuple(v)) for k,v in bot.items()), tuple(top))
  if done(state):
    return 0
  if key in DP:
    return DP[key]

  # move to dest if possible
  for i, c in enumerate(top):
    if c != EMPTY and only_correct_letter(c, bot[c]) and clear_path(c, i, top):
        di = dest_idx(bot[c])
        dist = di + 1 + abs(bot_idx(c)-i)
        cost = COST[c] * dist
        new_top = list(top)
        new_top[i] = 'E'
        top[i] = 'E'
        new_bot = deepcopy(bot)
        new_bot[c][di] = c
        return cost + calculate_min_energy((new_bot, new_top))

  # move from bottom to top
  ans = int(1e9)
  for k, col in bot.items():
    if only_correct_letter(k, col):
      continue
    ki = top_idx(k, col)
    if ki is None:
      continue
    c = col[ki]
    for to_ in range(len(top)):
      if to_ in [2, 4, 6, 8] or top[to_] != EMPTY:
        continue
      if clear_path(k, to_, top):
        dist = ki + 1 + abs(to_ - bot_idx(k))
        new_top = list(top)
        new_top[to_] = c
        new_bot = deepcopy(bot)
        new_bot[k][ki] = EMPTY
        ans = min(ans, COST[c]*dist + calculate_min_energy((new_bot, new_top)))
  DP[key] = ans
  return ans

print(calculate_min_energy(initial_state))