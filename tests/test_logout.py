from pages.login_page import LoginPage #importă clasa LoginPage din fișierul login_page.py din folderul pages


def test_logout(driver): #creeaza un test Pytest
    login_page = LoginPage(driver) #Creează un obiect din clasa LoginPage.
#Trimite browserul (driver) către această clasă.
#Astfel metoda LoginPage poate folosi browserul pentru: click,scris,citit elemente

    login_page.open() #Selenium deschide browserul si intra pe site
    login_page.login(username="standard_user", password="secret_sauce") #login

    login_page.logout() #logout

    assert "saucedemo.com" in driver.current_url #aceasta este verificarea testului.