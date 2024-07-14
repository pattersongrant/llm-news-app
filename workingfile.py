from gnews import GNews
import ollama
google_news = GNews()


#gnews stuff
#search = google_news.get_news('tottenham hotspur')
#
#article = google_news.get_full_article(search[0]['url'])
#
#print(article.text)
#
#for i in range(0,10):
#    print(str(i) + ". " +  search[i]['title'])


#ollama stuff
ollama.pull('llama3')


modelfile=('''
FROM llama3
SYSTEM You are a news chatbot who reads articles from the internet and answers questions about them. Your name is Zeno.
''')
ollama.create(model='newModel', modelfile=modelfile)
num = 2
question = ''
while question != 'exit':
    question = input('\n')
    stream = ollama.chat(
        model='newModel',
        messages=[{'role': 'user', 'content': "\n" + question}],
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)



