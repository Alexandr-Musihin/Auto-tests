from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path='D:\\ATestirovanie\\geckodriver.exe')




try:
    url = "https://5ka.ru/"
    driver.get(url=url)
    sleep(5)
    acc = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[1]').click()
    rating = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[2]').click()
    Magazins = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[3]').click()
    X5club = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[4]').click()
    More = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[5]').click()
    card = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/ul/li[1]').click()
    More1 = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[5]').click()
    news = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/ul/li[2]').click()
    More2 = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[5]').click()
    Feedback = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/ul/li[3]').click()
    More3 = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[5]').click()
    delivery = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/ul/li[4]').click()
    More3 = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/div/div/div/div[5]').click()
    leginfo = driver.find_element('xpath', '/html/body/div/div[2]/main/div[1]/div/div[1]/div/div/div[2]/nav/ul/li[5]').click()
    sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# driver.find_element('xpath', '').click()
# 

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