import socket
import geoip2.database
import math

# find my ip
myIP=socket.gethostbyname(socket.gethostname())

# Open file containing ip list
f= open("targets.txt", 'r')

# Open reader to geo database
reader = geoip2.database.Reader('../GeoLite2-City.mmdb')

for c in range (0, 10, 1):
    # pull ip from file
    dest_ip = f.readline()

    # Cut separation characters from string
    cut = len(dest_ip) - 1
    dest_ip = dest_ip[0:cut]

    # find lat lon variables
    home = reader.city(myIP)
    away = reader.city(dest_ip)

    awayLat = away.location.latitude
    awayLon = away.location.longitude

    homeLat = home.location.latitude
    homeLon = home.location.longitude

    # haversine formula
    radius = 6371
    homeLat = math.radians(homeLat)
    homeLon = math.radians(homeLon)

    awayLat = math.radians(awayLat)
    awayLon = math.radians(awayLon)

    dLat = awayLat-homeLat
    dLon = awayLon - homeLon

    a = math.sin(dLat/2)**2 + math.cos(homeLat) * math.cos(awayLat) * math.sin(dLon/2)**2
    b = 2*math.asin(a)
    d = radius * b

    print "Distance is: ", d, "km"

reader.close()