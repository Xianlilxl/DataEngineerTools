import scrapy

"""class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            text_value = re.findall(r"“(.+?)”",text_value)[0]
            yield { 'text' : text_value }"""



class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        import re
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]/article'):
            text_value = cit.xpath('div[@class="figsco__quote__text"]/a/text()').extract_first()
            text_value = re.findall(r"“(.+?)”",text_value)[0]
            auteur_value = cit.xpath('div[@class="figsco__quote__from figsco__row"]/div[@class="figsco__fake__col-9"]/a/text()').extract_first()
            yield { 'text' : text_value, 'auteur' : auteur_value }



"""
<li class="figsco__selection__list__evene__list__item">
<article>
  
    <div class="figsco__quote__text"><a href="http://evene.lefigaro.fr/citation/angleterre-ecroule-ordre-france-releve-desordre-27177.php">“L’Angleterre s’écroule dans l’ordre, et la France se relève dans le désordre.”</a></div>
        <div class="figsco__quote__from figsco__row">
            <div class="figsco__fake__col-1">
                    <a href="/celebre/biographie/winston-churchill-675.php"><img src="http://image2.evene.fr/files/imagecache/scope_40_40/celebrity/675.jpg" alt="Winston Churchill" title="Winston Churchill" width="40" height="40" class="  lazyloaded"></a>          </div>
            <div class="figsco__fake__col-9">
                    De <a href="/celebre/biographie/winston-churchill-675.php">Winston Churchill</a>                  <br>
                        </div>
  </div>
</article>
    </li>"""