import re


def GetOdeonId(url):

	txt = url

	re1='.*?'	# Non-greedy match on filler
	re2='((?:[a-z][a-z]*[0-9]+[a-z0-9]*))'	# Alphanum 1

	rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
	m = rg.search(txt)
	if m:
	    alphanum1=m.group(1)
	    return alphanum1