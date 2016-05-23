from Graph import Graph

g = Graph()
course_code = [101,102,103,104,105,106,107,108,109,110,111,112]


course_info = {}
course_info.setdefault('DATA STRUCTURE101', []).append(3)
course_info.setdefault('DATA STRUCTURE101', []).append(101)

course_info.setdefault('ADVANCE DATA STRUCTURE102', []).append(5)
course_info.setdefault('ADVANCE DATA STRUCTURE102', []).append(102)

course_info.setdefault('ALGORITHMS103', []).append(4)
course_info.setdefault('ALGORITHMS103', []).append(103)

course_info.setdefault('COMPUTER FUNDAMENTALS104', []).append(2)
course_info.setdefault('COMPUTER FUNDAMENTALS104', []).append(104)

course_info.setdefault('ADVANCE STATISTICS105', []).append(6)
course_info.setdefault('ADVANCE STATISTICS105', []).append(105)

course_info.setdefault('NETWORKING CONCEPTS106', []).append(5)
course_info.setdefault('NETWORKING CONCEPTS106', []).append(106)

course_info.setdefault('CRYPTOGRAPHY107', []).append(6)
course_info.setdefault('CRYPTOGRAPHY107', []).append(107)

course_info.setdefault('NETWORK SECURITY108', []).append(5)
course_info.setdefault('NETWORK SECURITY108', []).append(108)

course_info.setdefault('WEB DESIGNING109', []).append(3)
course_info.setdefault('WEB DESIGNING109', []).append(109)

course_info.setdefault('STATISTICS110', []).append(4)
course_info.setdefault('STATISTICS110', []).append(110)

course_info.setdefault('ECONOMICS111', []).append(6)
course_info.setdefault('ECONOMICS111', []).append(111)

course_info.setdefault('DBMS112', []).append(5)
course_info.setdefault('DBMS112', []).append(112)


for key in course_info:
  c= 1
  for value in course_info[key]:
  	if c == 1:
  		g.addVertex(key,value)
  		c = c+1
  	else: 
  		break

print "####################################################################################################"
print g.vertList
print g.numVertices
print "\n \n"


def addEdge():
	g.addEdge('ALGORITHMS103','COMPUTER FUNDAMENTALS104',2)
	g.addEdge('ADVANCE STATISTICS105','STATISTICS110',4)
	g.addEdge('NETWORKING CONCEPTS106','COMPUTER FUNDAMENTALS104', 2)
	g.addEdge('NETWORK SECURITY108', 'CRYPTOGRAPHY107', 6)
	g.addEdge('NETWORK SECURITY108', 'NETWORKING CONCEPTS106', 5)
	g.addEdge('DBMS112', 'ADVANCE STATISTICS105', 6)
	g.addEdge('DBMS112', 'ECONOMICS111', 6)




addEdge()

for v in g:
   for w in v.getConnections():
       print("( %s, %s, %s, %s )" % (v.getId(),v.getCourse_time(), w.getId(),w.getCourse_time()))
print "\n \n"       


def ComputerScienceMajor_NetworkingMajor():
	total_time_major = 0
	courses = ['DATA STRUCTURE101','ADVANCE DATA STRUCTURE102', 'ALGORITHMS103', 'COMPUTER FUNDAMENTALS104', 'ADVANCE STATISTICS105', 'NETWORKING CONCEPTS106', 'CRYPTOGRAPHY107', 'NETWORK SECURITY108']  

	for v in g:
		if str(v.getId()) in courses:
			total_time_major = total_time_major + v.getCourse_time()
			for w in v.getConnections():
				print("( %s, %s, %s, %s )" % (v.getId(),v.getCourse_time(), w.getId(),w.getCourse_time()))
				if str(w.getId()) not in courses:
					total_time_major = total_time_major + w.getCourse_time()
				else:
					print "Sorry, the node has already been visited :) \n"
		
	print "Total time required for pursuing ComputerScience and Networking Major is " + str(total_time_major)  +  "\n"


def ComputerScienceMajor_DataScienceMajor():
	total_time_major = 0
	courses = ['DATA STRUCTURE101','ADVANCE DATA STRUCTURE102', 'ALGORITHMS103', 'COMPUTER FUNDAMENTALS104', 'ADVANCE STATISTICS105','WEB DESIGNING109', 'STATISTICS110', 'ECONOMICS111', 'DBMS112']  

	for v in g:
		if str(v.getId()) in courses:
			total_time_major = total_time_major + v.getCourse_time()
			for w in v.getConnections():
				print("( %s, %s, %s, %s )" % (v.getId(),v.getCourse_time(), w.getId(),w.getCourse_time()))
				if str(w.getId()) not in courses:
					total_time_major = total_time_major + w.getCourse_time()
				else:
					print "Sorry, the node has already been visited :)"
	print "Total time required for pursuing ComputerScienceMajor and DataScience Major is " + str(total_time_major)  +  "\n"

def NetworkingMajor_DataScienceMajor():
	total_time_major = 0
	courses = ['COMPUTER FUNDAMENTALS104', 'ADVANCE STATISTICS105', 'NETWORKING CONCEPTS106', 'CRYPTOGRAPHY107', 'NETWORK SECURITY108', 'WEB DESIGNING109', 'STATISTICS110', 'ECONOMICS111', 'DBMS112' ]  

	for v in g:
		if str(v.getId()) in courses:
			total_time_major = total_time_major + v.getCourse_time()
			for w in v.getConnections():
				print("( %s, %s, %s, %s )" % (v.getId(),v.getCourse_time(), w.getId(),w.getCourse_time()))
				if str(w.getId()) not in courses:
					total_time_major = total_time_major + w.getCourse_time()
				else:
					print "Sorry, the node has already been visited :)"
	print "Total time required for pursuing Networking and DataScience Major is " + str(total_time_major)  +  "\n"		






print "#####################ComputerScienceMajor_NetworkingMajor################################"
ComputerScienceMajor_NetworkingMajor()
print "#####################ComputerScienceMajor_DataScienceMajor##########################"
ComputerScienceMajor_DataScienceMajor()
print "#####################NetworkingMajor_DataScienceMajor####################################"
NetworkingMajor_DataScienceMajor()