# -*- coding: utf-8 -*-                                                                                                                                                                                  
from app import app                                                                                                                                                                                      
import unittest                                                                                                                                                                                          

class Test(unittest.TestCase):                                                                                                                                                                           

    def setUp(self):                                                                                                                                                                                     
        # creates an instance of unittest, needs the name "setUp"                                                                                                                                       
        self.app = app.test_client()                                                                                                                                                                     

        # send a GET request to the URL                                                                                                                                                            
        self.result = self.app.get('/')                                                                                                                                                                  

    def test_request(self):                                                                                                                                                                           
        # compares the status of the request (must be equal to 200)                                                                                                                                    
        self.assertEqual(self.result.status_code, 200)                                                                                                                                                   

    def test_content(self):                                                                                                                                                                             
        # check the return of the page content                                                                                                                                                    
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World")