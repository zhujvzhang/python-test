import requests,openpyxl

wb=openpyxl.Workbook()  

sheet=wb.active 

sheet.title='lyrics' 

sheet['A1'] ='序号'     
sheet['B1'] ='电影名'   
sheet['C1'] ='评分'   
sheet['D1'] ='简解'
sheet['E1'] ='链接'

from bs4 import BeautifulSoup

for x in range(10):
    headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
   
    }   
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url,headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    book_list = bs.find("div",class_="article").find_all("li")
    
    for book in book_list:
        try:
            num = book.find("em").text
            name = book.find("span",class_="title").text
            score = book.find("span",class_="rating_num").text
            comment = book.find("span",class_="inq").text
            movieurl=book.find('a')['href']
            sheet.append([num,name,score,comment,movieurl])
        except:
            num = book.find("em").text
            name = book.find("span", class_="title").text
            score = book.find("span", class_="rating_num").text
            comment = "没有评论语"
            movieurl=book.find('a')['href']
            sheet.append([num, name, score, comment,movieurl])
wb.save('tp250.xlsx')