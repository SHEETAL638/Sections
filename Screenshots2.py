from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def take_screenshot(link, xpaths, num):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Open the webpage
    driver.get(link)
    time.sleep(2)
    try:
      alert = driver.switch_to.alert()
      alert.dismiss()
    except:
      print('no alert')
    width = 1920
    height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(width, height)
    counter = 0
    
    for xpath in xpaths:
        counter += 1
        try:
                
            element = driver.find_element(By.XPATH, xpath)  
            # Save the element screenshot to disk
            filename = f"screenshots/{num+11}/screenshot{counter}.png"
            element.screenshot(filename)
            
        except:
            print(f"error in image ({num}) xpath ({counter})")
    print("link",num,"done")

    # Quit the WebDriver
    driver.quit()
