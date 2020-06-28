# coding: utf-8

import bs4
get_ipython().run_line_magic('pinfo', 'bs4.BeautifulSoup')
soup = bs4.BeautifulSoup('harrington-sales.html', features='html')
with open('harrington-sales.html') as infile:
    soup = bs4.BeautifulSoup(infile, features='html')
    
soup
soup
soup.find('Durham')
get_ipython().run_line_magic('pinfo', 'soup.find')
soup.find(text='Durham')
get_ipython().run_line_magic('pinfo', 'soup.findAll')
soup.findAll(text='Durham')
soup.findAll(text='Harrington')
soup.find(text='Harrington')
print(soup.prettify())
soup.findAll("div", class_="jobsearch-")
soup.findAll("div", class_="jobsearch-jobDescriptionText")
description = soup.findAll("div", class_="jobsearch-jobDescriptionText")[0]
print(description.prettify())
get_ipython().run_line_magic('save', 'exploration.py 0-19')
