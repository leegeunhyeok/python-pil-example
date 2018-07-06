from PIL import Image

image = Image.open('./origin.png')

# 그레이스케일 이미지로 변환
gray = image.convert('LA')
gray.save('./result/greyscale.png')

image.close()