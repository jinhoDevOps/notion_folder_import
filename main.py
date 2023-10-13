# from local import scan_local_directory
# from notion import create_notion_page, update_notion_page
from local import *
from notion import *

# API 토큰과 시작 페이지 ID (노션 설정과 URL에서 얻을 수 있음)
api_token = "your api toekn"
start_page_id = "af7af15c4874452c9917d0372bb95680"

import os

# 설정
local_dir = "C:\\Users\\LENOVO\\Desktop\\github\\메뉴얼"
target_notion_page_id = "your_target_notion_page_id_here"

# 로컬 디렉토리 스캔
scanned_result = scan_local_directory(local_dir)

# 노션 페이지 생성 및 업데이트
for item, item_type in scanned_result:
    if item_type == "dir":
        create_notion_page(start_page_id, item, api_token)
    else:
        # 파일 확장자 가져오기
        _, ext = os.path.splitext(item)
        
        # 그림 파일 스킵
        if ext.lower() in ['.jpg', '.png', '.gif', '.bmp']:
            print(f"Skipping image file {item}")
            continue

        # PDF 파일 패스 (나중에 처리)
        if ext.lower() == '.pdf':
            print(f"Passing PDF file {item} for later processing")
            continue
        
        try:
            with open(f"{local_dir}\\{item}", "r", encoding="utf-8-sig") as f:
                content = f.read()
            update_notion_page(target_notion_page_id, content, api_token)
        except UnicodeDecodeError:
            print(f"Could not read the file {item} due to encoding issues.")

