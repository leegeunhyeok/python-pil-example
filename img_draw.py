from PIL import Image, ImageDraw

# origin.png 파일 열기
image = Image.open("./origin.png")

# 이미지에 그리기
draw = ImageDraw.Draw(image)

# 글자 위치, 글자 텍스트
draw.text((10, 10), "Python Image Library")

image.save("./result/draw.png")

# 열고 닫아주기
image.close()