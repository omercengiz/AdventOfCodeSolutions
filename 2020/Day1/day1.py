# complexity O(n^2)
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    numbers = [int(x) for x in lines]

def twoEntrySummation(numbers, input_summation):
  for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == input_summation:
        return numbers[i] * numbers[j]

twoEntrySummation(numbers, 2020)
# Answer is 651651
