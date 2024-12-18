# 戦車を検出するYOLO
YOLOv8xを元に学習を行いました

データセット:https://universe.roboflow.com/project-0woqr/tank-finder-xuueg  
モデル:https://github.com/kg-suken/TankDetection-YOLO/blob/main/best.pt  
モデルのダウンロードリンク:https://github.com/kg-suken/TankDetection-YOLO/raw/refs/heads/main/best.pt?download=

268 layers, 68,124,531 parameters, 0 gradients

ソース画像
<br><img src="https://github.com/user-attachments/assets/3d638c17-84b9-4a62-8d0d-ec743846a31e" width="500"/>

出力画像
<br><img src="https://github.com/user-attachments/assets/3e647d8a-9abe-4313-b88e-00816be4c2de" width="500"/>

---
## 使い方
### インストール
```
pip install opencv-python opencv-python-headless
```
```
pip install ultralytics
```
Pytorchは公式サイトからお使いのGPUにあったものをインストールしてください。  
```
pip install torch torchvision torchaudio
```
### 実行
モデルとpyファイルは同じディレクトリに配置し、そのディレクトリの中で実行してください。
```
python cam.py
```
カメラの選択肢が現れますので、数字を入力してエンターキーを押してください。

---
## サンプル
リアルタイムで動画から戦車を検出しています。

[ソース動画](https://www.youtube.com/watch?v=Kat897_pud4)

https://github.com/user-attachments/assets/6844ace2-995b-40b7-bf50-3fb14f65fce6
| パーツ | スペック            |
|--------|---------------------|
| CPU    | RYZEN 5 5600X      |
| GPU    | RTX2060 12GB       |
| MEM    | DDR4 32GB          |
| OS     | Ubuntu 24.04       |

---


## 制作
**sskrc**

---

今後の改良に関する提案やバグ報告は、お気軽にIssueを通してご連絡ください。
