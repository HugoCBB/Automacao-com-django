from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class SUN_BOT:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install()) 
        self.options = Options()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, timeout=30)


    def AcessarSite(self):
        link = 'https://web.whatsapp.com/'
        self.driver.get(link)
        print("Aguardando QRCode")
        sleep(90)

    def EnviarMensagem(self, numero, mensagens):
        # Procurar contato
        url = f"https://web.whatsapp.com/send?phone={numero}"
        self.driver.get(url)
        sleep(5)

        # Esperar o campo de mensagem aparecer
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')))
        
        # Mensagem
        mensagem = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
        mensagem.click()
        mensagem.send_keys(mensagens)
        mensagem.send_keys(Keys.RETURN)
        sleep(5)

    def EncerrarPrograma(self):
        self.driver.quit()


