from gnews import GNews
import ollama
google_news = GNews()


#gnews stuff
query = input('Name any topic to learn about: ')
print("Scanning the web for articles on " + query + "...")

search = google_news.get_news(query)

article = google_news.get_full_article(search[0]['url'])


#for i in range(0,10):
#    print(str(i) + ". " +  search[i]['title'])


#ollama stuff
ollama.pull('llama3')


modelfile='''
FROM llama3
SYSTEM You are a news chatbot named Zeno. You are given a news article on a certain topic. In your first message, summarize the article in 3 bullet points. Each bullet point should have no more than 8 words. Then afterwards, continually answer questions by the user. All of your language should be concise and informative.
'''



ollama.create(model='newModel', modelfile=modelfile)
question = ''
index = 0
msgs = [{'role': 'user', 'content': "Read this article: " + article.text}]
while question != 'exit':
    if index != 0:
        question = input('\nQ:')
    msgs.append({'role': 'user', 'content': question})
    stream = ollama.chat(
        model='newModel',
        messages=msgs,
        stream=True,
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        msgs.append({'role': 'system', 'content': chunk['message']['content']})
    index += 1



