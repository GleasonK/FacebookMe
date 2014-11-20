import urllib, urllib2, re
import writeHTML


class Person(object):
	def __init__(self, index, url, pic, cover):
		self.index = index
		self.url   = url
		self.pic   = pic
		self.cover = cover

	def __unicode__(self):
		return str(self.index) + "," + self.url + "," + self.pic + "," + self.cover

	def __str__(self):
		return str(self.index) + "," + self.url + "," + self.pic + "," + self.cover

	def __repr__(self):
		return str(self.index) + "," + self.url + "," + self.pic + "," + self.cover

def fb_scrape(name, s_range=25):
	fname,lname = name.split(" ")
	people = []
	for i in range(s_range):
		try: 
			url = "https://www.facebook.com/" + fname + "." + lname + "." + str(i)
			if i==0:
				url = "https://www.facebook.com/" + fname + "." + lname
			
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			response  = urllib2.urlopen(req)
			resp_text = response.read()

			pic_reg = re.compile(r'<img class=\"profilePic.*src="([A-Za-z0-9:/\-\._\?=&;]*)')
			pic_mat = pic_reg.search(resp_text)

			cover_reg = re.compile(r'<img class=\"coverPhotoImg.*src="([A-Za-z0-9:/\-\._\?=&;]*)')
			cover_mat = cover_reg.search(resp_text)

			### INFO NO GOOD YET
			# info_reg = re.compile(r'(<li class="_4_ug">([\s\w,\.]+)<a.*">([\s\w,\.]+)</a></li>)')
			# info_mat = info_reg.findall(resp_text)
			# print info_mat
			print url
			people.append(Person(i,url,pic_mat.group(1),cover_mat.group(1)))
		except AttributeError:
			try:
				people.append(Person(i,url,pic_mat.group(1),""))
			except AttributeError:
				people.append(Person(i,url,"",""))
		except urllib2.HTTPError:
		 	print "Failed on " + str(i) 

	return people

def main():
	# name = "Kevin Gleason"
	name = raw_input('Enter your name: ')
	people = fb_scrape(name, 1000)
	html = writeHTML.HTMLWriter(name, people)
	x = html.writeFile()
	print x

if __name__=="__main__":
	main()
	

