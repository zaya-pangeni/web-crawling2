from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\chromedriver.exe')
driver.get("https://www.accuweather.com/en/np/nepal-weather")

places = driver.find_elements_by_xpath('//span[@class="text title no-wrap"]')
temp = driver.find_elements_by_xpath('//span[@class="text temp"]')
number1=len(places)
number2=len(temp)
with open("weather.txt","w") as f:
    for i in range(number1):
      f.write(places[i].text + "temperature is" + temp[i].text + "\n")

driver.close()