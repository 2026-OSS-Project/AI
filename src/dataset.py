
import os

def count_images(data_path):

    print("=== 데이터셋 현황 ===")

    for cls in os.listdir(data_path):

        cls_path = os.path.join(data_path, cls)

        if os.path.isdir(cls_path):

            count = len(os.listdir(cls_path))

            print(f"{cls}: {count}장")
