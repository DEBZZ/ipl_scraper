import scrapy
from scrapy_splash import SplashRequest

class IplDataSpider(scrapy.Spider):
    name = "ipldata"
    start_urls = ['https://www.iplt20.com/matches/results/men/2022']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 10},
                                )

    def parse(self, response):
        for data in response.css('div.vn-shedule-desk'):
            yield {
                'Match No': data.css("div.vn-venueDet div.vn-date::text").get().split('|')[0].strip(),
                'Date': data.css("div.vn-venueDet div.vn-date::text").get().split('|')[1].strip().replace('"',''),
                'Venue': data.css("div.vn-matchTime span::text").get().replace(',','').strip(),
                '1st Team': data.css("div.vn-teamTitle h3::text").get(),
                '1st Team Run': data.css("div.vn-teamTitle p::text").get(),
                '2nd Team': data.css("div.vn-teamTitle h3::text").getall()[2],
                '2nd Team Run': data.css("div.vn-teamTitle p::text").extract()[1],
                'Result': data.css("div.vn-ticketTitle::text").get()
            }