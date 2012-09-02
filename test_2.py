import json
f = open("data.py","r")
data = json.load(f)
from termcolor import colored, cprint
# OUT: {u'name': u'ODEON Camden', u'chain_id': u's75', u'times': {u'Brave 2D': [u'f12841', {u'Wednesday': [[u'15:00', u'/fanatic/booking-interactive/s75/p13960000023DFBTZNA/'], [u'17:30', u'/fanatic/booking-interactive/s75/p23960000023DFBTZNA/']], u'Thursday': [[u'15:00', u'/fanatic/booking-interactive/s75/p53960000023DFBTZNA/'], [u'17:30', u'/fanatic/booking-interactive/s75/p63960000023DFBTZNA/']]}], u'Fat Boy Slim Live: From The Big Beach Bootique': [u'f14110', {}], u'Brave 3D': [u'f100416', {u'Wednesday': [[u'12:30', u'/fanatic/booking-interactive/s75/p03960000023DFBTZNA/']], u'Thursday': [[u'12:30', u'/fanatic/booking-interactive/s75/p43960000023DFBTZNA/']]}], u'The Bourne Legacy': [u'f13170', {u'Wednesday': [[u'15:00', u'/fanatic/booking-interactive/s75/pD4960000023DFBTZNA/'], [u'18:00', u'/fanatic/booking-interactive/s75/pE4960000023DFBTZNA/'], [u'21:00', u'/fanatic/booking-interactive/s75/pF4960000023DFBTZNA/']], u'Thursday': [[u'15:00', u'/fanatic/booking-interactive/s75/p05960000023DFBTZNA/'], [u'18:00', u'/fanatic/booking-interactive/s75/p15960000023DFBTZNA/'], [u'21:00', u'/fanatic/booking-interactive/s75/p25960000023DFBTZNA/']]}], u'Ted': [u'f13390', {u'Wednesday': [[u'16:00', u'/fanatic/booking-interactive/s75/p89960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p99960000023DFBTZNA/'], [u'21:15', u'/fanatic/booking-interactive/s75/pE9960000023DFBTZNA/']], u'Thursday': [[u'16:00', u'/fanatic/booking-interactive/s75/p1A960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p0A960000023DFBTZNA/'], [u'21:15', u'/fanatic/booking-interactive/s75/pF9960000023DFBTZNA/']]}], u'The Dark Knight Rises': [u'f13222', {u'Wednesday': [[u'13:30', u'/fanatic/booking-interactive/s75/p28960000023DFBTZNA/'], [u'16:45', u'/fanatic/booking-interactive/s75/p38960000023DFBTZNA/'], [u'20:15', u'/fanatic/booking-interactive/s75/p48960000023DFBTZNA/']], u'Thursday': [[u'13:30', u'/fanatic/booking-interactive/s75/p58960000023DFBTZNA/'], [u'16:45', u'/fanatic/booking-interactive/s75/p68960000023DFBTZNA/'], [u'20:15', u'/fanatic/booking-interactive/s75/p78960000023DFBTZNA/']]}], u'Total Recall': [u'f13978', {u'Wednesday': [[u'13:00', u'/fanatic/booking-interactive/s75/p46960000023DFBTZNA/'], [u'15:30', u'/fanatic/booking-interactive/s75/p56960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p66960000023DFBTZNA/'], [u'21:30', u'/fanatic/booking-interactive/s75/p76960000023DFBTZNA/']], u'Thursday': [[u'13:00', u'/fanatic/booking-interactive/s75/p86960000023DFBTZNA/'], [u'15:30', u'/fanatic/booking-interactive/s75/p96960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/pA6960000023DFBTZNA/'], [u'21:30', u'/fanatic/booking-interactive/s75/pB6960000023DFBTZNA/']]}], u'Keith Lemon: The Film': [u'f13886', {u'Wednesday': [[u'14:00', u'/fanatic/booking-interactive/s75/p3A960000023DFBTZNA/'], [u'20:30', u'/fanatic/booking-interactive/s75/p33960000023DFBTZNA/']], u'Thursday': [[u'14:00', u'/fanatic/booking-interactive/s75/p4A960000023DFBTZNA/'], [u'20:30',
# OUT: {u'name': u'ODEON Camden', u'chain_id': u's75', u'times': {u'Brave 2D': [u'f12841', {u'Wednesday': [[u'15:00', u'/fanatic/booking-interactive/s75/p13960000023DFBTZNA/'], [u'17:30', u'/fanatic/booking-interactive/s75/p23960000023DFBTZNA/']], u'Thursday': [[u'15:00', u'/fanatic/booking-interactive/s75/p53960000023DFBTZNA/'], [u'17:30', u'/fanatic/booking-interactive/s75/p63960000023DFBTZNA/']]}], u'Fat Boy Slim Live: From The Big Beach Bootique': [u'f14110', {}], u'Brave 3D': [u'f100416', {u'Wednesday': [[u'12:30', u'/fanatic/booking-interactive/s75/p03960000023DFBTZNA/']], u'Thursday': [[u'12:30', u'/fanatic/booking-interactive/s75/p43960000023DFBTZNA/']]}], u'The Bourne Legacy': [u'f13170', {u'Wednesday': [[u'15:00', u'/fanatic/booking-interactive/s75/pD4960000023DFBTZNA/'], [u'18:00', u'/fanatic/booking-interactive/s75/pE4960000023DFBTZNA/'], [u'21:00', u'/fanatic/booking-interactive/s75/pF4960000023DFBTZNA/']], u'Thursday': [[u'15:00', u'/fanatic/booking-interactive/s75/p05960000023DFBTZNA/'], [u'18:00', u'/fanatic/booking-interactive/s75/p15960000023DFBTZNA/'], [u'21:00', u'/fanatic/booking-interactive/s75/p25960000023DFBTZNA/']]}], u'Ted': [u'f13390', {u'Wednesday': [[u'16:00', u'/fanatic/booking-interactive/s75/p89960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p99960000023DFBTZNA/'], [u'21:15', u'/fanatic/booking-interactive/s75/pE9960000023DFBTZNA/']], u'Thursday': [[u'16:00', u'/fanatic/booking-interactive/s75/p1A960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p0A960000023DFBTZNA/'], [u'21:15', u'/fanatic/booking-interactive/s75/pF9960000023DFBTZNA/']]}], u'The Dark Knight Rises': [u'f13222', {u'Wednesday': [[u'13:30', u'/fanatic/booking-interactive/s75/p28960000023DFBTZNA/'], [u'16:45', u'/fanatic/booking-interactive/s75/p38960000023DFBTZNA/'], [u'20:15', u'/fanatic/booking-interactive/s75/p48960000023DFBTZNA/']], u'Thursday': [[u'13:30', u'/fanatic/booking-interactive/s75/p58960000023DFBTZNA/'], [u'16:45', u'/fanatic/booking-interactive/s75/p68960000023DFBTZNA/'], [u'20:15', u'/fanatic/booking-interactive/s75/p78960000023DFBTZNA/']]}], u'Total Recall': [u'f13978', {u'Wednesday': [[u'13:00', u'/fanatic/booking-interactive/s75/p46960000023DFBTZNA/'], [u'15:30', u'/fanatic/booking-interactive/s75/p56960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/p66960000023DFBTZNA/'], [u'21:30', u'/fanatic/booking-interactive/s75/p76960000023DFBTZNA/']], u'Thursday': [[u'13:00', u'/fanatic/booking-interactive/s75/p86960000023DFBTZNA/'], [u'15:30', u'/fanatic/booking-interactive/s75/p96960000023DFBTZNA/'], [u'18:30', u'/fanatic/booking-interactive/s75/pA6960000023DFBTZNA/'], [u'21:30', u'/fanatic/booking-interactive/s75/pB6960000023DFBTZNA/']]}], u'Keith Lemon: The Film': [u'f13886', {u'Wednesday': [[u'14:00', u'/fanatic/booking-interactive/s75/p3A960000023DFBTZNA/'], [u'20:30', u'/fanatic/booking-interactive/s75/p33960000023DFBTZNA/']], u'Thursday': [[u'14:00', u'/fanatic/booking-interactive/s75/p4A960000023DFBTZNA/'], [u'20:30', u'/fanatic/booking-interactive/s75/p73960000023DFBTZNA/']]}]}, u'address': u'London, NW1 7AA, United Kingdom, London, United Kingdom', u'lat': 51.538424, u'lng': -0.14219}
from LoudPopcorn.pipelines import *

class Spider():
	chain = "Odeon"

s = Spider()

error_list = []

for i in range(len(data)):
	try:
		c = ProcessCinemaPipeline()
		c.process_item(data[i], s)

		p = ProcessFilmTimes()
		p.process_item(data[i] , None)
		
		text = colored('PASSED', 'green',)
		print("Cinema Number %s \t[" %str(i)+text+"]")
	except Exception as e:
		text = colored('%s'%str(e), 'red',)
		print(text)
		error_list.append(str(e)) 

		with open("errors.txt", "a") as myfile:
			myfile.write(str(data[i]) +"\n" + str(e))
