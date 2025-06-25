import mysql.connector as mc

db = mc.connect (host = "...", port = 0, user = "...", password = "...", database = "...") # Removed data for security reasons
cursor = db.cursor ()

# sql = "SHOW DATABASES"
# sql = "SELECT * FROM city WHERE population > 5000000 ORDER BY population DESC LIMIT 10"
# sql = "SELECT name, continent, population FROM country WHERE population > 100000000 ORDER BY population DESC LIMIT 10"

# e = input ("Welches Land: ")
# sql = "SELECT country.name, country.continent, countrylanguage.language FROM country, countrylanguage WHERE country.code = countrylanguage.countrycode AND country.name LIKE %s"

e = input ("Welches Land: ")
sql = "SELECT city.name, country.name, country.lifeexpectancy FROM country, city WHERE city.countrycode = country.code AND country.name LIKE %s ORDER BY city.name"
cursor.execute (sql, [e])
daten = cursor.fetchall ()
db.close ()

if daten: print ("Stadt                 | Land                | Lebenserwartung")
for ds in daten:
    print (f"{ds[0]:22}| {ds[1]:20}| {ds[2]:.2f}")
