from behave import given, when, then

@given('el usuario abre la pagina saucedemo')
def step_impl(context):
    context.login_page.abrir()

@when('inicia sesion ok con sus credenciales correctas {username}')
def step_impl(context, username):
    context.username = username

@when('password {password}')
def step_impl(context, password):
    context.login_page.login_completo(context.username, password)

@then('debe acceer correctamente al inventario')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url