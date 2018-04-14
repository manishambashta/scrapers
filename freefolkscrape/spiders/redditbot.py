# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/freefolk/']
    start_urls = ['http://www.reddit.com/r/freefolk//']

    def parse(self, response):
        titles = response.css(".title.may-blank::text").extract()
        comments = response.css(".entry.unvoted .first>a::text").extract()
        votes = response.css(".score.unvoted::text").extract()
        times = response.css("time::attr('title')").extract()

        # save the extracted content in a dictionary
        for item in zip(titles, votes, comments, times):
            scraped_info = {
                'title': item[0],
                'votes': item[1],
                'comments': item[2],
                'created_at': item[3]
            }
            yield scraped_info

