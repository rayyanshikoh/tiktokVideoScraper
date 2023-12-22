import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.tiktok.com/@storms.1/video/7314345106738253099'

def downloadVideo(link, save_location, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
        '_ga': 'GA1.1.658076526.1703184174',
        '__gads': 'ID=f2350b86f3bbbfc1:T=1703184175:RT=1703184175:S=ALNI_MZpIfQFdw717x38J9VbfsJa8tRyWQ',
        '__gpi': 'UID=00000ce711ab05fd:T=1703184175:RT=1703184175:S=ALNI_MYgWpULXLm05ecnAQInnQks4TwrIg',
        '_ga_ZSF3D6YSLC': 'GS1.1.1703184173.1.1.1703184200.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'hx-target': 'target',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-trigger': '_gcaptcha_pt',
        'hx-request': 'true',
        'hx-current-url': 'https://ssstik.io/en',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'origin': 'https://ssstik.io',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ssstik.io/en',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': '_ga=GA1.1.658076526.1703184174; __gads=ID=f2350b86f3bbbfc1:T=1703184175:RT=1703184175:S=ALNI_MZpIfQFdw717x38J9VbfsJa8tRyWQ; __gpi=UID=00000ce711ab05fd:T=1703184175:RT=1703184175:S=ALNI_MYgWpULXLm05ecnAQInnQks4TwrIg; _ga_ZSF3D6YSLC=GS1.1.1703184173.1.1.1703184200.0.0.0',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'cFdydFU_', # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    print(f"Saving video {id} to: {save_location}/{videoTitle}.mp4")
    
    with open(f"{save_location}/{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


if __name__ == "__main__":
    while True:
        print("Please paste the link of the video you want to download:")
        url = input()
        if url == "":
            print("Please enter a valid URL, or type exit to quit")
            continue
        elif url == "exit":
            break
        else:
            pass
        downloadVideo(url, 1)
        print("Video downloaded successfully!")
