![](http://banot.etsii.ull.es/alu4103/STW/logo.png)

SISTEMAS Y TECNOLOGÍAS WEB
============================

Versión 2.3

![](http://banot.etsii.ull.es/alu4103/STW/informacion.png)
============================
| GRUPO                         | EMAIL                     |
| -------------                 | -------------             |
| Ángela Hernández Delgago      | alu0100536898@ull.edu.es  |
| Madelaine Martín Pazó         | alu0100537130@ull.edu.es  |
| Jessica A. Ramos Villarreal   | alu0100537338@ull.edu.es  |


![](http://banot.etsii.ull.es/alu4103/STW/comentarios.png)
============================

**- 02/10/2013** - Prototipo

**- 05/10/2013** - Empezando Proyecto

**- 06/10/2013** - Definición de usuarios

	 - pip install django-social-auth
    	 - cloud9: easy_install django-social-auth
    
**- 06/10/2013** - Definición BBDD

**- 08/10/2013** - Foto Perfil

	 - pip install django-simple-gravatar
	 - cloud9: easy_install django-simple-gravatar
    
**- 08/10/2013** - Rellenar BBDD

**- 11/10/2013** - Añadiendo Páginas Estáticas

	 - about us
    	 - contact
    	 - help
    
**- 18/11/2013** - Añadida Página Senderos

    	- El Sauzal => Sendero 1 => Sendero 2 => Sendero 3
    	- La Matanza => Sendero 1 => Sendero 2
    	- La Victoria => Sendero 1
    	- La Orotava => Sendero 1
    	- Los Realejos => Sendero 1 => Sendero 2
    	- Santa Úrsula
    	- Tacoronte => Sendero 1 => Sendero 2
    	- Puerto de la Cruz => Sendero 1 => Sendero 2
    
**- 18/11/2013** - Añadido mapa personalizado => Página Mapa

**- 23/11/2013** - Añadiendo mapas de cada sendero.

**- 30/11/2013** - Terminando BBDD

**- 03/12/2013** - Añadiendo rutas a los senderos.

		- Añadiendo página Municipios
	
**- 04/12/2013** - Añadiendo puntucuación.

		- Añadiendo Actividades
		- Añadiendo Municipios.
	
**- 05/12/2013** - Añadiendo comentarios

		- Fotos carrusel
	
**- 07/12/2013** - Añadiendo rutas a la BBDD

**- 08/12/2013** - Añadiendo rutas a la BBDD

	 - Subir fotos
    	 - Borrar fotos. 
    
**- 09/12/2013** - Primer intento despliegue Heroku. 

     	- Modificando el diseño. 
     	- Terminado Comentarios.
    
**- 10/12/2013** - Modificando perfil

	 - Migración de sqlite3 a Postgres
        	- Guardar bbdd de sqlite: sqlite database .dump > sqlite-dumpfile.sql
        	- Insertarla en Postgres: psql -d ctn -U user -W < sqlite-dumpfile.sql
    	 - Se ha instalado:
        	- sudo apt-get install postgresql
        	- sudo apt-get install pgadmin3
        	- sudo -u postgres createuser --superuser username
        	- sudo -u postgres psql
            	\password username
        	- Se ha de crear la base de datos: createdb ctn
        	- sudo apt-get install python-psycopg2
        	- Exportar bbdd: pg_dump ctn -U usuario > dump.sql
        
**- 11/12/2013** - Modificación mapas en los senderos.

**- 15/12/2013** - Aplicación en heroku : http://conocetenerifenorte2.herokuapp.com/

**- 16/12/2013** - Test

![](http://banot.etsii.ull.es/alu4103/STW/presentacion.png)
============================
**1.** ¿Qué es CTN?

**2.** Framework 

**3.** BBDD

**4.** Tecnologías

**5.** Mecanismos

**6.** Demostración

###Chicas al poder! =)


