from webdriver import WebDriver


if __name__ == '__main__':
    webdriver = WebDriver()
    page_size = 5
    page_number = 1
    
    webdriver.search_mod(f"https://www.curseforge.com/minecraft/search?page={page_number}&pageSize={page_size}&sortBy=popularity&class=mc-mods&version=1.20.1")
    
    webdriver.driver.quit() 