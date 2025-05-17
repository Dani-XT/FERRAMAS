from django.db import migrations, models
import os
from django.core.files import File
from django.conf import settings

def cargar_comics(apps, schema_editor):
    Editorial = apps.get_model('home', 'Editorial')
    Tipo = apps.get_model('home', 'Tipo')
    Producto = apps.get_model('home', 'Producto')

    comics = [
        {
            'descripcion': 'Sumérgete en el emocionante universo de Spider-Man con "The Amazing Spider-Man #1". Peter Parker enfrenta nuevos desafíos mientras equilibra su vida como superhéroe y estudiante. Con increíbles ilustraciones y una trama cautivadora, este cómic es imprescindible para los fanáticos del Hombre Araña.',
            'tipo': 'superhéroe',
            'imagen': 'Amazing-Spider-Man-1.webp',
            'editorial': 'Marvel',
            'nombre': 'THE AMAZING SPIDER-MAN #1',
            'precio': '5000',
            'stock': 10
        },
        {
            'descripcion': 'Explora el oscuro mundo de Gotham City con "Batman: The Killing Joke". Este clásico cómic presenta un enfrentamiento épico entre Batman y el Joker, ofreciendo una profunda mirada a la psicología de ambos personajes. Un imprescindible para cualquier coleccionista de cómics.',
            'tipo': 'superhéroe',
            'imagen': 'Batman-The-Killing-Joke.webp',
            'editorial': 'DC Comics',
            'nombre': 'BATMAN: THE KILLING JOKE',
            'precio': '8000',
            'stock': 8
        },
        {
            'descripcion': 'Acompaña a los Vengadores en una batalla épica contra Thanos en "Avengers: Infinity War". Este cómic reúne a los héroes más poderosos de la Tierra en una lucha desesperada para salvar el universo. Con impresionantes ilustraciones y una narrativa emocionante, es una joya para cualquier fan de Marvel.',
            'tipo': 'superhéroe',
            'imagen': 'Infinity-War-1.jpg',
            'editorial': 'Marvel',
            'nombre': 'AVENGERS: INFINITY WAR',
            'precio': '10000',
            'stock': 5
        },
        # Añade más cómics aquí según sea necesario
    ]

    for comic in comics:
        tipo, _ = Tipo.objects.get_or_create(nombre=comic['tipo'])
        editorial, _ = Editorial.objects.get_or_create(nombre=comic['editorial'])
        
        # Ruta completa de la imagen
        image_path = os.path.join(settings.MEDIA_ROOT, 'comic', comic['imagen'])
        
        with open(image_path, 'rb') as image_file:
            producto = Producto(
                descripcion=comic['descripcion'],
                nombre=comic['nombre'],
                precio=comic['precio'],
                stock=comic['stock'],
                tipo=tipo,
                editorial=editorial,
            )
            producto.imagen.save(comic['imagen'], File(image_file), save=True)

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_comics),
    ]
