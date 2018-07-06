from PIL import Image
import urllib.request
import io

# 웹에 있는 구글 로고
url = "https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"

# 구글 로고 불러오기 (Bytes)
image_data = urllib.request.urlopen(url).read()

# 스트림 생성 후 불러온 데이터 저장
data_stream = io.BytesIO(image_data)

# 스트림에서 이미지 열기
image = Image.open(data_stream)

# 그레이스케일 이미지로 변환
google = image.convert('LA')
google.save('./result/google.png')

data_stream.close()
google.close()
image.close()