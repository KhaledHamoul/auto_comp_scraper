# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pprint import pprint
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True
}


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        images = [x for ok, x in results if ok]
        if not images:
            raise DropItem("Item contains no images")
        item['images'] = images
        return item


class AutoPipeline(object):
    cnx = None
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print("Something is wrong with your user name or password" + err)

    def process_item(self, item, spider):
        # Implement the data store code here depending to the item type (check one of its filed)
        # if 'brand_name' in item.fields
        cursor = self.cnx.cursor()

        if 'prix' in item.fields:
            print('auto')
            cursor.execute('SELECT * FROM marques_autos where marque = "' + item['brand_name'] + '"')
            myresult = cursor.fetchall()

            sql = "INSERT INTO voitures (image, Moteur,	Puissance,	Boite_vitesse , Rapports_vitesse,	Energie,	Nombre_cylindres,	Couple,	Reservoir,	Vitesse_max,	zero_cent, Longueur,	Largeur,	Hauteur,	Empattement,	Nombre_places,	Nombre_portes,	Regulateur,	ABS,	AFU,	ESP,	Airbags,	Verouillage,	isofix,	ctrl_pression_pneus,	Detecteur_angle_mort,	Climatisation,	Radar_recul, Ordinateur_bord, Accoudoir,	Ecran_tactile,	Bluetooth,	Volant_cuir,	Commandes_volant,	Retroviseurs_electriques,	Vitres_electriques,	Detecteur_luminosite,	Detecteur_pluie,	Feux_anti_brouillard,	Feux_avant,	Feux_arriere,	Toit_verre,	Jantes,	Vitres_teintees, turbo,	modele,	finition, prix, id_marque) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            val = (
                   item['images'][0]['path'],
                   item.get('Moteur', None),
                   item.get('Puissance', None),
                   item.get('Boite', None),
                   item.get('rapport', None),
                   0 if 'Essence' in item.get('Energie', None)  else 1,
                   item.get('cylindres', None),
                   item.get('Couple', None),
                   item.get('Reservoir', None),
                   item.get('Vitesse_max', None),
                   item.get('zero_cent_kmh', None),
                   item.get('Longueur', None),
                   item.get('Largueur', None),
                   item.get('Hauteur', None),
                   item.get('Empattement', None),
                   int(item.get('Places', None)),
                   int(item.get('Portes', None)),
                   item.get('Limiteur_vitesse', None),
                   item.get('ABS', None),
                   item.get('AFU', None),
                   item.get('ESP', None),
                   int(item.get('Airbag', None)),
                   item.get('Verouillage', None),
                   1 if 'ISOFIX' in item.get('Isofix', None) else 0,
                   item.get('Pression_pneus', None),
                   item.get('angle_mort', None),
                   item.get('Climatisation', None),
                   item.get('Radar_recul', None),
                   item.get('Ordinateur_bord', None),
                   item.get('Accoudoir', None),
                   item.get('Ecran', None),
                   item.get('Bluetooth', None),
                   item.get('Volant_cuir', None),
                   item.get('Commandes_volant', None),
                   item.get('Retroviseurs', None),
                   item.get('Vitres_electriques', None),
                   item.get('luminosité', None),
                   item.get('pluie', None),
                   item.get('anti_brouillard', None),
                   item.get('Feux_avants', None),
                   item.get('Feux_arriéres', None),
                   item.get('Toit', None),
                   item.get('Jantes', None),
                   item.get('Vitres_teintés', None),
                   item.get('turbo', None),
                   item.get('modele', None),
                   item.get('s_modele', None),
                   item.get('prix', None),
                   myresult[0][0]
                   )
            cursor.execute(sql, val)
            self.cnx.commit()

        else:
            print('brand')
            sql = "INSERT INTO marques_autos (marque, logo) VALUES (%s, %s)"
            val = (item['brand_name'], item['images'][0]['path'])
            cursor.execute(sql, val)
            self.cnx.commit()
        return item
