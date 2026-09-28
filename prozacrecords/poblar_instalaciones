import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prozacrecords.settings')
django.setup()

from instalaciones.models import ArtistaVanguardia, InstalacionArtistica

def cargar_datos():
    print("Iniciando la carga masiva de datos para Instalaciones Artísticas...")

    datos_vanguardia = [
        # DADAÍSMO & SURREALISMO
        {"artista": "Marcel Duchamp", "movimiento": "Dadaísmo", "pais": "Francia", "obras": [
            ("Fuente (Fountain)", 1917, "Grand Central Palace, Nueva York", "Urinal de porcelana firmado como R. Mutt, obra pionera del Readymade."),
            ("La Mariée mise à nu par ses célibataires, même", 1923, "Philadelphia Museum of Art", "Escultura en vidrio y aceite sobre marco metálico."),
            ("Roue de bicyclette", 1913, "París", "Rueda de bicicleta montada sobre un taburete de madera."),
            ("L.H.O.O.Q.", 1919, "París", "Intervención dadaísta sobre una reproducción de la Gioconda."),
            ("Étant donnés", 1966, "Philadelphia Museum of Art", "Instalación voyerista a través de una puerta de madera vieja.")
        ]},
        {"artista": "Man Ray", "movimiento": "Dadaísmo / Surrealismo", "pais": "Estados Unidos", "obras": [
            ("Cadeau (El Regalo)", 1921, "Galerie Surréaliste, París", "Plancha de hierro con tachuelas pegadas a la base."),
            ("Obstacle d'Atelier", 1920, "Nueva York", "Instalación ensamblada con perchas suspendidas."),
            ("Indestructible Object", 1923, "París", "Metrónomo con una fotografía de un ojo en el péndulo."),
            ("Involute", 1935, "Galerie Charles Ratton, París", "Ensamblaje de materiales encontrados y sombras proyectadas."),
            ("Emak-Bakia Objet", 1926, "París", "Violonchelo modificado e instalación sonora de película experimental.")
        ]},
        {"artista": "Meret Oppenheim", "movimiento": "Surrealismo", "pais": "Suiza", "obras": [
            ("Le Déjeuner en Fourrure", 1936, "Museum of Modern Art, Nueva York", "Taza, plato y cuchara cubiertos de piel de gazela."),
            ("Das Paar (El Par)", 1956, "Basilea", "Par de zapatos unidos por las puntas."),
            ("Tisch mit Vogelfüßen", 1939, "Galerie René Drouin, París", "Mesa de bronce con patas en forma de garras de ave."),
            ("Cannibal Feast", 1959, "Exposición Internacional Surrealista, París", "Performance e instalación con banquete sobre un cuerpo vivo."),
            ("Genoveva", 1971, "Kunstmuseum Bern", "Escultura e instalación conceptual con elementos orgánicos.")
        ]},
        {"artista": "Kurt Schwitters", "movimiento": "Dadaísmo / Merz", "pais": "Alemania", "obras": [
            ("Merzbau Hannover", 1933, "Hannover, Alemania", "Arquitectura transformativa e instalación total en su propia vivienda."),
            ("Merzbau Lysaker", 1940, "Oslo, Noruega", "Instalación ambiental construida con materiales de desecho."),
            ("Cylindrical Merzbau", 1947, "Cumbria, Reino Unido", "Último ambiente Merz en un granero adaptado."),
            ("Merz-Barn Relief", 1947, "Elterwater", "Relieve e instalación de pared integrada en piedra."),
            ("Cathedral of Erotic Misery", 1928, "Hannover", "Estructura interna llena de nichos dedicados a artistas dadaístas.")
        ]},

        # FUTURISMO & ARTE SONORO TEMPRANO
        {"artista": "Luigi Russolo", "movimiento": "Futurismo / Arte Sonoro", "pais": "Italia", "obras": [
            ("Intonarumori Concert Hall", 1914, "Teatro Dal Verme, Milán", "Instalación de generadores acústicos de ruidos mecánicos."),
            ("Gran Concerto Futurista", 1914, "London Coliseum", "Exhibición de aparatos resonadores e instrumentos de ruido industrial."),
            ("Corale e Serenata", 1921, "Théâtre des Champs-Élysées, París", "Presentación de la orquesta de ruidos futuristas."),
            ("Rumorarmonio Display", 1924, "Milán", "Instalación del armonio de ruidos para música de vanguardia."),
            ("Archi Enarmonico", 1931, "París", "Demostración de mecanismos de microtonalidad en espacio cerrado.")
        ]},
        {"artista": "Giacomo Balla", "movimiento": "Futurismo", "pais": "Italia", "obras": [
            ("Ricostruzione Futurista dell'Universo", 1915, "Roma", "Instalación ambiental de esculturas complejas y coloridas."),
            ("Feu de Joie (Compenetrazione Iridescente)", 1917, "Teatro Costanzi, Roma", "Escenografía dinámica e iluminación matemática sin actores."),
            ("Casa Balla", 1928, "Via Oslavia, Roma", "Instalación habitacional donde paredes y muebles forman una obra total."),
            ("Fiori Futuristi", 1925, "Bienal de Venecia", "Jardín artificial con flores geométricas de madera y metal."),
            ("Lumen - Velocidad de luz", 1913, "Milán", "Instalación escénica de formas abstractas móviles.")
        ]},

        # FLUXUS & HAPPENING
        {"artista": "Nam June Paik", "movimiento": "Fluxus / Videoarte", "pais": "Corea del Sur", "obras": [
            ("TV Buddha", 1974, "Galeria Bonino, Nueva York", "Estatua de Buda contemplando su propia imagen en un televisor en bucle."),
            ("Electronic Superhighway", 1995, "Smithsonian American Art Museum", "Mapa gigante de EE.UU. construido con pantallas de neón y televisores."),
            ("TV Garden", 1974, "Solomon R. Guggenheim Museum", "Plantas vivas interconectadas con decenas de monitores que emiten videos."),
            ("Magnet TV", 1965, "Whitney Museum of American Art", "Televisor modificado por un imán masivo que distorsiona la señal."),
            ("Zen for TV", 1963, "Galerie Parnass, Wuppertal", "Televisor alterado para mostrar una sola línea vertical de luz.")
        ]},
        {"artista": "Yoko Ono", "movimiento": "Fluxus", "pais": "Japón", "obras": [
            ("Half-A-Room", 1967, "Lisson Gallery, Londres", "Habitación donde todos los muebles y objetos están cortados por la mitad."),
            ("Painting to Be Stepped On", 1960, "Indica Gallery, Londres", "Lienzo colocado en el suelo para ser pisado por los visitantes."),
            ("Apple", 1966, "Indica Gallery, Londres", "Manzana colocada sobre un pedestal de plexiglás para observar su descomposición."),
            ("Sky TV", 1966, "Nueva York", "Monitor de televisión que transmite en directo el cielo exterior."),
            ("Ama-no-gawa (Wish Tree)", 1996, "Museo de Arte Moderno de Tokio", "Árboles vivos donde el público cuelga deseos escritos en papel.")
        ]},
        {"artista": "Joseph Beuys", "movimiento": "Fluxus / Escultura Social", "pais": "Alemania", "obras": [
            ("7000 Eichen (7000 Robles)", 1982, "Documenta 7, Kassel", "Instalación ecológica urbana de 7000 árboles junto a bloques de basalto."),
            ("Plight", 1985, "Anthony d'Offay Gallery, Londres", "Habitación revestida completamente de fieltro con un piano de cola."),
            ("The Pack (Das Rudel)", 1969, "Kassel, Alemania", "Furgoneta Volkswagen con trineos que llevan fieltro, grasa y linternas."),
            ("Honigpumpe am Arbeitsplatz", 1977, "Documenta 6, Kassel", "Sistema de tubos que bombeaba miel a través de las salas del museo."),
            ("Capri-Batterie", 1985, "Capri, Italia", "Bombilla amarilla conectada a un limón fresco como fuente de energía.")
        ]},
        {"artista": "John Cage", "movimiento": "Fluxus / Arte Sonoro", "pais": "Estados Unidos", "obras": [
            ("33 1/3", 1969, "University of California, Davis", "Instalación interactiva con 12 tocadiscos y cientos de discos de vinilo."),
            ("Musicircus", 1967, "Champaign, Illinois", "Instalación ambiental simultánea de múltiples músicos en un solo espacio."),
            ("HPSCHD", 1969, "Assembly Hall, Urbana", "Espectáculo multimedia e instalación con claves, proyectores y sonido de computadora."),
            ("Variation VII", 1966, "Armory Show, Nueva York", "Sistema de captura sonora en tiempo real de llamadas telefónicas y radios."),
            ("Ryoanji Sound Installation", 1983, "París", "Instalación acústica basada en la disposición del jardín zen de Kioto.")
        ]},

        # CONSTRUCTIVISMO & SUPREMATISMO
        {"artista": "Vladimir Tatlin", "movimiento": "Constructivismo", "pais": "Rusia", "obras": [
            ("Monumento a la Tercera Internacional", 1919, "Petrogrado", "Maqueta e instalación arquitectónica helicoidal de acero y vidrio."),
            ("Letatlin", 1932, "Museum of Fine Arts, Moscú", "Instalación de aparato volador no motorizado de estructura orgánica."),
            ("Relieve Pictórico", 1914, "San Petersburgo", "Ensamblaje de madera, metal y cristal suspendido en esquinas."),
            ("Relieve de Esquina", 1915, "Exposición 0.10, Petrogrado", "Estructura colgada en la esquina superior de la sala sin soporte de suelo."),
            ("Estructura de Vestuario Teatral", 1923, "Moscú", "Instalación de vestuario funcional e industrial para el hombre nuevo.")
        ]},
        {"artista": "El Lissitzky", "movimiento": "Constructivismo", "pais": "Rusia", "obras": [
            ("Prounenraum (Espacio Proun)", 1923, "Grosse Berliner Kunstausstellung, Berlín", "Ambiente tridimensional donde el espectador camina dentro del cuadro."),
            ("Dresden Room (Abstrakter Raum)", 1926, "Internationale Kunstausstellung, Dresde", "Diseño de sala de exposición interactiva con paneles móviles."),
            ("Tribuna de Lenin", 1920, "Moscú", "Maqueta e instalación de estrado dinámico e inclinado."),
            ("Pressa Exhibition Pavilion", 1928, "Colonia, Alemania", "Instalación fotomontaje monumental de 24 metros de largo."),
            ("Pelikan Kiosk", 1924, "Hannover", "Estructura publicitaria e instalación urbana constructivista.")
        ]},

        # ARTE SONORO & BIOARTE CONTEMPORÁNEO
        {"artista": "Christina Kubisch", "movimiento": "Arte Sonoro", "pais": "Alemania", "obras": [
            ("Electrical Walks", 2004, "Berlín", "Paseo e instalación sonora mediante auriculares de inducción electromagnética."),
            ("Klangfluss (El Río del Sonido)", 1997, "ZKM Karlsruhe", "Cables de inducción colgados como enredaderas emisoras de tonos."),
            ("Electrical Mirages", 2012, "Milán", "Instalación inmersiva que mapea campos magnéticos de la ciudad."),
            ("Klangfeld", 1986, "Documenta 8, Kassel", "Campo de altavoces ocultos sobre césped que reaccionan a la luz."),
            ("Clocktower Sound Field", 1992, "P.S.1, Nueva York", "Composición espacial basada en frecuencias ultrasónicas en una torre de reloj.")
        ]},
        {"artista": "Eduardo Kac", "movimiento": "BioArte", "pais": "Brasil", "obras": [
            ("GFP Bunny (Alba)", 2000, "INRA, Jouy-en-Josas, Francia", "Instalación transgénica de una coneja genéticamente modificada con proteína verde."),
            ("Genesis", 1999, "O.K. Center for Contemporary Art, Linz", "Instalación que convierte frases bíblicas en código genético bacteriano."),
            ("Natural History of the Enigma", 2009, "Weisman Art Museum, Minneapolis", "Flor transgénica llamada Edunia que expresa el ADN del propio artista."),
            ("Move 36", 2002, "Gerson Zevi Gallery, Nueva York", "Instalación con planta transgénica sobre un tablero de ajedrez conceptual."),
            ("Teleporting An Anemone", 1994, "Siggraph, Chicago", "Instalación telerrobótica que conecta botánica y señales de internet.")
        ]},
        {"artista": "Ryoji Ikeda", "movimiento": "Arte Sonoro / Minimalismo Digital", "pais": "Japón", "obras": [
            ("Test Pattern", 2008, "Barbican Centre, Londres", "Instalación inmersiva de datos binarios proyectados a gran velocidad con ondas puras."),
            ("Data.tron", 2007, "ZKM Center for Art and Media, Karlsruhe", "Pantalla gigantesca que proyecta conjuntos masivos de datos matemáticos."),
            ("Micro/Macro", 2015, "Carriageworks, Sídney", "Instalación audiovisual escala gigante sobre física cuántica y cosmología."),
            ("Spectra", 2014, "Victoria Tower Gardens, Londres", "Instalación de cañones de luz blanca vertical proyectados al cielo nocturnal."),
            ("Supersymmetry", 2014, "YCAM, Yamaguchi", "Instalación de sensores y módulos que traducen colisiones de partículas.")
        ]},
        {"artista": "Anish Kapoor", "movimiento": "Arte Escultórico / Inmersivo", "pais": "India", "obras": [
            ("Svayambh", 2007, "Royal Academy of Arts, Londres", "Bloque gigante de cera roja que se desplaza lentamente por las puertas del museo."),
            ("Leviathan", 2011, "Grand Palais, París", "Estructura neumática monumental roja que ocupa todo el pabellón de cristal."),
            ("Descension", 2015, "Bienal de Kochi-Muziris, India", "Remolino de agua negra en constante rotación instalado en el suelo de la galería."),
            ("Marsyas", 2002, "Tate Modern, Londres", "Membrana gigante de PVC rojo extendida en la Sala de Turbinas."),
            ("At the Edge of the World", 1998, "Fondazione Prada, Milán", "Cúpula roja suspendida del techo que parece flotar sobre los espectadores.")
        ]},
        {"artista": "Olafur Eliasson", "movimiento": "Arte Instalativo / EcoArte", "pais": "Dinamarca", "obras": [
            ("The Weather Project", 2003, "Tate Modern, Londres", "Sol artificial gigante de lámparas mono-frecuencia y humedad artificial."),
            ("Ice Watch", 2014, "Place de la Panthéon, París", "Bloques masivos de hielo de Groenlandia dispuestos en forma de reloj."),
            ("Din blind passager (Your Blind Passenger)", 2010, "ARoS Aarhus Kunstmuseum", "Túnel de 90 metros lleno de niebla densa iluminada con colores primarios."),
            ("The New York City Waterfalls", 2008, "East River, Nueva York", "Cuatro cascadas artificiales de acero construidas en el puerto de Nueva York."),
            ("Blind Pavilion", 2003, "Bienal de Venecia", "Estructura de cristales negros y espejos que distorsionan la visión del entorno.")
        ]},

        # KINETIC & LIGHT ART
        {"artista": "Alexander Calder", "movimiento": "Arte Cinético", "pais": "Estados Unidos", "obras": [
            ("Cirque Calder", 1931, "Whitney Museum of American Art", "Instalación de figuras de alambre, tela y goma impulsadas manualmente."),
            ("Arc of Petals", 1941, "Peggy Guggenheim Collection, Venecia", "Escultura móvil suspendida que reacciona a las corrientes de aire."),
            ("Trapèze", 1929, "París", "Instalación de alambre que proyecta sombras dramáticas sobre paredes blancas."),
            ("Un effet du japonais", 1941, "Nueva York", "Móvil cinético monumental de discos de colores equilibrados."),
            ("Red Lily Pads", 1956, "Solomon R. Guggenheim Museum", "Instalación de discos flotantes de metal en el estanque del museo.")
        ]},
        {"artista": "Dan Flavin", "movimiento": "Minimalismo / Light Art", "pais": "Estados Unidos", "obras": [
            ("The Diagonal of May 25, 1963", 1963, "Green Gallery, Nueva York", "Tubo fluorescente de luz dorada colocado en un ángulo de 45 grados."),
            ("Greensburg, Pennsylvania Installation", 1973, "Westmoreland Museum of American Art", "Estructura de luces fluorescentes verdes y rojas en esquina."),
            ("Untitled (to You, Heiner, with Admiration)", 1973, "Dia Beacon, Nueva York", "Barrera modular de tubos fluorescentes verdes que atraviesa la sala."),
            ("Untitled (Marfa Complex)", 1996, "Chinati Foundation, Marfa, Texas", "Instalación permanente en 6 edificios militares usando tubos de colores."),
            ("Untitled (to Donna)", 1971, "Kunstmuseum Basel", "Combinación de luz azul y rosa en el pasillo central del museo.")
        ]},
        {"artista": "James Turrell", "movimiento": "Light and Space", "pais": "Estados Unidos", "obras": [
            ("Afrum-Proto", 1966, "Pasadena Art Museum", "Proyección de luz de alta intensidad que crea la ilusión de un cubo sólido flotante."),
            ("Roden Crater", 1977, "Desierto de Arizona", "Instalación a escala del paisaje dentro de un cono volcánico extinguido."),
            ("Aten Reign", 2013, "Solomon R. Guggenheim Museum", "Estructura concéntrica de tela y LED que transforma el atrio del museo."),
            ("D空間 (Skyspace - House of Light)", 2000, "Niigata, Japón", "Apertura cuadrangular en el techo que enmarca el cielo con variaciones de color LED."),
            ("Breathing Light", 2013, "LACMA, Los Ángeles", "Ganzfeld ambiental donde la percepción de profundidad espacial se elimina.")
        ]},
        {"artista": "Bruce Nauman", "movimiento": "Arte Conceptual", "pais": "Estados Unidos", "obras": [
            ("The True Artist Helps the World by Revealing Mystic Truths", 1967, "Philadelphia Museum of Art", "Anuncio de neón en espiral instalado en la ventana de la galería."),
            ("Live-Taped Video Corridor", 1970, "Solomon R. Guggenheim Museum", "Pasillo estrecho donde el visitante camina hacia un monitor que lo graba por detrás."),
            ("One Hundred Live and Die", 1984, "Benesse House Museum, Naoshima", "Muro gigantesco de frases de neón que parpadean en patrones aleatorios."),
            ("Get Out of My Mind, Get Out of This Room", 1968, "París", "Habitación vacía e iluminada donde se reproduce una grabación de voz hostil."),
            ("Mapping the Studio I (Fat Chance John Cage)", 2001, "Dia Art Foundation", "Instalación de siete proyecciones simultáneas de video de infrarrojos.")
        ]},
        {"artista": "Rebecca Horn", "movimiento": "Arte Corporal / Cinético", "pais": "Alemania", "obras": [
            ("Einhorn (Unicornio)", 1970, "Berlín", "Estructura vestible e instalación con un cuerno gigante de tela rígida."),
            ("Concert for Anarchy", 1990, "Tate Modern, Londres", "Piano de cola colgado al revés del techo que libera sus teclas estrepitosamente."),
            ("Finger Gloves", 1972, "Documenta 5, Kassel", "Guantes de madera de un metro de largo que alteran la percepción táctil."),
            ("Tower of the Nameless", 1994, "Viena", "Instalación de violines mecánicos que se tocan solos colgados en una torre."),
            ("The Feathered Prison Fan", 1978, "París", "Estructura mecánica de plumas gigantes que se abren y cierran como un abanico.")
        ]},
        {"artista": "Yayoi Kusama", "movimiento": "Arte Inmersivo / Pop Art Vanguardista", "pais": "Japón", "obras": [
            ("Infinity Mirror Room - Phalli's Field", 1965, "Castellane Gallery, Nueva York", "Habitación de espejos llena de cientos de tubos de tela rellenos con lunares rojos."),
            ("Mirrored Room - Pumpkin", 1991, "Fukutake Collection, Japón", "Espacio infinito reflejado con esculturas gigantes de calabazas amarillas."),
            ("The Souls of Millions of Light Years Away", 2013, "The Broad, Los Ángeles", "Espejos y luces LED colgantes que crean un universo infinito de destellos."),
            ("Narcissus Garden", 1966, "Bienal de Venecia", "1500 esferas de espejo de acero inoxidable colocadas en el césped exterior."),
            ("Obliteration Room", 2002, "Queensland Art Gallery", "Habitación blanca donde los visitantes pegan lunares de colores hasta cubrirla.")
        ]},
        {"artista": "Cildo Meireles", "movimiento": "Arte Conceptual Latinoamericano", "pais": "Brasil", "obras": [
            ("Babel", 2001, "Tate Modern, Londres", "Torre circular gigantesca construida con cientos de radios antiguos encendidos en diferentes emisoras."),
            ("Volatiles", 1980, "Museu de Arte Moderna, Río de Janeiro", "Habitación a oscuras con suelo cubierto de ceniza, olor a gas y una vela encendida."),
            ("Desvio para o Vermelho (Desvío al Rojo)", 1967, "Inhotim, Brumadinho", "Habitación completa donde absolutamente todos los muebles y objetos son rojos."),
            ("Inserções em Circuitos Ideológicos", 1970, "Río de Janeiro", "Intervención e instalación con botellas de Coca-Cola grabadas con mensajes políticos."),
            ("Atravessamento", 1989, "París", "Instalación de mallas metálicas, telas de araña y cristales rotos que el espectador debe atravesar.")
        ]},
        {"artista": "Marta Minujín", "movimiento": "Happening / Vanguardia Latinoamericana", "pais": "Argentina", "obras": [
            ("El Partenón de Libros", 1983, "Avenida 9 de Julio, Buenos Aires", "Reconstrucción del Partenón a escala real cubierta con 30.000 libros prohibidos."),
            ("La Menesunda", 1965, "Instituto Torcuato Di Tella, Buenos Aires", "Laberinto interactivo de 16 habitaciones con texturas, olores y actores."),
            ("El Obelisco de Pan Dulce", 1979, "Feria de las Naciones, Buenos Aires", "Estructura de 30 metros de altura cubierta con 30.000 paquetes de pan dulce."),
            ("El Pago de la Deuda Externa con Maíz", 1985, "Buenos Aires", "Performance e instalación con Andy Warhol sobre sacos de maíz amarillo."),
            ("Soft Gallery", 1973, "Harold Rivkin Gallery, Washington D.C.", "Ambiente construido íntegramente con 200 colchones usados de colores.")
        ]},
        {"artista": "Lygia Clark", "movimiento": "Neoconcretismo", "pais": "Brasil", "obras": [
            ("Bichos", 1960, "Río de Janeiro", "Esculturas geométricas articuladas de aluminio que el público debe manipular y transformar."),
            ("A casa é o corpo (La casa es el cuerpo)", 1968, "Bienal de Venecia", "Instalación laberíntica neumática que simula la penetración, ovulación y nacimiento."),
            ("Caminhando", 1963, "Río de Janeiro", "Cinta de Möbius cortada continuamente con tijeras por el espectador."),
            ("Máscaras Sensoriais", 1967, "Museu de Arte Moderna, Río de Janeiro", "Máscaras con sacos de olores, espejos y sonidos incorporados."),
            ("Estrutura de Caixas", 1964, "Río de Janeiro", "Cajas de madera entrelazadas para crear espacios habitables participativos.")
        ]},
        {"artista": "Hélio Oiticica", "movimiento": "Neoconcretismo / Tropicália", "pais": "Brasil", "obras": [
            ("Tropicália", 1967, "Museu de Arte Moderna, Río de Janeiro", "Instalación ambiental con arena, plantas, guacamayos vivos y penetrales de madera."),
            ("Eden", 1969, "Whitechapel Gallery, Londres", "Habitación llena de arena, pajas, camas e instalaciones para descansar e interactuar."),
            ("Grande Núcleo", 1960, "Río de Janeiro", "Paneles de colores geométricos suspendidos del techo en cuadrícula espacial."),
            ("Bólides", 1963, "Río de Janeiro", "Cajas y contenedores interactivos llenos de pigmentos puros, tierra y telas."),
            ("Parangolés", 1964, "Favela da Mangueira, Río de Janeiro", "Capas e instalaciones vestibles diseñadas para cobrar vida mediante la danza.")
        ]}
    ]

    total_artistas = 0
    total_instalaciones = 0

    for item in datos_vanguardia:
        artista_obj, created = ArtistaVanguardia.objects.get_or_create(
            nombre=item["artista"],
            defaults={
                "movimiento": item["movimiento"],
                "pais": item["pais"]
            }
        )
        if created:
            total_artistas += 1

        for obra in item["obras"]:
            titulo, anio, lugar, desc = obra
            InstalacionArtistica.objects.get_or_create(
                titulo=titulo,
                artistas=artista_obj,
                defaults={
                    "anio_exposicion": anio,
                    "lugar_galeria": lugar,
                    "descripcion": desc
                }
            )
            total_instalaciones += 1

    print(f"✅ ¡Proceso completado con éxito!")
    print(f"📊 Artistas procesados: {total_artistas} creados.")
    print(f"🎨 Instalaciones agregadas: {total_instalaciones} en la base de datos MySQL.")

if __name__ == '__main__':
    cargar_datos()
