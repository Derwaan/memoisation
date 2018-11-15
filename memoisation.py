##
# @authorr: Julien Gomez
# @date: 15/11/18
# 
# Ce fichier contient toutes les fonctions nécessaires à la mission 8.
##

### Fibonacci
# On commence par créer les différentes fonctions de Fibonacci

import time
import turtle

def fibo_recursive(n):
  """
  @pre: n >= O, n est un entier.
  @post: retourne la valeure en position n de la suite de Fibonacci. Pour n = 0, retourne 0.

  Cette fonction utilise la récursion.
  """
  if n <= 1:
    return n
  
  return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_iterative(n):
  """
  @pre: n >= O, n est un entier.
  @post: retourne la valeure en position n de la suite de Fibonacci. Pour n = 0, retourne 0.

  Cette fonction est itérative.
  """
  if n <= 1:
    return n

  a,b = 1,1
  for _ in range(n-1):
    a,b = b,a+b
  return a

def fibo_memoization(n):
  """
  @pre: n >= O, n est un entier.
  @post: retourne la valeure en position n de la suite de Fibonacci. Pour n = 0, retourne 0.

  Cette fonction utilise la méthode de mémoisation.
  """
  if n <= 1:
    return n
  
  return memoization(fibo_memoization, n-1) + memoization(fibo_memoization, n-2)

### Mémoisation
# On va avoir besoin d'un dictionaire pour stocker les valeures déjà vues
mapping = {}

def memoization(fun, n):
  """
  @pre: fun est une fonction, n est le paramètre envoyé à la function fun.
  @post: retourne la valeure de fun(n). 
    Si la valeure avait déjà été vue, elle est renvoyée depuis le dictionnaire mapping sinon elle y est rajoutée.
  """
  # Si la fonction n'a pas enore été vue
  if fun not in mapping:
    mapping[fun] = {n:fun(n)}
  # Si le paramètre pour la fonction n'a pas encore été vue
  elif n not in mapping[fun]:
    mapping[fun][n] = fun(n)
  # On renvoit la valeure contenue dans le dictionnaire
  return mapping[fun][n]

### Mesures
# On va créer les fonctions pour mesurer le temps pris par les fonctions de Fibonacci

def exec_time(fun):
  """
  @pre: fun est une fonction.
  @post: renvoie une fonction mesurant le temps pris par la fonction fun en secondes.
  """
  def f_time(n):
    t0 = time.clock()
    fun(n)
    t1 = time.clock()
    return t1 - t0
  return f_time

### Barchart
# On reprend la fonction draw_chart du cours

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    # t.write("  "+ str(height))
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

def main():
  wn = turtle.Screen()         # Set up the window and its attributes
  wn.bgcolor("lightgreen")

  tess = turtle.Turtle()       # Create tess and set some attributes
  tess.color("blue", "red")
  tess.pensize(3)

  # xs = []
  # # Iterative
  # for i in range(10000,1000000,100000):
  #   print("Current iteration: {0} - {1}%".format(i, (i/1000000)*100))
  #   xs.append(exec_time(fibo_iterative)(i)*10)

  # xs = []
  # # Recursive
  # for i in range(20, 40):
  #   print("Current iteration: {0} - {1}%".format(i, (i/40)*100))
  #   xs.append(exec_time(fibo_recursive)(i)*10)

  # xs = []
  # # Mémoisation
  # for i in range(480,500):
  #   print("Current iteration: {0} - {1}%".format(i, (i/500)*100))
  #   xs.append(exec_time(fibo_memoization)(i)*100000)

  for a in xs:
    print(a)
    # draw_bar(tess, a)

  wn.mainloop()

if __name__ == '__main__':
  main()