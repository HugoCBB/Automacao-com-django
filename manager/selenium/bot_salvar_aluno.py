from webdriver_manager.chrome import ChromeDriverManager 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class BotSalvarAluno:
    def __init__(self):
        self.__service = Service(ChromeDriverManager().install())
        self.__options = Options()
        self.__options.add_argument("--disable-blink-features=AutomationControlled")
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__options)
        self.__wait = WebDriverWait(self.__driver, timeout=30)

        self.AcessarSite()
        self.ProcurarAluno()
        self.EncerrarPrograma()
        
    def AcessarSite(self):
        link = 'https://web.whatsapp.com/'
        self.__driver.get(link)
        print("Aguardando QRCode")
        sleep(15)

    def ProcurarAluno(self):
        self.__wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="labels-filter"]')))
        filtro = self.__driver.find_element((By.XPATH, '//*[@id="labels-filter"]'))
        filtro.click()
        
        self.__wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/li[2]/button')))
        orcamento = self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/li[2]/button')
        orcamento.click()
        sleep(5)


    def SalvarContato(self):
        pass

    def EncerrarPrograma(self):
        self.__driver.quit()
        

    def IniciaProgramaTeste(self):
        while True:
            self.AcessarSite()
            self.ProcurarAluno()
            self.EncerrarPrograma()
            break
            
if __name__ == "__main__":
    p1 = BotSalvarAluno()
    while True:
        p1.AcessarSite()
        p1.ProcurarAluno()
        p1.EncerrarPrograma()