
# coding: utf-8

# In[2]:

import csv


# In[3]:

keywords_f = 'Peru_KeywordsSpanish_2009_2016_AidData.csv'
database_f = 'project__1_2016-09-24-15-45.csv'


# In[5]:

with open(keywords_f, 'rU') as fin:
    fin = csv.reader(fin)
    keywords_head = next(fin)
    keywords_data = [d for d in fin]
    
with open(database_f, 'rU') as fin:
    fin = csv.reader(fin)
    database_head = next(fin)
    database_data = [d for d in fin]


# In[8]:

keywords_head

kw = {r[2]: r for r in keywords_data}


# In[12]:

database_head

db = {r[0]: r for r in database_data}


# In[29]:

kw_ids = set(kw.keys())
db_ids = set(db.keys())
db_kw_intersect = kw_ids.intersection(db_ids) # this content will be written to the file
db_kw_diff = kw_ids.difference(db_ids) # list of ids kw but not db
kw_db_diff = db_ids.difference(kw_ids) # list of ids in db but not kw


# In[22]:

len(kw_ids), len(db_ids), len(db_kw_intersect)


# In[24]:

merge = {}

for idnum in db_kw_intersect:
    merge[idnum] = kw[idnum] + db[idnum]


# In[25]:

headers = keywords_head + database_head


# In[27]:

with open('merged.csv', 'wt') as fout:
    fout = csv.writer(fout)
    fout.writerow(headers)
    fout.writerows(merge.values())


# In[39]:

in_kw_not_in_db = {}

for idnum in db_kw_diff:
    in_kw_not_in_db[idnum] = kw[idnum]
    
in_db_not_in_kw = {}

for idnum in kw_db_diff:
    in_db_not_in_kw[idnum] = db[idnum]

with open('in_kw_not_in_db.csv', 'wt') as fout:
    fout = csv.writer(fout)
    fout.writerow(keywords_head)
    fout.writerows(in_kw_not_in_db.values())
    
with open('in_db_not_in_kw.csv', 'wt') as fout:
    fout = csv.writer(fout)
    fout.writerow(database_head)
    fout.writerows(in_db_not_in_kw.values())


# In[34]:

len(kw_db_diff)


# In[ ]:



