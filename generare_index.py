# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]
ranges = [["Время", times], ["Призывы", advices], ["Суть", promises]]


def generate_page(head, body):
	page = '''<meta charset="UTF-8"><html>''' + head + body + "</html>"
	return page

def generate_head(title):
	head = "<title>" + title + "</title>"
	return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
	body = "<h1>" + header + "</h1>"
	i = 0
	while i < len(paragraphs):
		body = body + "<p>" + paragraphs[i] + "</p>"
		i += 1
	body += '''<hr><br><p><a href="about.html">О проекте</p></p>'''
	return "<body>" + body + "</body>"

def generate_a_body():
	body = '''
	<h1>О чем этот проект</h1>
	<img src="11.jpg" height="100" width="100">
	<br>
	<ol>'''
	for p in ranges:
		body += f"<li>{p[0]}</li><ul>"
		for n in p[1]:
			body += f"<li>{n.capitalize()}</li>"
		body += "</ul>"
	body += "</ol>"

	body += '''<hr><br><p><a href="index.html">Main</p></p>'''
	return "<body>" + body + "</body>"



def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head = generate_head(title),
		body = generate_body(header = header, paragraphs = paragraphs)
	)
	print(page, file=fp)
	fp.close()

def generate_about():
	ap = open("about.html", "w")
	page = generate_page(
		head = generate_head("About"),
		body = generate_a_body()
	)
	print(page, file=ap)
	ap.close()


today = dt.now().date()
generate_about()
save_page(
	title = "Гороскоп на сегодня",
	header = "Что день " + str(today) + " готовит",
	paragraphs = generate_prophecies())