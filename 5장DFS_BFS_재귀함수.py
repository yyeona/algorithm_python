# 5-4 재귀함수 종료 예제
def recrusive_function(i):
  #100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recrusive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recrusive_function(1)

# 5-5 2가지 방식으로 구현한 팩토리얼 예제

def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result
  
# 재귀적으로 구현한 n!

def factorial_recursive(n):
    if n <= 1:
      return 1
  # n! = n * (n-1)를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! (n = 5)
print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))

# 재귀함수 최대공약수 계산 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
      return b
    else:
      return gcd(b, a % b)

print(gcd(192, 162))
