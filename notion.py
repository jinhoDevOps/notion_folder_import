# import requests

# def create_notion_page(parent_page_id, title, token):
#     url = "https://api.notion.com/v1/pages"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json",
#         "Notion-Version": "2021-08-16"
#     }
#     data = {
#         "parent": {"page_id": parent_page_id},
#         "properties": {
#             "title": {
#                 "title": [
#                     {
#                         "text": {
#                             "content": title
#                         }
#                     }
#                 ]
#             }
#         }
#     }
#     response = requests.post(url, headers=headers, json=data)
#     return response.json()

# def update_notion_page(page_id, content, token):
#     url = f"https://api.notion.com/v1/pages/{page_id}"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json",
#         "Notion-Version": "2021-08-16"
#     }
#     # 본문 내용 업데이트 로직 (Notion API 형식에 맞게)
#     response = requests.patch(url, headers=headers, json={"your_update_data_here": content})
#     return response.json()


import requests
import json

def create_notion_page(parent_page_id, title, token):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16"
    }
    data = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "type": "title",
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    
    if "id" in response_json:
        return response_json["id"]
    else:
        return None

def update_notion_page(page_id, content, token):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16"
    }
    data = {
        "properties": {
            "content": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    return response.json()
