import scrapy


class TokpedSetSpider(scrapy.Spider):
    print("class TokpedSetSpider")
    name = "tokped_spider"
    start_urls = ['https://www.tokopedia.com/vaporlab?sort=8']

    def parse(self, response):
        SET_SELECTOR = '.css-1nyq18m'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h3 ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }
            print("for")
        #     NAME_SELECTOR = 'h1 ::text'
        #     PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        #     MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
        #     IMAGE_SELECTOR = 'img ::attr(src)'
        #     yield {
        #         'name': brickset.css(NAME_SELECTOR).extract_first(),
        #         'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
        #         'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
        #         'image': brickset.css(IMAGE_SELECTOR).extract_first(),
        #     }
        #
        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )

        print(response.css)