from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pdb

driver = webdriver.Chrome(executable_path='/home/compliasset/projects/SeleniumPyCrashCourse/chromedriver')

driver.get('http://demostore.supersqa.com')

# By.ID
cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_text = cart.text
print(cart_text)

# Plural
my_products = driver.find_elements(By.CLASS_NAME, 'product')
print(my_products)

# By.ID
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie')
search_field.send_keys(Keys.ENTER)

# By.CSS_SELECTOR & By.XPATH
my_acct = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
# my_acct = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
my_acct.click()


# pdb.set_trace()

# driver.quit()

