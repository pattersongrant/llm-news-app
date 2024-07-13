from gnews import GNews

google_news = GNews()

search = google_news.get_news('ann arbor')

article = google_news.get_full_article(search[0]['url'])

print(article.text)

#for i in range(0,10):
#    print(str(i) + ". " +  search[i]['title'])