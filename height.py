from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-notifications")  # Disable notifications

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Function to identify set of siblings with specified error in sum of heights and average width
def identify_siblings_with_error(element, page_width, page_height, height_error, width_error):
    siblings = element.find_elements(By.XPATH, 'preceding-sibling::*')
    siblings += element.find_elements(By.XPATH, 'following-sibling::*')
    siblings.append(element)

    sum_heights = 0
    sum_widths = 0
    for sibling in siblings:
        sum_heights += sibling.size['height']
        sum_widths += sibling.size['width']
    avg_width = sum_widths / len(siblings)
    return (abs(sum_heights - page_height) <= height_error * page_height) and \
           (abs(avg_width - page_width) <= width_error * page_width)

# URLs to analyze
urls = [
    "https://app.goprimer.com/direct_to_page/O7oDC?redirect=false&",
    "https://app.goprimer.com/direct_to_page/g4gIh?redirect=false&",
    "https://try.goprimer.com/direct_to_page/YkM8O?redirect=false&",
    "https://try.goprimer.com/direct_to_page/YMosc?redirect=false&redirect=false&",
    "https://try.goprimer.com/direct_to_page/A8WKX?redirect=false&",
    "https://try.goprimer.com/direct_to_page/EwboD?redirect=false&",
    "https://try.goprimer.com/direct_to_page/ulr2O?redirect=false&",
    "https://try.goprimer.com/direct_to_page/WZBLj?redirect=false&redirect=false&",
    "https://try.goprimer.com/direct_to_page/MMbKf?redirect=false&redirect=false&",
    "https://try.goprimer.com/direct_to_page/8gtEH?redirect=false&",
    "https://try.goprimer.com/direct_to_page/EC23W?redirect=false&"
]

# Set error margins
height_error_margin = 0.9  # 10% error in sum of heights
width_error_margin = 0.1    # 10% error in average width

for url in urls:
    # Navigate to the webpage
    driver.get(url)

    # Find the root element of the webpage
    root_element = driver.find_element(By.TAG_NAME, 'html')

    # Get the width and height of the webpage
    page_width = driver.execute_script("return document.body.scrollWidth")
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Initialize variables to store maximum level and corresponding set of siblings
    max_level = 0
    siblings_with_error = []

    # Start traversing the tree structure from the root element
    for level, element in enumerate(root_element.find_elements(By.XPATH, './/*'), 1):
        if identify_siblings_with_error(element, page_width, page_height, height_error_margin, width_error_margin):
            max_level = level
            siblings_with_error = element.find_elements(By.XPATH, 'preceding-sibling::*')
            siblings_with_error += element.find_elements(By.XPATH, 'following-sibling::*')
            siblings_with_error.append(element)

    # Print the results for the current URL
    print("URL:", url)
    print("Maximum Level:", max_level)
    if siblings_with_error:
        siblings_tags = [s.get_attribute('id') for s in siblings_with_error]
        print("Set of Siblings with Error in Sum of Heights and Average Width:")
        print(siblings_tags)
    print("=" * 50)

# Close the WebDriver
driver.quit()
