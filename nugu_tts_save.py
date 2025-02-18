import requests
import base64

#변수 설정
script_file = "script.txt" #TTS로 변환할 스크립트 (script.txt)
url = "https://apis.openapi.sk.com/axtts/tts" #api 주소
appKey = "skt open api app key"   #큰 따옴표 안에 app key insert

# A.X Nugu tts 이용해 wav 파일 생성 함수 
def getWav(text, file_name) :
    #api input parameter setting
    payload = {
        "model": "axtts-2-6",
        "voice": "aria",  #음성 모델
        "text": text,
        "speed": "1.1",   #속도 조절
        "sr": 22050,
        "sformat": "wav"
    }
    headers = {
        "accept": "audio/wav",
        "content-type": "application/json",
        "appKey" : appKey,
    }

    # api 호출
    response = requests.post(url, json=payload, headers=headers)
    data = response.content

    # wav 저장을 위한 인코딩 및 디코딩
    encode_string = base64.b64encode(data).decode('utf-8')
    decode_string = base64.b64decode(encode_string)
   
    #파일 저장
    with open(file_name, "wb") as wav:
        wav.write(decode_string)

    print(file_name + "생성완료") 

# 스크립트 파일을 읽어 wav 생성
with open(script_file,"r") as f:
    count = 1
    for line in f:
        #저장 파일명 설정
        file_name = "output"+str(count)+".wav"
        text = line.strip()
        getWav(text, file_name)
        count = count+1