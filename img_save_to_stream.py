from PIL import Image
import io

# 이미지 파일 열기
image = Image.open("./origin.png")

# 스트림 생성
stream = io.BytesIO()

# 썸네일 생성
image.thumbnail((100, 100))

# 스트림에 썸네일 저장
image.save(stream, format="PNG")

# 스트림에 저장된 썸네일 데이터 출력 (Bytes)
print(stream.getvalue())

stream.close()
image.close()
