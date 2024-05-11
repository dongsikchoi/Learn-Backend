line_count = 20 
overall_score_total = 0
got_score_total = 0 
table_dict = {
    'A+' : 4.5,
    'A0' : 4,
    'B+' : 3.5,
    'B0' : 3,
    'C+' : 2.5,
    'C0' : 2,
    'D+' : 1.5,
    'D0' : 1,
    'F' : 0
}

for _ in range(line_count):
    name, score, grade = input().split()

    if grade == 'P':
        continue
    else:
        score = float(score)
        got_score_total += score
        overall_score_total += (score * table_dict[grade])

print(round((overall_score_total / got_score_total),4))