import pytest #importă librăria pytest.
from selenium import webdriver #importă WebDriver din Selenium WebDriver



@pytest.fixture #spune lui pytest că aceasta este o funcție reutilizabilă pentru teste
def driver(): #creează fixture-ul numit driver.
    driver = webdriver.Chrome()#deschide Chrome
    driver.maximize_window() #face browserul fullscreen(unele elemente sunt ascunse în modul mic,testele sunt mai stabile)

    yield driver #Aceasta este linia cea mai importantă din fixture.Trimite driverul către test si codul după yield se execută după ce testul se termină.

    driver.quit()#închide browserul după test