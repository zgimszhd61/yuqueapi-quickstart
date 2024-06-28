from pyuque.client import Yuque
from dotenv import load_dotenv
import json,os
import time

# 添加内容道特定库

load_dotenv()
ACCESS_TOKEN = os.getenv("YUQUEACCESS_TOKEN")

client = Yuque(ACCESS_TOKEN)

repo_namespace = "lexiansheng/onm58a"

title = "示例文档"

content = """
# 这是一个示例文档

这是文档的内容部分。
"""

# response = client.doc.create(repo_namespace, title, content, slug=None, public=0, format='markdown', directory_id=directory_id)

# 创建文档,52329330
response = client.doc.create(repo_namespace, title, body=content, public=1, format='markdown')

# 打印响应结果
print(response)