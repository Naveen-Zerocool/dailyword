import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def getword():
	url = "http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=your_api_key_from_wordnik"
	response = requests.get(url)
	js = response.json()
	word = js["word"]
	note =  js["note"]
	defn = js["definitions"][0]["text"]
	wpos = js["definitions"][0]["partOfSpeech"]
	ex1 = js["examples"][0]["text"]
	addnl = "\n\n\n\n\n\n\nNote: Its an automated script, let me know for changes or suggestions"
	sndmal="""\
		<html>
			<body>
				<p>
					<h1>Word Of Day: </h1>
					<h2>%s</h2><br>
					<h3>
					<b><u>Definition</u> :</b>%s<br><br>
					<b><u>Note</u> : </b>%s<br><br>
					<b><u>Part Of Speech</u> : </b>%s<br><br>
					<b><u>Example</u> : </b>%s<br><br>
					<i>%s</i>
					</h3>
				</p>
			</body>
		</html>
"""%(word,defn,note,wpos,ex1,addnl)
	return sndmal

def main():
	words=getword()
	send = MIMEMultipart()
	send['From'] = "abc@xxx.com"
	send['To'] =  "def@xxx.com"
	send['Subject'] = "Daily Word"
	body = words
	send.attach(MIMEText(body, 'html'))
	text = send.as_string()
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("sendermail@domain.com", "password")
	server.sendmail("sendermail@domain.com", "receiver@domain.com", text)
	server.quit()

if __name__ == "__main__":
	main()
