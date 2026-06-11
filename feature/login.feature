Feature: Login de usuarios
    Scenario: Login exitoso
        Given que el usuario abra la pagina saucedemo
        When inicia sesion con sus credenciales correctas standard_user
        And password secret_sauce
        Then debe acceer correctamente al inventario
