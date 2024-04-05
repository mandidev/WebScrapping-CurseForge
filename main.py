from posixpath import basename
from webdriver import WebDriver
from os import makedirs
from os.path import exists, join
from requests import get

if __name__ == '__main__':
    webdriver = WebDriver()
    page_size = 5
    page_number = 1

    data = webdriver.search_mod(f"https://www.curseforge.com/minecraft/search?page={page_number}&pageSize={page_size}&sortBy=popularity&class=mc-mods&version=1.20.1")



    for mod in data.items():
        path = join('mods', mod[0].replace("/", "-"))
        if not exists( path ):
            makedirs( path )

        for url in mod[1]:
            with open( join(path, basename(url['url_download'])), 'wb' ) as f:
                f.write( get(url['url_download']).content )

       
            print("DESCARGADO: " + url['url_download'])


    webdriver.driver.quit()