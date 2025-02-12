from webdriver_manager.chrome import ChromeDriverManager 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from time import sleep


class botSalvarAluno:
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
        sleep(90)

    def ProcurarAluno(self):
        self.__wait.until((By.XPATH, '//*[@id="labels-filter"]'))

        orcamento = self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/li[3]/button')
        orcamento.click()

        pass

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
    p1 = botSalvarAluno()
    p1.IniciaProgramaTeste()
    
