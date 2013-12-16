Feature: Validating User Model


        Scenario: Probar el acceso al HTML raiz
        Given I access the url "/"
        Then I see the header "Twitter Basket"

        Scenario: Pagina index tiene contenido
                Given I access the url "/"
                Then I see the first link "Log in"
                #And I see the link "Contact "
                And I see the input and type "id_username" , "text"
                And I see the input and type "id_password" , "password"
