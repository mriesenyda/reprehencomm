from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")

elements = driver.find_elements(By.CLASS_NAME, "my_class")
