from selenium.webdriver.common.by import By #Importă clasa By din Selenium.
from selenium.webdriver.support.ui import WebDriverWait #Importă clasa care permite așteptări explicite.
from selenium.webdriver.support import expected_conditions as EC #Importă condițiile de așteptare.
#expected_conditions spune ce anume așteptăm.


class LoginPage: #Creare clasa
	def __init__(self, driver): #constructorul clasei
		self.driver = driver #salveaza driverul in clasa astfel incat sa il putem folosi in toate metodele

	def open(self): #metoda care deschide pagina
		self.driver.get("https://www.saucedemo.com") #selenium deschide URL

	def login(self, username, password): #metoda care face login,primeste doua variabile
		self.driver.find_element(By.ID, "user-name").send_keys(username) #gasim input pentru username si scriem text

		self.driver.find_element(By.ID, "password").send_keys(password) #gasim input si scriem parola

		self.driver.find_element(By.ID, "login-button").click() #gasim login button si face click

	def get_error_message(self): #această metodă returnează mesajul de eroare dacă loginul e greșit
		# găsește elementul care conține mesajul de eroare
		error = self.driver.find_element(By.CLASS_NAME, "error-message-container")
		# ia textul afișat în browser,returneaza textul ca sa poata fi folosit în test:
		return error.text

	def logout(self): #metoda pentru logout
		# deschide meniul
		self.driver.find_element(By.ID, "react-burger-menu-btn").click()

		# așteaptă până apare butonul logout
		logout_button = WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
		)

		logout_button.click() #click logout
