import phonenumbers

from test import number

#elow c is for country and h is for history
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,'CH')
location=geocoder.description_for_number(ch_number,'en')
print(location)


#carrier is to provide about the service provided
from phonenumbers import carrier
service_num=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_num,'en'))

from opencage.geocoder import OpenCageGeocode
key="d2bf116a4649481484eb5e237f1e4400"
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
# print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

import folium

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("mylocation.html")


print(lat,lng)

