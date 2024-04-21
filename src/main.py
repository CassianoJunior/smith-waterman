from os import path

def print_matrix(matrix: list[list[int]]):
  # Print the matrix
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(f'{matrix[i][j]:>3}', end=' ')
    print()

def create_initial_matrix(sequence1: str, sequence2: str) -> list[list[int | str]]:
  # Create the matrix with labels
  matrix = [[0 for _ in range(len(sequence1) + 2)] for _ in range(len(sequence2) + 2)]
  

  # Add gap labels
  lower_left_corner_row = len(sequence2) + 1
  lower_left_corder_column = 0

  matrix[lower_left_corner_row][lower_left_corder_column] = ' '
  matrix[lower_left_corner_row - 1][lower_left_corder_column] = '-'
  matrix[lower_left_corner_row][lower_left_corder_column + 1] = '-'

  # Add row labels
  inverted_sequence_2 = sequence2[::-1]
  for i in range(len(inverted_sequence_2)):
    matrix[i][0] = inverted_sequence_2[i]

  # Add column labels
  matrix[len(sequence2) + 1][2:] = [char for char in sequence1]

  # Add gap penalties
  for i in range(2, len(matrix[0])):
    matrix[len(matrix) - 2][i] = (i - 1) * gap
  
  for i in range(len(sequence2) - 1, -1, -1):
    matrix[i][1] = (len(sequence2) - i) * gap

  matrix[lower_left_corner_row - 1][lower_left_corder_column + 1] = 0

  # Return the matrix
  return matrix

def get_score(source_char: str, target_char: str, gap: int, match: int, mismatch: int) -> int:
  if "-" in [source_char, target_char]:
    return gap
  
  return match if source_char == target_char else mismatch 

def traceback(matrix: list[list[int | str]], sequence1: str, sequence2: str):
  i, j = 0, len(sequence1) + 1

  alignment1 = ''
  alignment2 = ''

  breakpointRow = len(sequence2)
  breakpointColumn = 1

  while True:
    if i == breakpointRow:
      while j > breakpointColumn:
        alignment1 = sequence1[j - 2] + alignment1
        alignment2 = '-' + alignment2
        j -= 1
      break
  
    if j == breakpointColumn:
      while i < breakpointRow:
        alignment1 = '-' + alignment1
        alignment2 = sequence2[len(sequence2) - 1 - i] + alignment2
        i += 1
      break

    current_score = matrix[i][j]
    diagonal_score = matrix[i + 1][j - 1]
    left_score = matrix[i][j - 1]

    if (type(diagonal_score) == str):
      diagonal_score = 0

    if (type(left_score) == str):
      left_score = 0

    if current_score == diagonal_score + get_score(sequence1[j - 2], sequence2[len(sequence2) - 1 - i], gap, match, mismatch):
      alignment1 = sequence1[j - 2] + alignment1
      alignment2 = sequence2[len(sequence2) - 1 - i] + alignment2
      i += 1
      j -= 1
    elif current_score == left_score + gap:
      alignment1 = sequence1[j - 2] + alignment1
      alignment2 = f'-{alignment2}'
      j -= 1
    else:
      alignment1 = f'-{alignment1}'
      alignment2 = sequence2[len(sequence2) - 1 - i] + alignment2
      i += 1

  return alignment1, alignment2

def check_align(align1: str, align2: str, gap: int, match: int, mismatch: int, expected_score: int):
  score = 0
  for i in range(len(align1)):
    if align1[i] == '-' or align2[i] == '-':
      score += gap
    elif align1[i] == align2[i]:
      score += match
    else:
      score += mismatch


  return score == expected_score


if __name__ == '__main__':
  print('Smith waterman')

  # Read the input file
  input_file_path = path.join(path.dirname(__file__), 'input.txt')
  with open(input_file_path, 'r') as file:
    sequence1_with_gaps = file.readline().strip().upper()
    sequence2_with_gaps = file.readline().strip().upper()
    gap = int(file.readline().strip())
    mismatch = int(file.readline().strip())
    match = int(file.readline().strip())
  
  # Print read sequences
  sequence1 = sequence1_with_gaps.replace('-', '')
  sequence2 = sequence2_with_gaps.replace('-', '')

  print('Sequence 1:', sequence1)
  print('Sequence 2:', sequence2)

  # Create the initial matrix
  matrix = create_initial_matrix(sequence1, sequence2)

  # Print initial matrix
  print('Initial score matrix')
  print_matrix(matrix)
  
  # Fill the matrix
  for i in range(len(sequence2) - 1, -1, -1):
    for j in range(2, len(sequence1) + 2):
      with_match = matrix[i+1][j-1] + get_score(sequence1[j - 2], sequence2[len(sequence2) - 1 - i], gap, match, mismatch)
      with_gap_sequence1 = matrix[i][j - 1] + gap
      with_gap_sequence2 = matrix[i + 1][j] + gap

      matrix[i][j] = max(with_match, with_gap_sequence1, with_gap_sequence2)

  # Print the final matrix
  max_score = matrix[0][len(sequence1) + 1]
  print('Final score matrix')
  print_matrix(matrix)

  # Traceback
  align1, align2 = traceback(matrix, sequence1, sequence2)

  if not check_align(align1, align2, gap, match, mismatch, max_score):
    print('The alignment is incorrect')
    exit()

  for _ in range(50):
    if _ == 49: 
      print()
      continue
    print('-', end='')

  print(f'Alignment ** score = {max_score} ** Match = {match} | Mismatch = {mismatch} | Gap = {gap}')

  for _ in range(50):
    if _ == 49: 
      print()
      continue
    print('-', end='')

  print(align1)
  print(align2)

  