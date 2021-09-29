import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://www.zyte.com/blog/page/1/',
        'https://www.zyte.com/blog/page/2/'
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        print("Je suis iciiiiiii \n\n\n\n\n\n\n",page,"Je suis iciiiiiii ")
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
