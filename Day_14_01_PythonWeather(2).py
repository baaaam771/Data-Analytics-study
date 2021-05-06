# Day_14_01_PythonWeather.py
import re
import requests

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184'
received = requests.get(url)
# print(received)                 # <Response [200]>
# print(type(received))           # <class 'requests.models.Response'>

data = received.text
# print(data)
# print(type(data))               # <class 'str'>

# 문제
# city 태그 안쪽의 지역을 찾아주세요
# temp = re.findall(r'<city>제주</city>', data)
# temp = re.findall(r'<city>..</city>', data)
# temp = re.findall(r'<city>...</city>', data)
# temp = re.findall(r'.+', data)                    # 의미없다. 변별력 없음
# temp = re.findall(r'<city>.+</city>', data)
# print(temp)
# temp = re.findall(r'<city>(.+)</city>', data)
# print(temp)

# <city>.+</city>
# <city>제주</city>
# <city>서귀포</city>
# <city>성산</city>
# <city>성판악</city>
# <city>고산</city>
# <city>이어도</city>
# <city>추자도</city>

# 문제
# <body> 태그 안쪽에 들어있는 커다란 분량의 문자열을 검색(추출)하세요
# re.DOTALL: 개행 문자를 일반 문자로 변환. 검색 패턴이 여러 줄에 걸쳐 있을 때 사용
body = re.findall(r'<body>.+</body>', data, re.DOTALL)
# print(body)
# print(len(body))

# 문제
# body 태그 안쪽에서(검색한 내용으로부터) city 태그 안쪽의 지역을 찾아주세요
# 아래처럼 태그 단위로 검색하면 싱크(동기화)를 맞출 수 없다
# 맞출 수 있더라도 굉장히 피곤한 코딩을 수반한다. 이런 방법은 정신 건강에 해롭다
# t1 = re.findall(r'<province>(.+)</province>', body[0])
# t2 = re.findall(r'<city>(.+)</city>', body[0])
# t3 = re.findall(r'<mode>(.+)</mode>', body[0])
# t4 = re.findall(r'<tmEf>(.+)</tmEf>', body[0])
# t5 = re.findall(r'<wf>(.+)</wf>', body[0])
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print(t5)

# ['제주도', '제주도', '제주도', '제주도', '제주도', '제주도', '제주도']
# ['제주', '서귀포', '성산', '성판악', '고산', '이어도', '추자도']
# ['A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A02', 'A01', 'A01', 'A01']
# ['2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00', '2021-04-26 00:00', '2021-04-26 12:00', '2021-04-27 00:00', '2021-04-27 12:00', '2021-04-28 00:00', '2021-04-28 12:00', '2021-04-29 00:00', '2021-04-29 12:00', '2021-04-30 00:00', '2021-04-30 12:00', '2021-05-01 00:00', '2021-05-02 00:00', '2021-05-03 00:00']
# ['구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음', '구름많음', '구름많음', '구름많음', '흐림', '흐리고 비', '흐리고 비', '흐리고 비', '구름많음', '맑음', '맑음', '맑음', '맑음', '구름많음']

# 문제
# body 태그 안쪽에서(검색한 내용으로부터) location 태그를 찾아주세요
# .+ : 탐욕적(greedy)
# .+? : 비탐욕적(non-greedy)
# locations = re.findall(r'<location wl_ver="3">(.+)</location>', body[0], re.DOTALL)
# print(len(locations))
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', body[0], re.DOTALL)
# print(len(locations))
# print(locations[0])

# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>
# <location wl_ver="3">...</location>

# '3412 '에 '[0-9]+' 패턴 적용
# 3, 34, 341, 3412









