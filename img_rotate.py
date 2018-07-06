from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

# 이미지 회전 (각도)
rotate = image.rotate(77)

# 지정 경로에 저장
rotate.save("./result/rotate.png")

rotate.close()
image.close()