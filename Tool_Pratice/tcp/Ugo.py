import requests
from bs4 import BeautifulSoup
import Agent


class Ugo():

    def __init__(self, url="None"):


        self.agentSetting()
        if url!="None":
            self.res = requests.get(url)
            #解析 HTML
            self.soup = BeautifulSoup(self.res.text, "html")

            #存取 標籤
            self.head = self.soup.find_all("head")
            self.body = self.soup.find_all("body")
            self.script = self.soup.find_all("script")
    def agentSetting(self):
        # Agent.py 設定
        agent = Agent.AgentTool()
        self.SearchUrl = 'https://www.google.com.tw/search?q='
        self.user_agent = agent.UserAgent(0)
        self.proxy = agent.proxy()
    def google_Search(self,keyword):


        #關鍵字搜尋


        res=requests.get(self.SearchUrl+keyword , headers = self.user_agent , proxies =self.proxy)

        soup = BeautifulSoup(res.text,"html")
        titles = []
        divs = soup.find_all("div", class_="g")
        #print(divs)
        for d in divs:

            if d.find("a"):
                x=d.find("a")
                href = x['href']
                title = list(x.children)[0].string

                titles.append(
                    {
                        'title':title,
                        'href':href
                    }
                )
        #print ( titles)

        return titles
    def hotKey(self,geo="TW"):
        url = "https://trends.google.com.tw/trends/trendingsearches/daily?geo="
        res = requests.get(url+geo ,headers=self.user_agent, proxies=self.proxy)

        soup = BeautifulSoup(res.text,"html")
        return soup


if __name__ == '__main__':
    url = "https://pala.tw/python-web-crawler/"
    u = Ugo(url)


    print(u.hotKey())