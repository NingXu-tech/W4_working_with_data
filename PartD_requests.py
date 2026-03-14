import requests
import csv
url="https://example.com"
responce=requests.get(url)

print("Status code:",responce.status_code)
print("Ok:",responce.ok)
print("Url:",responce.url)
print("First 200 characters:",responce.text[:200])

text=responce.text.strip()
lines=text.split("\n")
print("last five lines")
for line in lines[-5:]:
    print(line)

csv_reader=csv.reader(lines,delimiter=";")
rows=[row for row in csv_reader]

print("last 5 rows:")
for row in rows[-5:]:
    print(row)

