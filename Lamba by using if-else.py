#odd and even number
def odd_value(x):
  check_num=lambda x:"Even" if x%2==0 else "Odd"
  return check_num(x)

print(odd_value(10))
print(odd_value(11))
#finding greater number
def greater_num(a,b):
  check_value=lambda a,b:a if a>b else b
  return check_value(a,b)

print(greater_num(10,22))
print(greater_num(14,1))
#CHECKING POSITIVE AND NEGATIVE VALUE
def odd_value(x):
  check_num=lambda x:"Positive value" if x>=0 else "Negative value"
  return check_num(x)

print(odd_value(0))
print(odd_value(-1))
#check pass or fail
def odd_value(mark):
  check_num=lambda mark:"Pass" if mark>=45 else "Fail"
  return check_num(mark)

print(odd_value(10))
print(odd_value(55))
#check eligible for voting
def odd_value(mark):
  check_num=lambda mark:"Eligible for voting" if mark>=18 else "Not eligible for voting"
  return check_num(mark)

print(odd_value(10))
print(odd_value(55))