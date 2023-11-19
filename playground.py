import requests
from bs4 import BeautifulSoup

url = 'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=167023&page=1&schStr=regist&pbancEndYn=N'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # .table_inner에서 특정 데이터 항목 처리 및 출력
    target = soup.select('.table_inner')
    items = [element.text.replace('<br/>', '\n').strip() for element in target]
    for idx, item in enumerate(items, start=1):
        if idx in [13, 14]:
            print(f"{idx}. {item}")

    # <p> 태그에서 텍스트 출력, '문의처' 섹션부터 '자세한 내용은...' 섹션까지
    p_tags = soup.select('p')
    start_printing = False
    for p in p_tags:
        text = p.get_text().strip()
        if '문의처' in text:
            start_printing = True
        if start_printing:
            if '자세한 내용은 첨부파일 참조 및 문의처로 문의하여 주시기 바랍니다' in text:
                print(text)
                break  # 이 부분에서 출력 중단
            print(text)

else:
    print("삐빅! 오류입니다")
