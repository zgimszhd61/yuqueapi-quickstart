from pyuque.client import Yuque
from dotenv import load_dotenv
import json,os
import time

## 搜索特定关键词.

load_dotenv()
ACCESS_TOKEN = os.getenv("YUQUEACCESS_TOKEN")
# 使用你的个人访问令牌（Access Token）创建一个语雀API客户端
client = Yuque(ACCESS_TOKEN)

keyword = 'api'

# 搜索文档
def search_documents(keyword):
    try:
        # 调用搜索API,doc或者repo
        response = client.search.search(keyword,type='doc',related=False)
        # print(response)
        # 解析并打印搜索结果
        for item in response['data']:
            print(f"Title: {item['title']} ， URL: https://www.yuque.com{item['url']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 执行搜索
search_documents(keyword)