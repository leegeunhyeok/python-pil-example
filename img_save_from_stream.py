from PIL import Image
import io

with open("./origin.png", "rb") as image_bin:
    # Bytes 스트림에 데이터 저장
    out = io.BytesIO(image_bin.read())

    # Bytes 형태의 데이터 열기
    image = Image.open(out)

    # 이미지를 열고 필터, 크기조절, 썸네일 생성 등 작업 가능
    image.thumbnail((100, 100))
    
    # 썸네일 저장
    image.save("./result/thumbnail_from_stream.png")