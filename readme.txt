Background
==========

This dataset includes two sets of scripts and data files.

Additional background information and description of usage will be in the forthcoming Nakamura dissertation.  Data originally supplied by Nakamura.  Python code and this readme file created by Wickes.  Data included within this deposit are examples to demonstrate execution.

Keyword matching tool
=====================

keyword_search.py

This tool uses a set of predefined keywords from a text file, searches through a csv file of project data from aiddata.org, and generates two data files:  keyword_results and project_subset results.  

Techinical information:  written with Python 2.7 using only standard library tools.  Not a command line tool so the expectation is that you change the script to change the source files, etc.

Keyword results
---------------

* line_num: the line number from the source file where the result was found
* project_num:  project number coming in from the source project file
* word:  which keyword (from keywords text file) matched on this line
* column_name: which column within the source data file the keyword was found within
* content: the content of that column name

You'll note that a project will have as many results as it has keyword matches. Example: if three keywords match within a single project entry, that will result in three entries within this file.  One for each keyword, with the matching column name and content in those respective columns.

Project subset results
----------------------

Should have the same structure as the project source file, but only includes projects that have at least one keyword match result.

***

Matching tool
=============

matching_tool.ipynb
matching_tool.py

This tool is originally written and designed for execution in the Jupyter Notebook environment.  For preservation purposes, I've included a dump of a .py version.  Written in Python 2.7 using only standard library utilities.

This takes in two source files:  a keyword results file (as produced by the keyword matching tool) and a project file from aiddata.org.  This then compares the projects found in the keywords results with other projects file and creates project subset results representing projects found only in the keywords file and projects only found within the projects file.  Useful to investigate differing results with an updated projects file.

Data structure should be the same as the aiddata.org project data file.
