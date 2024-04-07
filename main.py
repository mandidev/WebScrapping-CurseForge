from posixpath import basename
from webdriver import WebDriver
from os import makedirs
from os.path import exists, join
from requests import get

def download_file(path:str, url:str):
    with open(path, 'wb' ) as f:
        f.write( get(url).content )


if __name__ == '__main__':
    webdriver = WebDriver()
    page_size = 100
    page_number = 1

    for i in range(1, 51):
        page_number = i
        data = webdriver.search_mod(f"https://www.curseforge.com/minecraft/search?page={page_number}&pageSize={page_size}&sortBy=popularity&class=mc-mods&version=1.20.1")

        for mod in data.items():
            path = join('mods', mod[0].replace("/", "-"))

            if not exists( path ):
                makedirs( path )

            download_file(
                path=join(path, "avatar.jpeg"),
                url=mod[1]['url_avatar'])
    
            for i in mod[1]['list_screenshots']:
                path_screenshots = join(path, 'screenshots')
                if not exists(path_screenshots):
                    makedirs(path_screenshots)
                download_file( join(path_screenshots, basename(i)), i)
                

            for url in mod[1]['dic_list']:
                path_full = join(path, url['game_version'])
                if not exists( path_full ):
                    makedirs( path_full )
                
                download_file(
                    path=join(path_full, basename(url['url_download'])), 
                    url=url['url_download'])
        
                print("DESCARGADO: " + url['url_download'])


    webdriver.driver.quit()