import wolframalpha
import wikipedia

while True:
	usrinput = input("Question: ")
	#wikipedia.set_lang("es")<to change language of wiki to spanish>
	if usrinput == "quit" or usrinput == "exit":
		break
	try:
		app_id = "36UY6L-X5VXYHR59R"
		client = wolframalpha.Client(app_id)

		res = client.query(usrinput)
		answer = next(res.results).text
		print(answer)
	except:
		print(wikipedia.summary(usrinput, sentences=5))


input("bye")