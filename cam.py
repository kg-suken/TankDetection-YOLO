import cv2
from ultralytics import YOLO

# 使用可能なカメラデバイスを探す関数
def find_available_cameras(max_cameras=10):
    available_cameras = []
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

# 使用可能なカメラデバイスのリストを表示
available_cameras = find_available_cameras()

if not available_cameras:
    print("利用可能なカメラが見つかりません")
    exit()

print("使用可能なカメラデバイス:")
for idx, cam in enumerate(available_cameras):
    print(f"{idx}: カメラデバイス {cam}")

# ユーザーにカメラを選択させる
cam_index = int(input("使用するカメラの番号を入力してください: "))
selected_camera = available_cameras[cam_index]

# YOLOv8モデルのロード
model = YOLO('./best.pt')

# 選択されたカメラをキャプチャ
cap = cv2.VideoCapture(selected_camera)

# 解像度を1280x720に設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

if not cap.isOpened():
    print("カメラにアクセスできません")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("フレームの取得に失敗しました")
        break

    # YOLOで物体検出
    results = model(frame)

    # 検出結果を画像に描画
    annotated_frame = results[0].plot()

    # 映像を表示
    cv2.imshow("YOLOv8 Real-time Detection", annotated_frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# クリーンアップ
cap.release()
cv2.destroyAllWindows()
