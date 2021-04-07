import geopandas as gpd
import geoplot as gplt
import matplotlib.pyplot as plt
import mysql.connector
from descartes import PolygonPatch

color_official_or_national = ['#0000ff', '#006600', '#ff0000', '#ff9900', '#660066', '#595959', '#666633']
color_widely = ['#3399ff', '#00b300', '#ff4d4d', '#ffad33', '#b300b3', '#808080', '#888844']
color_regional_or_minority = ['#66ccff', '#66ff66', '#ff8080', '#ffcc80', '#ff99ff', '#a6a6a6', '#bbbb77']

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="",
    database="maps"
)
mycursor = mydb.cursor()

def toList(s):
    l =[]
    for i in s:
        i = str(i)
        i = i.replace('(', '')
        i = i.replace(')', '')
        i = i.replace(',', '')
        i = i.replace('\'', '')
        l.append(i)
    return l


def query(language, column):
    mycursor.execute("SELECT country_name FROM country_list WHERE LOCATE('" + str(language) + "', " + str(column) + ");")
    query_results = mycursor.fetchall()
    query_results = toList(query_results)
    return query_results

languages_spoken = []
x = 'language'
y = 0

while x != '' and  y <= 6:
    x = input('Insert spoken language:')
    if x != '':
        languages_spoken.append(x)
        y += 1
    print(languages_spoken)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.name != "Antarctica")]

'''
mycursor.execute("SELECT country_name FROM country_list;")
query_results = mycursor.fetchall()
query_results = toList(query_results)
print("___________________________")
print(world.name.tolist())
print("_______Errors________")

for i in query_results:
    if i not in world.name.tolist():
        print(i)

print("_______Errors________")
for i in world.name.tolist():
    if i not in query_results:
        print(i)
'''

#world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
#world.plot(column='gdp_per_cap')

fig, ax = plt.subplots()
ax.set_aspect('equal')

#s_world = world[world.name == query_results[4]]

world.plot(ax=ax, color='white', edgecolor='black')
column_list_priorities = ["official_languages", "national_languages", "widely_spoken_languages", "regional_languages", "minority_languages"]

already_plotted = []
color_list = []

k = 0
for h in column_list_priorities:
    if column_list_priorities.index(h) < 2:
        color_list = color_official_or_national
    elif column_list_priorities.index(h) > 2:
        color_list = color_regional_or_minority
    else:
        color_list = color_widely
    for i in languages_spoken:
        countries = query(i, h)
        for j in countries:
            s_world = world[world.name == j]
            if j not in already_plotted:
                s_world.plot(ax=ax, color=color_list[k])
                print(j)
                already_plotted.append(j)
        k += 1
    k = 0

plt.show()
