# 로컬 디렉토리의 폴더와 파일을 스캔하는 함수
import os

def scan_local_directory(path, parent=""):
    result = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        full_path = os.path.join(parent, item) if parent else item
        if os.path.isdir(item_path):
            result.append((full_path, "dir"))
            result.extend(scan_local_directory(item_path, full_path))
        else:
            result.append((full_path, "file"))
    return result


# "C:\Users\LENOVO\Desktop\github\메뉴얼" 폴더를 스캔
# (실제 실행 환경에서는 주석을 해제하고 경로를 실제로 존재하는 경로로 바꿔주세요)
scanned_result = scan_local_directory("C:\\Users\\LENOVO\\Desktop\\github\\메뉴얼")

# 스캔 결과 출력 (디버깅 목적)
# for item, item_type in scanned_result:
#     print(f"{item} ({item_type})")

