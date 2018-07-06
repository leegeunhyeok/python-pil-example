from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

# 밴드를 포함한 튜플 반환
r, g, b = image.split()

# 배경으로 사용할 이미지 새로 생성
background = Image.new("L", r.size, "black")

# 배경이미지와 분할한 이미지 병합
Image.merge("RGB", (r, background, background)).save("./result/r.png")
Image.merge("RGB", (background, g, background)).save("./result/g.png")
Image.merge("RGB", (background, background, b)).save("./result/b.png")

image.close()