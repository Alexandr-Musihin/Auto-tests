from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path='D:\\ATestirovanie\\geckodriver.exe')




try:
    url = "https://netschool.edu22.info/about.html"
    driver.get(url=url)
    sleep(10)
    rayon = driver.find_element('xpath', '//*[@id="provinces"]').click()
    sleep(3)
    enter_rayon = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/select/option[42]').click()
    sleep(2)
    city = driver.find_element('xpath', '//*[@id="cities"]').click()
    sleep(3)
    enter_city = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[4]/div/select/option[10]').click()
    sleep(2)
    org_type = driver.find_element('xpath', '//*[@id="funcs"]').click()
    sleep(3)
    enter_org_type = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[5]/div/select/option[3]').click()
    sleep(2)
    school = driver.find_element('xpath', '//*[@id="schools"]').click()
    sleep(3)
    enter_school = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[6]/div/select/option[4]').click()
    sleep(5)
    LoginEntryField = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[8]/input')
    sleep(4)
    LoginEntryField.send_keys('МусихинА1')
    sleep(3)
    PassEntryField = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[9]/input')
    sleep(4)
    PassEntryField.send_keys('070807')
    sleep(3)
    enter = driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[11]/a/span').click()
    sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# driver.find_element('xpath', '').click()

######################################

#   def close():
#       a = input("Close program?")
#       if a == "yes":
#           driver.quit()
#       if a == "no":
#           close()
#       else:
#           close()



######################################
