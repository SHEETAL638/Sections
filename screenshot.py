from selenium import webdriver
from selenium.webdriver.common.by import By

def take_screenshot(link, xpaths, num):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Open the webpage
    driver.get(link)
    try:
      alert = driver.switch_to.alert()
      alert.dismiss()
    except:
      print('no alert')
    width = 1920
    height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(width, height)
    counter = 0
    
    if(num==2):
        try:
          driver.find_element(By.XPATH,"//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1']").click()
        except:
          print("Window did not appear")
        try:
          driver.find_element(By.XPATH,"//button[contains(text(), 'Change Country')]").click()
        except:
          print("Pop-up did not appear")
        try:
          driver.find_element(By.XPATH,"//a[@aria-label='deny cookies']").click()
        except:
          print("Cookies already disabled")
    
    if(num==3):
       try:
           driver.find_element(By.XPATH,"//button[@class='modal__close js-modalClose']").click()
       except:
           print("no_cookies")
           
       
    if(num==4):
        try:
           driver.find_element(By.ID,"ps-desktop-widget__close").click()
        except:
            print("no pop up")
        try:
           driver.find_element(By.XPATH,"//button[@class='css-1c3imcp']").click()
        except:
            print("no cookies")

    for xpath in xpaths:
        counter += 1
        try:
                
            element = driver.find_element(By.XPATH, xpath)  
            # Save the element screenshot to disk
            filename = f"screenshots/{num+1}/screenshot{counter}.png"
            element.screenshot(filename)
            
        except:
            print(f"error in image ({num}) xpath ({counter})")
    print("link",num,"done")

    # Quit the WebDriver
    driver.quit()
