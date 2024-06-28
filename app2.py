from pyuque.client import Yuque
from dotenv import load_dotenv
import json,os
import time

## 得到特定文档中的内容.

load_dotenv()
ACCESS_TOKEN = os.getenv("YUQUEACCESS_TOKEN")
# 使用你的个人访问令牌（Access Token）创建一个语雀API客户端
client = Yuque(ACCESS_TOKEN)

repo_namespace = "lexiansheng/onm58a"
document = client.doc.get(repo_namespace, "pb6e3wtn28qdsfa7")

# 打印文档内容
print(document['data']['body'])