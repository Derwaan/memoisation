import time
import turtle

def fibo_recursive(n):
  count = 0
  def fibo_recursive_count(n):
    count += 1
    if n <= 1:
      return n
    return fibo_recursive_count(n-1) + fibo_recursive_count(n-2)

  print("{0},{1}".format(n ,count))
  return fibo_recursive_count(n)

def fibo_iterative(n):
  if n <= 1:
    return n

  a,b = 1,1
  for _ in range(n-1):
    a,b = b, a+b
  
  return a

def fibo_mem(n):
  memo = {0:0, 1:1}
  count = 0
  def fibo_memo(n):
    count += 1
    if n not in memo:
      memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]
  
  print("{0},{1}".format(n ,count))
  return fibo_memo(n)

# def fibo_mem(n):
#   if n <= 1:
#     return n
#   return memoization(fibo_mem, n-1) + memoization(fibo_mem, n-2)

# mapping = {} # Sans cas de base

# def memoization(f, n):
#   if f not in mapping:
#     mapping[f] = {n:f(n)}
#   elif n not in mapping[f]:
#     mapping[f][n] = f(n)
#   return mapping[f][n]

def exec_time(f):
  def exec_times(n):
    t0 = time.clock()
    f(n)
    return time.clock() - t0
  return exec_times

def main():
  for i in range(0, 31, 2):
    # t_recursive = exec_time(fibo_recursive)(i)
    # t_iterative = exec_time(fibo_iterative)(i)
    t_mem = exec_time(fibo_mem)(i)
    # print("{0},{1},{2}".format(t_recursive, t_iterative, t_mem))
    # print(t_mem)

if __name__ == '__main__':
  main()

  