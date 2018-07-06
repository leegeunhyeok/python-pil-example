from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

# 지정 크기로 이미지 크기 재설정 (폭, 높이)
resized = image.resize((100, 50))

# 지정 경로에 저장
resized.save("./result/resize.png")

resized.close()
image.close()