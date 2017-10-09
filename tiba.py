import urllib.request
import re
import os

num = 0
def fetch_pictures(url):
    global num
    html_content = urllib.request.urlopen(url).read()

    r = re.compile('<img class="BDE_Image" pic_type="0" width="560" height="315" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))
    #print(len(picture_url_list))
    #os.mkdir('photos')
    os.chdir('/home/moon/photos/')
    for i in range(len(picture_url_list)):
        picture_name = str(num) + '.jpg'
        num+=1
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])

if __name__ == '__main__':
    for i in range(1, 4):
        fetch_pictures("https://tieba.baidu.com/p/3204119098?see_lz=1&pn="+str(i))