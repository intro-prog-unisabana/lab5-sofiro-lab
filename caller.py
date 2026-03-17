from mystery_module import transform_data
import sys

x = int(sys.argv[1])
y = float(sys.argv[2])

result = transform_data(x, y, "quiz_test")

print(result)