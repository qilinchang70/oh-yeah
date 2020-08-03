from bs4 import BeautifulSoup
import re
import requests
import time
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from selenium import webdriver

url = "https://www.dcard.tw/topics/podcast"
BOARD = ''
LATEST = False
ARTICLE_NUM = 30
COMMENT_NUM = 3

# search keyword
KEYWORD = 'podcast'

# chrome driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome("chromedriver",chrome_options=chrome_options)
driver.get(url)


def Search_Board():

    #if not LATEST:
    #    res = requests.get(url + '/f/' + BOARD)
    #else:
    #    res = requests.get(url + '/f/' + BOARD + '?latest=true')
    #soup = BeautifulSoup(res.text, 'html.parser')
    title_list = []
    href_list = []
    like_list = []
    time_list = []

    for i in range(5):  
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        # 文章標題、文章網址
        for entry in soup.select('article a'):
            title_list.append(entry.text)
            href_list.append(entry['href'])
        
        # 案讚數
        for entry in soup.select('article div'):
            if entry.has_attr('class'):
                item = re.search('sc-1kuvyve-3',entry['class'][0])
                if item is not None:
                    like_list.append(int(entry.text))
        # 抓時間
        for entry in soup.select('div span'):
            if entry.has_attr('class'):
                item = re.search('sc-6oxm01-2',entry['class'][0])
                if item is not None:
                    time_list.append(entry.text)

        ct=0
        Y=[]
        for timell in time_list:
            ct+=1
            if(ct%3==0):
                ct=0
                Y.append(timell)
          

                
        # 往下滑
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
    
    print('title list length = ')
    print(len(title_list))
    return title_list[0:ARTICLE_NUM], href_list[0:ARTICLE_NUM], like_list[0:ARTICLE_NUM], time_list[0:ARTICLE_NUM],Y


def Get_Article(href):

    res = requests.get("http://www.dcard.tw"+ href)
    soup = BeautifulSoup(res.text, 'html.parser')
    comment_list = []
    content = ''
    #all_content = ''
    

    for entry in soup.select('article div'):
        if entry.has_attr('class'):
            item = re.search('sc-4ihej7-0',entry['class'][0])
            if item is not None:
                content = entry.text
                break
          
    for entry in soup.select('div#comment-anchor div'):
        if entry.has_attr('class'):
            item = re.search('giORMG',entry['class'][1])
            if item is not None:
                comment_list.append(entry.text)

    return content, comment_list


def DrawBar(x_list, y_list, title, font):
    plt.title(title, fontproperties = font)
    plt.bar(x_list, y_list)
    plt.xticks(x_list,x_list)
    return


if __name__ == '__main__':

    title_list, href_list, like_list,time_list,Y = Search_Board() # Search the board and get article titles and likes number of each article

    ##############################################################################################################
    # Plot the like number of each article as histogram
    ##############################################################################################################
    myfont = FontProperties(fname=r'./Kaiu.ttf')

    title = '每篇文章讚數'
    DrawBar(list(range(1,ARTICLE_NUM + 1)), like_list, title, myfont)
    plt.show()
        ##############################################################################################################
    # Sort the articles according to likes number
    ##############################################################################################################
    
    #把標題、案讚數、網址，依照案讚數排序
    for i in range(ARTICLE_NUM):
        for j in range(ARTICLE_NUM - i - 1):
            if like_list[j] < like_list[j + 1]:
                title_list[j], title_list[j + 1] = title_list[j + 1], title_list[j]
                href_list[j], href_list[j + 1] = href_list[j + 1], href_list[j]
                like_list[j], like_list[j + 1] = like_list[j + 1], like_list[j]

    for i in range(ARTICLE_NUM):
        print('(' + str(like_list[i]) + ')', end = ' ')
        print(title_list[i], end = ' ')
        print('(' + href_list[i] + ')')

    for i in range(ARTICLE_NUM):
        z=Y[i]
        #print(z)
    
    a=0
    h=0
    g=0
    for i in range(ARTICLE_NUM):
        z=Y[i]
        if '2018' in z:
            a+=1
        elif '2019' in z:
            h+=1
        else:
            g+=1

    print('2018:',a,'2019:',h,'2020:',g)
    print('=========================================================================================================')
    
    #找關鍵字和頻道
    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=0,0,0,0,0,0,0,0,0,0
    for i in range(ARTICLE_NUM):
        content, comment_list = Get_Article(href_list[i])
        
        if '新聞' in content:     #'關鍵字'
            a1=a1+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '好笑' in content:     #'關鍵字'
            a2=a2+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '聲音' in content:     #'關鍵字'
            a3=a3+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '有幫助' in content:     #'關鍵字'
            a4=a4+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '生活' in content:     #'關鍵字'
            a5=a5+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '學習' in content:     #'關鍵字'
            a6=a6+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '有趣' in content:     #'關鍵字'
            a7=a7+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '知識' in content:     #'關鍵字'
            a8=a8+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '充實' in content:     #'關鍵字'
            a9=a9+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '歌' in content:     #'關鍵字'
            a10=a10+1
            #print('(' +title_list[i]+ ')' + '\n')
 
    print('新聞共有'+str(a1)+'篇','好笑共有'+str(a2)+'篇','聲音共有'+str(a3)+'篇','有幫助共有'+str(a4)+'篇')
    print('生活共有'+str(a5)+'篇','學習共有'+str(a6)+'篇','有趣共有'+str(a7)+'篇','知識共有'+str(a8)+'篇')
    print('充實共有'+str(a9)+'篇','歌共有'+str(a10))
    print('=========================================================================================================')
    #b1,b2,b3,b4,b5
    b = [0,0,0,0,0]
    b_label=[list(range(1,6))]
    for i in range(ARTICLE_NUM):
        content, comment_list = Get_Article(href_list[i])
        #print('content'+str(i))
        #print(content)
        if '台灣通勤第一品牌' in content:     #'頻道名'
            b[0]=b[0]+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '百靈果' in content:     #'頻道名'
            b[1]=b[1]+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '股癌' in content:     #'頻道名'
            b[2]=b[2]+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '科技島讀' in content:     #'頻道名'
            b[3]=b[3]+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '敏迪選讀' in content:     #'頻道名'
            b[4]=b[4]+1
            #print('(' +title_list[i]+ ')' + '\n')
        elif '馬力歐陪你喝一杯' in content:     #'頻道名'
            b[5]=b[5]+1
            #print('(' +title_list[i]+ ')' + '\n')
    print('台灣通勤第一品牌共有'+str(b[0])+'篇','百齡果共有'+str(b[1])+'篇','股癌共有'+str(b[2])+'篇','科技島讀'+str(b[3])+'篇')
    print('敏迪選讀共有'+str(b[4])+'篇','馬力歐陪你喝一杯共有'+str(b[5])+'篇')
    tit = '頻道提及數'
    DrawBar(b_label, b , tit, myfont)
    plt.show()
