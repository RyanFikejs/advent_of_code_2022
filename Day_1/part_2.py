with open("input.txt", "r") as f:
  try:
    calorie_counts = []
    temp_count = 0
    
    for line in f:
      if line == "\n":
        calorie_counts.append(temp_count)
        temp_count = 0
      else:
        temp_count += int(line)

    calorie_counts.sort(reverse=True)
    print(sum(calorie_counts[:3]))
      
  finally:
    f.close()