## Daniel Brotman
## Network Distance Finder
## 4/26/2016

# Usage
# distMeasurement.py

This program will return hop count, rtt, and number of bytes returned from original datagram through ICMP
messages. Exactly 10 IP addresses must be stored in the file targets.txt. To execute run the command:
_sudo python distMeasurement.py_ in the terminal.

# geoDistance.py

This program will give approximate geographic distance between two IP addresses.  The distance is calculated using the GeoIP2_City
database which must be stored in the directory one level above this program. IP addresses are read from targets.txt for
exactly 10 addresses. Distance is measured using the Haversine great-circle equation. Executed via _sudo python geoDistance.py_ in terminal.

# Credits

Credit to:
## Socket Structure: https://blogs.oracle.com/ksplice/entry/learning_by_doing_writing_your
## Austin Fedyt apf31@case.edu for ICMP parsing
## Haversine formula: http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points