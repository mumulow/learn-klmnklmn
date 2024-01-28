def solution(a, b):
  result = ""
  for num in range(a, b + 1):
    result += f"{num} "
  result += "\n"
  for dun in range(b, a - 1, -1):
    result += f"{dun}\n"
  return result.strip()

print(solution(1, 3))

rom
enum
import Enum
from uuid import uuid4

from uuid import uuid4
from enum import Enum
from secret_module import SECRET


class SalesStatus(Enum):
  CREATED = "created"
  PROCESSING = "processing"
  COMPLETED = "completed"
  WAIT_FOR_PAYMENT = "wait_for_payment"
  REJECTED = "rejected"
  ARCHIVED = "archived"


halstuch_storage = {1: {"color": SECRET, "cost": 100}}
sales_storage = {}


def sale_halstuch(hastuch_id: int):
  if not halstuch_storage.get(hastuch_id):
    return False
  sales = {"status": SalesStatus.CREATED, "halstuch_id": hastuch_id}
  sales_id = uuid4()
  sales_storage[sales_id] = sales
  ...

  sales["status"] = SalesStatus.COMPLETED
  del halstuch_storage[hastuch_id]
  return True


print(halstuch_storage)
print(sales_storage)
sale_halstuch(1)
print(halstuch_storage)
print(sales_storage)


def check_dz(expected_solution, solution_from_Egor):
  assert expected_solution == solution_from_Egor


expected_solution = 1
solution_from_Egor = 2

# LBYL
if expected_solution == solution_from_Egor:
  check_dz(expected_solution, solution_from_Egor)
else:
  print("Failed")

# 2
try:
  check_dz(expected_solution, solution_from_Egor)
except AssertionError:
  print("Failed")

some_dict = {"2": "keks"}
# LBYL
if "1" in some_dict:
  print(some_dict["1"])
else:
  print("Nope")


class NoCakeError(Exception):
  details = "No cake for you!"


# 2
try:
  try:
    print(some_dict["1"])
  except KeyError as key_error:
    raise NoCakeError from key_error
except NoCakeError as error:
  print(f"Nope: {error.details}")

try:
  ...  # Подозрительный код
except Exception as exc:
  ...  # Обработка исключения
else:
  ...  # Инструкция, если все ок
finally:
  ...  # Инструкция, исполняемая при любых условиях

# Инструкция после обработки