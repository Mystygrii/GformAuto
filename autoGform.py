from selenium import webdriver
from selenium.webdriver.common.by import By

class AutoGform:
    def __init__(self,nom:str,prenom:str):
        self.nom = nom
        self.prenom = prenom
        
    def complete(self):
        print("completing...")
        self.driver = webdriver.Firefox()
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScbe3yuuPNnv8BJ7V7PMbNwhKBQBQYhYxWZQg_Ganh92o4O3A/viewform")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div").click()
        
        self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()
        
        self.lastNameIn = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.lastNameIn.send_keys(self.nom)
        
        self.nameIn = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.nameIn.send_keys(self.prenom)
        
        self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
        print("Completion Done !")