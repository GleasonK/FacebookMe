# File: writeHTML.py
# Author: Kevin Gleason

class HTMLWriter(object):

	header = \
	'''
	<html>
	<head>
		<title>%s %s | FacebookMe</title>
	</head>
	<body style='text-align:center;background:#3b5998;color:white;'>
	'''  ## % (fname, lname)

	top_text = "<center><h1 style='margin:15px 0 10px 0;'><i>FacebookMe</i></h1></center>\
	<center><h1 style='margin:5px 0 10px 0;'>The %s %s of Facebook</h1></center>"
	extra = "<div style='background:rgba(255,255,255,0.75);width:92%;padding:15px;border-radius:10px;margin:0 auto;'>"

	footer="</div><center><p><i>FacebookMe by Kevin Gleason<i></p></center></body></html>"


	def __init__(self, name, people):
		names = name.split(" ")
		self.fname, self.lname = names 
		self.people=people

	def writeLine(self, person):
		entry= "\
		<div style='display:inline-block;width:200px;height:200px;'>\
			<a href='"+person.url+"'><img style='width:200px;height:200px' src='" + person.pic + "'/></a>\
		</div>"
		return entry

	def writeLines(self):
		html=""
		for person in self.people:
			html+= self.writeLine(person)
		return html

	def getPluralName(self):
		lname_plural = self.lname if self.lname.endswith("s") else self.lname + "s"
		return (self.fname,lname_plural)

	def writeFile(self):
		fout = open(self.fname[0]+"_"+self.lname+"_Creep.html","w")
		fout.write(self.header % (self.fname, self.lname))
		fout.write(self.top_text % (self.getPluralName()))
		fout.write(self.extra)
		fout.write(self.writeLines())
		fout.write(self.footer)
		fout.close()




