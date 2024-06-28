from pyuque.client import Yuque
from dotenv import load_dotenv
import json,os
import time

## 得到特定知识库下所有文档.

load_dotenv()
ACCESS_TOKEN = os.getenv("YUQUEACCESS_TOKEN")
# 使用你的个人访问令牌（Access Token）创建一个语雀API客户端
client = Yuque(ACCESS_TOKEN)

repo_namespace = "lexiansheng/onm58a"

# 获取知识库下的所有文档
docs = client.repo.list_docs(repo_namespace)

print(docs)
for doc in docs['data']:
    print(f"Title: {doc['title']}, URL: https://www.yuque.com/lexiansheng/onm58a/{doc['slug']}")
