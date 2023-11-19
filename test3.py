import requests
from bs4 import BeautifulSoup

url = 'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=167023&page=1&schStr=regist&pbancEndYn=N'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    target = soup.select('.table_inner')
    
    # 각 항목을 배열에 저장하고 <br> 태그를 줄 바꿈(\n)으로 대체
    items = [element.text.replace('<br/>', '\n').strip() for element in target]
    
    # 12번과 13번 데이터 항목만 출력
    for idx, item in enumerate(items, start=1):
        if idx in [13,14]:
            print(f"{idx}. {item}", sep='')

else:
    print("삐빅! 오류입니다")
