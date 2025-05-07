from base_test import BaseTest
from selenium.webdriver.common.by import By

class TestSolicitudServicio(BaseTest):
    def test_validacion_campos_obligatorios(self):
        driver = self.driver
        driver.get("https://orgfarm-23b5231ee9-dev-ed.develop.lightning.force.com/lightning/o/Solicitud_de_Servicio__c/new?count=1&nooverride=1&useRecordTypeCheck=1&navigationLocation=LIST_VIEW&uid=174663646996329981")
        
