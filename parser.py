from bs4 import BeautifulSoup
import urllib2
import re
import os
import subprocess

links = []
comparison = []
numberOfAntennas = 8
line_regex = re.compile(r"^\d")

proc = subprocess.Popen(["<customer>"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

out = out.replace("suite.log.html", "log_private/")
print out

soup = BeautifulSoup(urllib2.urlopen(out), "html.parser")
print "\nAvailable tests:\n"

for i, link in enumerate(soup.findAll('a', attrs={'href': re.compile("^tc_")})):
    links.append(link.get('href'))
    print "[{}]  {}".format(i, link.get('href'))


#testNum = raw_input('Select test number: ')
out = out.replace("log_private/", "log_private/" + links[int(raw_input('Select test: '))])

print out

soup = BeautifulSoup(urllib2.urlopen(out), "html.parser")
for i, link in enumerate(soup.findAll('a', attrs={'href': re.compile("^comparison")})):
    comparison.append(link.get('href'))
    print "[{}]  {}".format(i, link.get('href'))


arr = [[] for _ in comparison]
print arr
for i, logFile in enumerate(comparison):
	url = "{}{}".format(out, logFile).replace("\n", "")
	for line in urllib2.urlopen(url):
		if (line_regex.search(line)): 
			arr[i].append("{}+{}i".format(int(float(re.split("\t",line)[1].lstrip())),int(float(re.split("\t",line)[2].lstrip()))).replace("+-", "-"))				
		#print line	
	arr[i] = [arr[i][x:x+600] for x in range(0, len(arr[i]), 600)]

print arr[0][0]
print arr[1][2]
for p in arr[0][0]: print p

#for comp in arr:
#	comp[
		

	#print "{}+{}i".format(int(float(re.split("\t",line)[1].lstrip())),int(float(re.split("\t",line)[2].lstrip()))).replace("+-", "-")
	#tempList.append("{}+{}i".format(int(float(re.split("\t",line)[1].lstrip())),int(float(re.split("\t",line)[2].lstrip()))).replace("+-", "-"))


for line in urllib2.urlopen(url):
    print line
