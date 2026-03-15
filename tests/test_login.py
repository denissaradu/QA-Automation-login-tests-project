from pages.login_page import LoginPage #importă clasa LoginPage din fișierul login_page.py care se află în folderul pages

#Pytest rulează automat toate funcțiile care încep cu test_
#driver - Aceasta este o fixture definită în conftest.py, ea creează browserul Chrome.

def test_login_valid(driver):
    login_page = LoginPage(driver) #creează un obiect din clasa LoginPage. Trimite driverul catre pagina
    login_page.open() #această linie apelează metoda din login_page.py.Selenium deschide site-ul
    login_page.login(username="standard_user", password="secret_sauce") #apeleaza metoda login
    assert "inventory" in driver.current_url #aceasta este verificarea testului. După login, site-ul te duce la pagina Saucedemo si verificam daca url ul contine inventory.(daca da, trece testul)


def test_login_invalid(driver): #testează cazul în care loginul nu ar trebui să funcționeze.
    login_page = LoginPage(driver) #creeaza pagina
    login_page.open() #deschide site ul
    login_page.login(username="locked_out_user", password="secret_sauce") #incercare de logare cu user blocat. Site ul returneaza mesaj de eroare.
    assert "locked out" in login_page.get_error_message() #aici se intampla metoda get_error_message() si returneaza textul erorii din pagina
#verificam daca "locked out" exista in text(daca da - trece testul)

def test_logout(driver): #testează dacă utilizatorul se poate deloga.
    login_page = LoginPage(driver) #se creeaza pagina
    login_page.open() #deschide site ul
    login_page.login(username="standard_user", password="secret_sauce") #face login
    login_page.logout() #apelează metoda din login_page.py care deschide meniul si apasă logout
    assert "saucedemo.com" in driver.current_url #după logout utilizatorul revine la pagina de login Saucedemo. Verificam daca url ul contine "saucedemo.com"