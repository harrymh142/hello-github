from GoogleNews import GoogleNews

news = GoogleNews('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')
print(news.getForYou())