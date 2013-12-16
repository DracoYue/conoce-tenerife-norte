Feature: Validating User Model


        Scenario: Probar el acceso al HTML raiz
        Given I access the url "/"
        Then I see the header "CTN"

        Scenario: Pagina index tiene contenido
                Given I access the url "/"
                Then I see the first link "CTN"


        Scenario: Page register has content
                Given I access the url "/registrate/"
                Then I see h1 " REGISTRO "
                And I see the form "form"
                And I see the input and type "id_usuario" , "text"
                And I see the input and type "id_nombre" , "text"
                And I see the input and type "id_fecha_nacimiento" , "text"
                And I see the input and type "id_email" , "text"
                And I see the input and type "id_remail" , "text"
                And I see the input and type "id_password" , "password"
                And I see the input and type "id_password1" , "password"
                And I see the button and type "boton" , "submit"
                #And I see in register the link "Contact "
                I see the label "id_usuario"
                I see the label "id_nombre"
                I see the label "id_fecha_nacimiento"
                I see the label "id_email"
                I see the label "id_remail"
                I see the label "id_password"
                I see the label "id_password1"
                
        


        #Scenario: A user can login
#                Given I access the url "/"
#                Then A usuario is loging

        Scenario: These users with length shorter than 50 should pass
                Given I have a usuario Macarena
                When I check if usuario is valid
        #Examples:
        #|usuario |
        #|Jessica |
        #|FernandO|
        #|ANGELA91|
        #|jess |
        #|fErni |

        Scenario: These users with length shorter than 50 should fail
                Given I have a usuario Je$$ica
                When I check if usuario is not valid
        #Examples:
        #|usuario |
        #|Je$$ica |
        #|@jess |
        #|Fer/ni |
        #|angie(lokilla)|

        Scenario: A ususario's password should be valid
                Given I have a password A123aaWW
                When I check if password is valid
                Then Password should pass if not empty
        #Examples:
        #|password |
        #|contrasena |
        #|4caracteres|
        #|hola&adios |

        Scenario: Two password should be equals
                Given I have a password 1234felipe
                And I have a second password 1234felipe
                The first password is not empty
                The second password is not empty
                When I check if password is valid
                The second password is valid
                The two passwords are the same
        
        Scenario: Two password not should be equals
                Given I have a password 1234felipe
                And I have a second password 1234felipE
                The first password is not empty
                The second password is not empty
                When I check if password is valid
                The second password is valid
                The two passwords are not the same

        Scenario: A user's date of birth should be valid
                Given I have a date 04/12/1991
                When I check if date is valid
                And I have a date 03/05/1999
                When I check if date is valid

        Scenario: A user's date of birth shoud be invalid
                Given I have a date 13/12/2013
                When I check if date is not valid

        Scenario: Beide e-mails mussen ubereinstimmen
                Habe die erste e-mail pepe@gmail.com
                Habe den zweiten e-mail pepe@gmail.com
                Die erste e-mail musste eingetragen werden
                Das zweite e-mail musste eingetragen werden
                Die erste e-mail muss gultig sein
                Das zweite e-mail muss gultig sein
                Beide e-mails mussen ubereinstimmen

        Scenario: Testear que los dos correos son diferentes
                Obtengo el primer email pepe@gmail.com
                Obtengo el segundo email pep@gmail.com
                Miro que el primer email no este vacio
                Miro que el segundo email no este vacio
                Miro que el primer email es valido
                Miro que el segundo email es valido
                Miro que los dos email son diferentes

        Scenario: Nombres de usuario sin palabrotas
                Obtengo un nombre de usuario pepe
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es valido
                Compruebo que el usuario no tiene palabrotas

        Scenario: Nombres de usuario con palabrotas
                Obtengo un nombre de usuario hijoputa
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es valido
                Compruebo que el usuario tiene palabrotas

        Scenario: Nombre de usuario iguales a nombres de Jugadores
                Obtengo un nombre de usuario DwyaneWade
                Compruebo que el nombre de usuario es valido
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es igual al de un Jugador

        Scenario: Nombre de usuario diferentes a nombres de Jugadores
                Obtengo un nombre de usuario Lebron_James
                Compruebo que el nombre de usuario es valido
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es diferente al de un Jugador

        Scenario: Nombre de usuario iguales a nombres de Equipo
                Obtengo un nombre de usuario MiamiHeat
                Compruebo que el nombre de usuario es valido
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es igual al de un Equipo

        Scenario: Nombre de usuario diferentes a nombres de Equipo
                Obtengo un nombre de usuario Miami_Heat
                Compruebo que el nombre de usuario es valido
                Compruebo que el nombre de usuario no es vacio
                Compruebo que el nombre de usuario es diferente al de un Equipo
        
        Scenario: Sigo a un Jugador
                Obtener mi nombre de usuario Bulbasaur
                Comprobar que el usuario no es vacio
                Comprobar que el usuario es valido
                Obtengo nombre del jugador que sigo pikachu
                Comprobar que el jugador no es vacio
                Comprobar que el jugador es valido
                Comprobar que sigo a ese jugador

        Scenario: No sigo a un Jugador
                Obtener mi nombre de usuario Bulbasaur
                Comprobar que el usuario no es vacio
                Comprobar que el usuario es valido
                Obtengo nombre del jugador que sigo tolete
                Comprobar que el jugador no es vacio
                Comprobar que el jugador es valido
                Comprobar que no sigo a ese jugador


        Scenario: A user can access all urls
                Given I have a url <url>
                Then I access the url
        #Examples:
        #|url |
        #|/registrate/ |
        #|/login/ |
        #|/twitter/logout/|
        #|/perfil/ |
        #|/modperfil/ |
        #|/login/follow/ |