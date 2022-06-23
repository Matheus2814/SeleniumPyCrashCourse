from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/compliasset/projects/SeleniumPyCrashCourse/chromedriver')
# driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com')
print(driver.title)
