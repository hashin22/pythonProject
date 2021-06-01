import csv



f = open('./1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()

# with open("./1.csv", "rb") as source:
#
#     f = f.drop(f.index[[0,2]])



f = open('./1.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['1', '김정수', '2017-01-19', '11:30:00', '25'])
wr.writerow(['2', '박민구', '2017-02-07', '10:22:00', '35'])
wr.writerow(['3', '정순미', '2017-03-22', '9:10:00', '33'])
wr.writerow(['4', '용뽀진', '2021-05-20', '9999:00', '99'])
# f.close()