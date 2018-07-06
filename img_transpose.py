from PIL import Image

# origin.png 파일 열기
image = Image.open("./origin.png")

# 90단위로 회전 또는 좌우, 위아래 뒤집기
"""
Image.FLIP_LEFT_RIGHT
Image.FLIP_TOP_BOTTOM
Image.ROTATE_90
Image.ROTATE_180
Image.ROTATE_270
Image.TRANSPOSE
"""
rotate = image.transpose(Image.FLIP_TOP_BOTTOM)

# 지정 경로에 저장
rotate.save("./result/rotate.png")

rotate.close()
image.close()