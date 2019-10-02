# -*- coding: utf-8 -*-
import scrapy

from auto.items import BrandItem;
from auto.items import AutoItem;
from pprint import pprint


class AutoScraperSpider(scrapy.Spider):
    name = 'auto_scraper'

    start_urls = ['https://www.autobip.com/prix-du-neuf']

    def parse(self, response):
        try:
            items = response.css("body > div > div.single-entry.single-entry--template-4-alt > div > div > div > div.page-sidebar-content.pt-4 > div.row.row--space-between > div > article > div.post__thumb > a")

            for item in items:
                image_url = item.css('div.background-img::attr(style)').re(r"http.*.png")
                yield scrapy.Request(item.css('a::attr(href)').get(), self.parseBrands, meta={'image_url': image_url})
        except Exception:
            print('///////// ERROR')


    def parseBrands(self, response):
        # SAVE THE BRAND NAME AND IMAGE
        image_url = response.meta.get('image_url')
        item = BrandItem(image_urls=image_url)
        item['brand_name'] = response.css(".mnmd-news-ticker.mnmd-block--contiguous.mnmd-news-ticker--fw > div > ul > li:nth-child(2) > a > span::text").get()
        yield item

        # FOLLOW MODELS LINKS
        try:
            urls = response.css(".page-sidebar-content > div:nth-child(3) .post__title a::attr(href)").getall()
            response.css(".page-sidebar .post__title  a::attr(href)").getall()
            for url in urls:
                yield scrapy.Request(url, self.parseModels)
        except Exception:
            print('///////// ERROR')

    def parseModels(self, response):
        # FOLLOW MODELS LINKS
        try:
            urls = response.css(".page-sidebar-content > div:nth-child(3) .post__title a::attr(href)").getall()
            response.css(".page-sidebar .post__title  a::attr(href)").getall()
            if len(urls) != 0:
                for url in urls:
                    yield scrapy.Request(url, self.parseModels)
            else:
                auto = AutoItem()
                auto['image_urls'] = [response.css('div.page-sidebar-content.pt-3 > div.row.price-details.my-4 > div.d-none.d-md-block.col-md-4 > div > a > img::attr(src)').get()]
                auto['brand_name'] = response.css(".mnmd-news-ticker.mnmd-block--contiguous.mnmd-news-ticker--fw > div > ul > li:nth-child(2) > a > span::text").get()
                auto['modele'] = response.css(".mnmd-news-ticker.mnmd-block--contiguous.mnmd-news-ticker--fw > div > ul > li:nth-child(3) > a > span::text").get()
                auto['s_modele'] = response.css("div.page-sidebar-content.pt-3 > div.row.price-details.my-4 > div.col-12.col-md-8 > div > div:nth-child(2) > span::text").get()
                auto['prix'] = response.css("div.page-sidebar-content.pt-3 > div.row.price-details.my-4 > div.col-12.col-md-8 > div > div:nth-child(6) > span::text").get()
                auto['Moteur'] = response.css("div.page-sidebar-content.pt-3 > div.row.price-details.my-4 > div.col-12.col-md-8 > div > div:nth-child(4) > span::text").get()
                auto['Puissance'] = response.xpath('//div[text()="Puissance"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                try:
                    auto['Boite'] = response.xpath('//div[text()="Boite"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Boite')

                try:
                    auto['rapport'] = response.xpath('//div[text()="Boite rapports"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// rapport')

                try:
                    auto['Energie'] = response.xpath('//div[text()="Energie"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Energie')

                try:
                    auto['cylindres'] = response.xpath('//div[text()="Nbr cylindres"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// cylindres')

                try:
                    auto['Couple'] = response.xpath('//div[text()="Couple"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Couple')

                try:
                    auto['Reservoir'] = response.xpath('//div[text()="Reservoir"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Reservoir')

                try:
                    auto['Vitesse_max'] = response.xpath('//div[text()="Vitesse max"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\ km)')[0]
                except Exception:
                    print('///////// Vitesse_max')

                try:
                    auto['zero_cent_kmh'] = response.xpath('//div[text()="Acceleration de 0 à 100"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// zero_cent_kmh')

                try:
                    auto['turbo'] = response.xpath('//div[text()="Turbo"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// turbo')

                try:
                    auto['Longueur'] = response.xpath('//div[text()="Longueur"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Longueur')

                try:
                    auto['Largueur'] = response.xpath('//div[text()="Largueur"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Largueur')

                try:
                    auto['Hauteur'] = response.xpath('//div[text()="Hauteur"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Hauteur')

                try:
                    auto['Empattement'] = response.xpath('//div[text()="Empattement"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Empattement')

                try:
                    auto['Places'] = response.xpath('//div[text()="Places"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Places')


                try:
                    auto['Portes'] = response.xpath('//div[text()="Portes"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Portes')

                try:
                    auto['Limiteur_vitesse'] = response.xpath('//div[text()="Limiteur de vitesse"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Limiteur_vitesse')

                try:
                    auto['ABS'] = 1 if response.xpath('//div[text()="ABS"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// ABS')

                try:
                    auto['AFU'] = 1 if response.xpath('//div[text()="AFU"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// AFU')

                try:
                    auto['ESP'] = 1 if response.xpath('//div[text()="ESP"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// ESP')


                try:
                    auto['Airbag'] = response.xpath('//div[text()="Airbag"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Airbag')

                try:
                    auto['Verouillage'] = 1 if response.xpath('//div[text()="Verouillage centralisé"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Verouillage')

                try:
                    auto['Isofix'] = response.xpath('//div[text()="Isofix"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Isofix')

                try:
                    auto['Pression_pneus'] = 1 if response.xpath('//div[text()="Pression pneus"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Pression_pneus')

                try:
                    auto['angle_mort'] = 1 if response.xpath('//div[text()="Détecteur d\'angle mort"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// angle_mort')

                try:
                    auto['Climatisation'] = response.xpath('//div[text()="Climatisation"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Climatisation')

                try:
                    try:
                        auto['Radar_recul'] = None if response.xpath('//div[text()="Radar de recul"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['Radar_recul'] = response.xpath('//div[text()="Radar de recul"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Radar_recul')

                try:
                    auto['Ordinateur_bord'] = 1 if response.xpath('//div[text()="Ordinateur de bord"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Ordinateur_bord')

                try:
                    try:
                        auto['Accoudoir'] = None if response.xpath('//div[text()="Accoudoir"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['Accoudoir'] = response.xpath('//div[text()="Accoudoir"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Accoudoir')

                try:
                    try:
                        auto['Ecran'] = None if response.xpath('//div[text()="Ecran"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['Ecran'] = response.xpath('//div[text()="Ecran"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Ecran')

                try:
                    auto['Bluetooth'] = 1 if response.xpath('//div[text()="Bluetooth"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Bluetooth')

                try:
                    auto['Volant_cuir'] = 1 if response.xpath('//div[text()="Volant cuir"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Volant_cuir')

                try:
                    auto['Commandes_volant'] = 1 if response.xpath('//div[text()="Commandes aux volant"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Commandes_volant')

                try:
                    try:
                        auto['Retroviseurs'] = None if response.xpath('//div[text()="Retroviseurs électriques"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['Retroviseurs'] = response.xpath('//div[text()="Retroviseurs électriques"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Retroviseurs')

                try:
                    try:
                        auto['Vitres_electriques'] = None if response.xpath('//div[text()="Vitres électriques"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['Vitres_electriques'] = response.xpath('//div[text()="Vitres électriques"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Vitres_electriques')

                try:
                    auto['luminosité'] = 1 if response.xpath('//div[text()="Détécteur de luminosité"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// luminosité')

                try:
                    auto['pluie'] = 1 if response.xpath('//div[text()="Detecteur de pluie"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// pluie')

                try:
                    try:
                        auto['anti_brouillard'] = None if response.xpath('//div[text()="Feux anti brouillard"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else 1
                    except Exception:
                        auto['anti_brouillard'] = response.xpath('//div[text()="Feux anti brouillard"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// anti_brouillard')

                try:
                    auto['Feux_avants'] = response.xpath('//div[text()="Feux avants"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Feux_avants')

                try:
                    auto['Feux_arriéres'] = response.xpath('//div[text()="Feux arriéres"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Feux_arriéres')

                try:
                    auto['Toit'] = 1 if response.xpath('//div[text()="Toit"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'yes' else 0
                except Exception:
                    print('///////// Toit')

                try:
                    auto['Jantes'] = response.xpath('//div[text()="Jantes"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Jantes')

                try:
                    try:
                        auto['Vitres_teintés'] = 0 if response.xpath('//div[text()="Vitres teintés"]/..').css('div.col-12 + div .price-td-value img::attr("src")').re('(?<=img/)(.*?)(?=.png)')[0] == 'no' else  1
                    except Exception:
                        auto['Vitres_teintés'] = response.xpath('//div[text()="Vitres teintés"]/..').css('div.col-12 + div .price-td-value::text').re('(?<=\\n)(.*?)(?=\\n)')[0]
                except Exception:
                    print('///////// Vitres_teintés')


                yield auto

        except Exception:
            print('ERROR')