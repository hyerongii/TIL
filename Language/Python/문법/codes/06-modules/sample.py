# import my_math
# from my_math import add

# print(my_math.add(1, 2))
# print(add(1,2))

# my_math.py에서 만든 함수를 불러옴

#패키지 안에 있는 경우 from절 사용

from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add)
print(tools.mod)
