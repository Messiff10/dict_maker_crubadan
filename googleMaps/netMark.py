from geotext import GeoText
import geograpy
import nltk
import cre
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
text=GeoText("ShenZhen Jin hua,China,London,USA,usa,北京西城北三环中路辅路,China,India,the United Stated,U.K.,Brazil,Pakistan,Nigeria,Bangladesh,Russia,Mexico")
# print(text.cities)
# print(text.countries)
# print(text.nationalities)
# print(text.country_mentions)

url="ShenZhen Jin hua,China,London,USA,usa,北京西城北三环中路辅路,China,India,the United Stated,U.K.,Brazil,Pakistan,Nigeria,Bangladesh,Russia,Mexico"
places = geograpy.get_place_context(text=url)
places.set_countries()
print(places.countries)
places.set_cities()
print(places.cities)
# print(places.countries)