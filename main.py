import requests
import ksetwallpaper
def get_bing_wallpaper_url():
    url = "https://bing.biturl.top/?resolution=1920&format=json&index=0&mkt=zh-CN"
    response = requests.get(url)
    data = response.json()
    return data['url']

def download_bing_wallpaper():
    url = get_bing_wallpaper_url()
    response = requests.get(url)
    with open("/tmp/bing_wallpaper.jpg", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    download_bing_wallpaper()
    ksetwallpaper.setwallpaper("/tmp/bing_wallpaper.jpg")
    ksetwallpaper.set_lockscreen_wallpaper("/tmp/bing_wallpaper.jpg")

