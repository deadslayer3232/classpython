


 # reader(...)
 #        csv_reader = reader(iterable [, dialect='excel']
 #                                [optional keyword args])
 #            for row in csv_reader:
 #                process(row)


 # writer(...)
 #        csv_writer = csv.writer(fileobj [, dialect='excel']
 #                                    [optional keyword args])
 #            for row in sequence:
 #                csv_writer.writerow(row)

import csv

def pen(fileob,data):
	
	csv_writer = csv.writer(fileob,delimiter = ',')
	for a in data:
		csv_writer.writerow(a)

if __name__ =='__main__':
	fileob = open('detais.csv','w')
	data = ['name,class,phno,address'.split(','),
	'batman,python,2222,usa'.split(',')
	'superman,python,5555,paki'.split(',')]
	pen(fileob,data)