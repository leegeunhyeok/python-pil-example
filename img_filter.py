from PIL import Image, ImageFilter

# origin.png 파일 열기
image = Image.open("./origin.png")

# 이미지에 필터효과 적용
"""
ImageFilter.BLUR
ImageFilter.CONTOUR
ImageFilter.DETAIL
ImageFilter.EDGE_ENHANCE
ImageFilter.EDGE_ENHANCE_MORE
ImageFilter.EMBOSS
ImageFilter.FIND_EDGES
ImageFilter.SMOOTH
ImageFilter.SMOOTH_MORE
ImageFilter.SHARPEN
"""
filter_image = image.filter(ImageFilter.BLUR)

filter_image.save("./result/filter.png")

# 열고 닫아주기
filter_image.close()
image.close()