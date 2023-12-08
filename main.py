from scrapy.crawler import CrawlerProcess

from scary_py.scary_py.spiders import authors, quotes


process_authors = CrawlerProcess()
process_quotes = CrawlerProcess()
process_authors.crawl(authors.AuthorsSpider)
process_quotes.crawl(quotes.QuotesSpider)
process_authors.start()
process_quotes.start()
