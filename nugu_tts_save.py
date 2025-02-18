import requests
import base64

#api 주소
url = "https://apis.openapi.sk.com/axtts/tts"

#api input parameter setting
payload = {
    "model": "axtts-2-6",
    "voice": "aria",  #음성 모델
    "text": "오토큐에이는 상담어시스트와 통합된 패키지로 제공될 예정이며 통합 공급을 통해 실시간과 비실시간 전수 분석과 모니터링이 가능해집니다.",
    "speed": "1.1",   #속도 조절
    "sr": 22050,
    "sformat": "wav"
}
headers = {
    "accept": "audio/wav",
    "content-type": "application/json",
    "appKey": "skt open api app key"   #큰 따옴표 안에 app key insert
}

# api 호출
response = requests.post(url, json=payload, headers=headers)
data = response.content

# wav 저장을 위한 인코딩 및 디코딩
encode_string = base64.b64encode(data).decode('utf-8')
decode_string = base64.b64decode(encode_string)

#저장 파일명 설정
file_name = "audio01.wav"
   
#파일 저장
with open(file_name, "wb") as wav:
    wav.write(decode_string)

print(file_name + "생성완료") 