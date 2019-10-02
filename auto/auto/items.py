# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    brand_name = scrapy.Field()
    pass


class AutoItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    brand_name = scrapy.Field()
    modele = scrapy.Field()
    s_modele = scrapy.Field()
    prix = scrapy.Field()
    remise = scrapy.Field()
    Moteur = scrapy.Field()
    Puissance = scrapy.Field()
    Boite = scrapy.Field()
    rapport = scrapy.Field()
    Energie = scrapy.Field()
    cylindres = scrapy.Field()
    Couple = scrapy.Field()
    Reservoir = scrapy.Field()
    Vitesse_max = scrapy.Field()
    zero_cent_kmh = scrapy.Field()
    turbo = scrapy.Field()
    Longueur = scrapy.Field()
    Largueur = scrapy.Field()
    Hauteur = scrapy.Field()
    Empattement = scrapy.Field()
    Places = scrapy.Field()
    Portes = scrapy.Field()
    Limiteur_vitesse = scrapy.Field()
    ABS = scrapy.Field()
    AFU = scrapy.Field()
    ESP = scrapy.Field()
    Airbag = scrapy.Field()
    Verouillage = scrapy.Field()
    Isofix = scrapy.Field()
    Pression_pneus = scrapy.Field()
    angle_mort = scrapy.Field()
    Climatisation = scrapy.Field()
    Radar_recul = scrapy.Field()
    Ordinateur_bord = scrapy.Field()
    Accoudoir = scrapy.Field()
    Ecran = scrapy.Field()
    Bluetooth = scrapy.Field()
    Volant_cuir = scrapy.Field()
    Commandes_volant = scrapy.Field()
    Retroviseurs = scrapy.Field()
    Vitres_electriques = scrapy.Field()
    luminosité = scrapy.Field()
    pluie = scrapy.Field()
    anti_brouillard = scrapy.Field()
    Feux_avants = scrapy.Field()
    Feux_arriéres = scrapy.Field()
    Toit = scrapy.Field()
    Jantes = scrapy.Field()
    Vitres_teintés = scrapy.Field()

    pass
