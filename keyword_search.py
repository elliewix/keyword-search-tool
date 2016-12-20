import csv


# this is the file path for your source CSV of all the data
source = 'project__1_2016-09-24-15-45.csv'

with open(source, 'rt') as fin:
	fin = csv.reader(fin)
	headers = next(fin)
	data = [r for r in fin]

# add your headers here, be sure they match *perfectly* to the CSV headers
headers_to_look_in = ['Title', 'Short Description','Long Description','AidData Purpose Name', 'AidData Activity Name(s)']

headerids = [headers.index(h) for h in headers if h in headers_to_look_in] # finds the header index values you want


# this is the file path for your keywords
keywords_source = 'keywords_miller_includespanish.txt'

with open(keywords_source, 'rt') as fin:
	keywords = [l.strip().lower() for l in fin.readlines() if len(l) > 0]

#print keywords

miniheaders = ['line_num', 'project_number', 'word', 'column_name', 'content']
miniresults = []

bigresults = []


# begin searching through the data rows for matches
for line_num, row in enumerate(data):
	# enumerates the rows so you can know which line number you're working on
	results = [row[i].lower() for i in headerids] 
	# returns the lowercase version of the cell if that cell number is in the headers of interest
	# effectively this grabs just the cell values you care about, based on the headers you specify at the beginning
	for word in keywords: # iterating through the keywords
		check = [[line_num, row[0], word, headers[headerids[k]], cell] for k, cell in enumerate(results) if cell.find(word) != -1]
		# return the linenum, keyword, header name, and the cell value for each cell if the keyword
		# of interest is found within that cell.
		# this means that a single row will have multiple entries within your results files if 
		# multiple keywords are found within content
		if len(check) > 0:
			# if the results are not empty
			for item in check:
				miniresults.append(item) # add the keywords results to one big list
			bigresults.append(line_num) # add the full row results to one big list for writing

uniquebigresults = list(set(bigresults))

uniquerows = [data[i] for i in uniquebigresults]

#print miniresults

# write out the files
with open('project_subset_results.csv', 'wt') as fout:
	fout = csv.writer(fout)
	fout.writerow(headers)
	fout.writerows(uniquerows)
	
with open('keyword_results_1.csv', 'wt') as fout:
	fout = csv.writer(fout)
	fout.writerow(miniheaders)
	fout.writerows(miniresults)
