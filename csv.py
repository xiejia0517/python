
#encoding:utf-8
import csv
 
#读取csv文件方式1
csvFile = open('../../data/capital/2011-Q3-cabi-trip-history-data.csv','r')
reader = csv.reader(csvFile)
 
data = []
 
for item in reader:
#	print(item)
	data.append(item)
 
#print(data)
 
csvFile.close()
 
 
#读取csv文件方式2
with open("../../data/capital/2011-Q3-cabi-trip-history-data.csv",'r') as csvFile:
	#读取csv文件,返回的是迭代类型
	reader2 = csv.reader(csvFile)
	for item2 in reader2:
		print(item2)
csvFile.close()
 
 
#从列表写入csv文件
#设置newline,否则两行之间会空一行
csvFile2 = open('../../data/capital/0001.csv','w',newline='')
writer = csv.writer(csvFile2)
m = len(data)
for i in range(m):
	writer.writerow(data[i])
csvFile2.close()
 
 
#从字典写入csv文件
dic = {'key_1':123,'key_2':456,'key_3':789}
csvFile3 = open('../../data/capital/0001.csv','w',newline='')
writer2 = csv.writer(csvFile3)
for key in dic:
	print(key)
#	writer2.writerow([key,dic[key]])
 
csvFile3.close()