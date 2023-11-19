import requests
from bs4 import BeautifulSoup

url = 'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=167026&page=1&schStr=regist&pbancEndYn=N'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    target = soup.select('.table_inner')
    
    # 각 항목을 배열에 저장하고 <br> 태그를 줄 바꿈(\n)으로 대체
    items = [element.text.replace('<br/>', '\n').strip() for element in target]
    
    # 13번과 14번 데이터 텍스트를 공백 3자리를 기준으로 잘라서 저장
    if len(items) >= 14:
        item_13 = items[12]  # 13번 데이터 항목 선택
        item_14 = items[13]  # 14번 데이터 항목 선택
        item_13_array = item_13.split('   ')  # 공백 3자리를 기준으로 나눔
        item_14_array = item_14.split('   ')  # 공백 3자리를 기준으로 나눔
        item_13_array = [item.strip() for item in item_13_array]  # 각 항목의 앞뒤 공백 제거
        item_14_array = [item.strip() for item in item_14_array]  # 각 항목의 앞뒤 공백 제거
        
        # 13번과 14번 데이터 각각을 배열로 출력
        print("13번_신청대상 데이터 배열:")
        print(item_13_array)
        print("14번_제외대상 데이터 배열:")
        print(item_14_array)

else:
    print("삐빅! 오류입니다")
