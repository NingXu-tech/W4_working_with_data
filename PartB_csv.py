import csv
with open("student.csv","r",encoding="utf-8")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        print(row)

with open("student.csv","r",encoding="utf-8")as f:
    csv_reader=csv.reader(f)
    rows=[row for row in csv_reader]
print("All rows")
print(rows)

header=rows[0]
data_rows=rows[1:]
print("Header:",header)
print("data rows:",data_rows)

scores=[int(row[2])for row in data_rows]
average=sum(scores)/len(scores)
max_score=max(scores)
print("scores:",scores)
print("average acores:",average)
print("max score:",max_score)

with open("student.csv","r",encoding="utf-8")as f:
    csv_reader2=csv.DictReader(f)
    records=[row1 for row1 in csv_reader2]
for record in records:
    print("record:",record)
name1=[record["name"]for record in records]
age1=[int(record["age"])for record in records]
score1=[int(record["score"])for record in records]
max_score1=max(score1)
top_student=[record["name"]for record in records if int(record["score"])== max_score1]
older_student=[record["name"]for record in records if int(record["age"])>20]
print("name:",name1)
print("age:",age1)
print("score:",score1)
print("max score",max_score1)
print("top student:",top_student)
print("older students:",older_student)