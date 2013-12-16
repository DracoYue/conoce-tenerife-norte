Feature: Validating User Model


        Scenario: We have access
                Given I access the url "/"
                Then I see the first link "CTN"
                Then I see the header "CTN"
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"

        Scenario: Principal page has content
                Given I access the url "/"
                Then I see the first link "CTN"
                Then I see the header "CTN"
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"


        Scenario: Page register has content 
                Given I access the url "/login/"
                Then I see the first link "CTN"
                Then I see the header "CTN"
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"
                
                
        Scenario: Page help has content
                Given I access the url "/help/"
                Then I see the header "CTN"
                Then I see the first link "CTN"
                Then I see h1 "HELP"
                Then I see the first h4 " 1. Â¿QuÃ© es CTN? "
                Then I see the first h5 " PÃ¡gina web donde los amantes de la naturaleza pondrÃ¡n encontrar informaciÃ³n de los lugares que desean conocer."
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"

        Scenario: Page contact has content
                Given I access the url "/contact/"
                Then I see the header "CTN"
                Then I see the first link "CTN"
                Then I see the first p "Si desea contactar con nosotros, puede hacerlo mediante la siguiente informaciÃ³n:"
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"

        Scenario: Page Municipios has content
                Given I access the url "/municipios/"
                Then I see the first link "CTN"
                Then I see the header "CTN"
                Then I see h1 " MUNICIPIOS "
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"
                Then I see the eighth a "La Orotava"
                Then I see the ninth a "Santa Ursula"
                Then I see the tenth a "Puerto de la Cruz"
                Then I see the eleventh a "Tacoronte"
                Then I see the twelfth a "Los Realejos"
                Then I see the thirteenth a "El Sauzal"
                Then I see the fourteenth a "La Matanza de Acentejo"
                Then I see the fifteenth a "La Victoria de Acentejo"

        Scenario: Page Senderos has content
                Given I access the url "/senderos/"
                Then I see the first link "CTN"
                Then I see the header "CTN"
                Then I see h1 " SENDEROS "
                Then I see the second link "Ayuda"
                Then I see the third link "Contacto"
                Then I see the fourth link "Nosotros"
                Then I see the first h3 "Municipio:"
                Then I see the first h5 "La Orotava"
