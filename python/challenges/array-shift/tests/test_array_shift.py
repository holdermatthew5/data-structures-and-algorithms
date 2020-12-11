from code_challenges.array_shift.array_shift import insertShiftArray

# test number inputs

def test_check_numbers_one():
  actual = insertShiftArray([1,2,3,4,5,6], 8)
  expected = [1,2,3,8,4,5,6]
  assert actual == expected

def test_check_numbers_two():
  actual = insertShiftArray([1,2,3,4,5,6,7,8,9], 100)
  expected = [1,2,3,4,5,100,6,7,8,9]
  assert actual == expected

# test string inputs

def test_check_string_one():
  actual = insertShiftArray(["Huckabee", "Conway", "McConnel", "Trump"], "Melania")
  expected = ["Huckabee", "Conway", "Melania", "McConnel", "Trump"]
  assert actual == expected

def test_check_string_one():
  actual = insertShiftArray(["Biden", "Harris", "Obama", "AOC", "Porter"], "Ilhan")
  expected = ["Biden", "Harris", "Obama", "Ilhan", "AOC", "Porter"]
  assert actual == expected