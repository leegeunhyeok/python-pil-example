from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

print("이미지 사이즈 (가로, 세로): ", image.size)
print("이미지 모드: ", image.mode)
print("이미지 포맷: ", image.format)
print("이미지 정보: ", image.info)

# 열고 닫아주기
image.close()