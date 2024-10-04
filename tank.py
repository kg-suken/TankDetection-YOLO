import cv2
from ultralytics import YOLO

# YOLOv8モデルのロード
model = YOLO('./best.pt')

# 画像を読み込む
input_image_path = './input.png'
image = cv2.imread(input_image_path)

if image is None:
    print(f"画像ファイル '{input_image_path}' を読み込めませんでした")
    exit()

# YOLOで物体検出
results = model(image)

# 検出結果を画像に描画
annotated_image = results[0].plot()

# 結果をoutput.pngとして保存
output_image_path = './output.png'
cv2.imwrite(output_image_path, annotated_image)
print(f"結果の画像を '{output_image_path}' として保存しました")
