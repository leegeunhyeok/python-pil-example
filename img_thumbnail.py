from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

# 지정 크기로 썸네일 생성
# (이미지 비율에 맞춤)
image.thumbnail((50, 50))

# 지정 경로에 저장
image.save("./result/thumbnail.png")

image.close()