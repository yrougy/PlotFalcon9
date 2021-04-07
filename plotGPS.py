import re
import pyproj
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def read_file(gpsfile):
    # Lit le fichier ligne par ligne et extrait les coordonnées au format ECEF (x, y, z)
    coords = []
    with open(gpsfile, encoding="ISO-8859-1") as f:
        for line in f:
            if 'solution x/y/z' in line:
                regex = r'z:\s(.*)\sPDOP'
                le = re.findall(regex, line)
                try:
                    coord = le[0].split(' ')
                    coords.append([coord[0], coord[1], coord[2]])
                except:
                    # La flemme de corriger les erreurs.. On a assez de points pour tracer la courbe
                    pass
    return(coords)


def transform_coords(coords):
    # Transforme les coordonnées ECEF (x, y, z) en LatLon (lat, lon, altitude)
    coord_wgs = []

    transformer = pyproj.Transformer.from_crs(
        {"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'},
        {"proj": 'latlong', "ellps": 'WGS84', "datum": 'WGS84'},
    )
    for coord in coords:
        x, y, z = coord
        lon, lat, _ = transformer.transform(x, y, z, radians=False)
        # Je skip l'altitude via le _

        coord_wgs.append([lon, lat])
    return(coord_wgs)


def plot_map(points, filename):

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # Défini le "zoom" avec des coordonnées "hardcoded"
    # A améliorer si on choisit d'autres fichiers !
    ax.set_extent([-10, 40, 30, 60], crs=ccrs.PlateCarree())

    ax.stock_img()
    ax.coastlines()

    # On extrait les coordonnées [[x, y],... , [x, y]] en [x, ...][y, ...]
    # Oui on peut mieux faire mais ... j'étais pressé ^^
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    # print(max(x), min(x), max(y), min(y))
    # ^ Avec cette ligne on pourrait mieux faire pour le zoom
    ax.plot(x, y, transform=ccrs.Geodetic())

    plt.savefig(filename)


coords = read_file('gps_debug.txt')
transformed_coords = transform_coords(coords)
plot_map(transformed_coords, 'output.png')

# Coucou le chat!

