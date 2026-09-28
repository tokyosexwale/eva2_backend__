import os
import django
import requests
import random

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prozacrecords.settings')
django.setup()

from musica_experimental.models import ArtistaCompositor, AlbumExperimental

# Lista de 75 Artistas y Compositores de Vanguardia/Música Experimental con su País
ARTISTAS_70 = [
    # Pioneros Electroacústica & Musique Concrète
    ("Pierre Schaeffer", "Francia"), ("Karlheinz Stockhausen", "Alemania"),
    ("John Cage", "Estados Unidos"), ("Iannis Xenakis", "Grecia"),
    ("Éliane Radigue", "Francia"), ("Luc Ferrari", "Francia"),
    ("Pierre Henry", "Francia"), ("Luigi Russolo", "Italia"),
    ("Pauline Oliveros", "Estados Unidos"), ("Morton Subotnick", "Estados Unidos"),
    
    # Minimalismo & Drone Temprano
    ("La Monte Young", "Estados Unidos"), ("Terry Riley", "Estados Unidos"),
    ("Steve Reich", "Estados Unidos"), ("Philip Glass", "Estados Unidos"),
    ("Charlemagne Palestine", "Estados Unidos"), ("Tony Conrad", "Estados Unidos"),
    ("Brian Eno", "Reino Unido"), ("William Basinski", "Estados Unidos"),
    
    # Japanese Noise / Avant-Garde Japonesa
    ("Merzbow", "Japón"), ("Keiji Haino", "Japón"),
    ("Otomo Yoshihide", "Japón"), ("Ryoji Ikeda", "Japón"),
    ("Boredoms", "Japón"), ("Masonna", "Japón"),
    ("Les Rallizes Dénudés", "Japón"), ("Hijokaidan", "Japón"),
    ("Aki Onda", "Japón"), ("Yasuaki Shimizu", "Japón"),
    
    # Industrial, Dark Ambient & Noise Wall
    ("Coil", "Reino Unido"), ("Nurse With Wound", "Reino Unido"),
    ("Throbbing Gristle", "Reino Unido"), ("Einstürzende Neubauten", "Alemania"),
    ("Vomir", "Francia"), ("Prurient", "Estados Unidos"),
    ("Pharmakon", "Estados Unidos"), ("Lustmord", "Reino Unido"),
    ("Puce Mary", "Dinamarca"), ("The Body", "Estados Unidos"),
    
    # Ambient Moderno, Drone & Electroacústica Contemporánea
    ("Tim Hecker", "Canadá"), ("Oneohtrix Point Never", "Estados Unidos"),
    ("Alva Noto", "Alemania"), ("Christian Fennesz", "Austria"),
    ("Oren Ambarchi", "Australia"), ("Alessandro Cortini", "Italia"),
    ("Kaitlyn Aurelia Smith", "Estados Unidos"), ("Holly Herndon", "Estados Unidos"),
    ("Ben Frost", "Australia"), ("Grouper", "Estados Unidos"),
    ("Julianna Barwick", "Estados Unidos"), ("Abul Mogard", "Serbia"),
    
    # Deconstructed Club, Microtonal & Vaporwave Vanguardista
    ("Arca", "Venezuela"), ("SOPHIE", "Reino Unido"),
    ("Autechre", "Reino Unido"), ("Aphex Twin", "Reino Unido"),
    ("Oneohtrix Point Never", "Estados Unidos"), ("James Ferraro", "Estados Unidos"),
    ("Oneohtrix Point Never", "Estados Unidos"), ("Dean Blunt", "Reino Unido"),
    ("Lucrecia Dalt", "Colombia"), ("Moor Mother", "Estados Unidos"),
    
    # Experimental Metal, Post-Rock Vanguardista & Improvisación
    ("Sunn O)))", "Estados Unidos"), ("Earth", "Estados Unidos"),
    ("Boris", "Japón"), ("Swans", "Estados Unidos"),
    ("Godspeed You! Black Emperor", "Canadá"), ("Natural Snow Buildings", "Francia"),
    ("Current 93", "Reino Unido"), ("Deathprod", "Noruega"),
    ("Fire!", "Suecia"), ("Peter Brötzmann", "Alemania"),
    ("Anthony Braxton", "Estados Unidos"), ("Derek Bailey", "Reino Unido"),
    ("Fred Frith", "Reino Unido"), ("Arto Lindsay", "Estados Unidos"),
    ("Laurie Anderson", "Estados Unidos"), ("Glenn Branca", "Estados Unidos")
]

FORMATOS = ['VINYL', 'CASSETTE', 'CD', 'DIGITAL', 'CINTA_MAGN']

def poblar_api_70():
    print("🧹 Limpiando base de datos de álbumes anteriores...")
    AlbumExperimental.objects.all().delete()
    
    print("🌐 Conectando a la API de iTunes para consultar 70+ artistas (Mínimo 4 álbumes destacados por artista)...\n")
    
    total_albumes = 0
    total_artistas = 0

    for nombre_artista, pais in ARTISTAS_70:
        # Crear o recuperar artista en la BD
        artista_obj, created = ArtistaCompositor.objects.get_or_create(
            nombre=nombre_artista,
            defaults={"pais": pais}
        )
        if created:
            total_artistas += 1

        # Consultar la API pública
        search_query = requests.utils.quote(nombre_artista)
        url = f"https://itunes.apple.com/search?term={search_query}&entity=album&limit=20"

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                results = response.json().get("results", [])
                
                albumes_agregados_artista = 0
                titulos_vistos = set()

                for item in results:
                    titulo_album = item.get("collectionName")
                    if not titulo_album or titulo_album in titulos_vistos:
                        continue

                    # Normalizar género y fecha
                    genero = item.get("primaryGenreName", "Experimental")
                    if genero in ["Music", "Pop", "Rock"]:
                        genero = "Experimental / Avant-Garde"

                    release_date = item.get("releaseDate", "2000")
                    anio = int(release_date.split("-")[0]) if "-" in release_date else 2000

                    # Portada HD (600x600 px) servida por CDN oficial de Apple
                    portada_hd = item.get("artworkUrl100", "").replace("100x100bb", "600x600bb")

                    if portada_hd:
                        AlbumExperimental.objects.create(
                            titulo=titulo_album,
                            genero=genero,
                            anio=anio,
                            formato=random.choice(FORMATOS),
                            portada=portada_hd,
                            artista=artista_obj
                        )
                        titulos_vistos.add(titulo_album)
                        albumes_agregados_artista += 1
                        total_albumes += 1

                print(f"✅ [{nombre_artista} ({pais})] -> {albumes_agregados_artista} álbumes agregados.")

        except Exception as e:
            print(f"⚠️ Error al consultar {nombre_artista}: {e}")

    print("\n" + "="*60)
    print("📊 RESUMEN FINAL DE CARGA MASIVA DE BD")
    print(f"👤 Artistas en BD: {ArtistaCompositor.objects.count()}")
    print(f"💿 Álbumes destacados guardados con Portada HD: {total_albumes}")
    print("="*60)

if __name__ == '__main__':
    poblar_api_70()
