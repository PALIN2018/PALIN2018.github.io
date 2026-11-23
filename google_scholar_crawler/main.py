from scholarly import scholarly, ProxyGenerator
import json
import sys
import time
from datetime import datetime
import os

MAX_ATTEMPTS = 5
RETRY_DELAY_SECONDS = 15


def fetch_author():
    """Fetch the author record from Google Scholar via a fresh free-proxy pool.

    Each call draws a new set of free proxies, so retrying after a failure
    usually lands on a different proxy than the one Google Scholar rejected.
    """
    pg = ProxyGenerator()
    pg.FreeProxies()  # Use free rotating proxies
    scholarly.use_proxy(pg)

    print("正在查找作者信息...")
    author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])

    print("正在填充作者详细信息...")
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


author = None
last_error = None
for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        print(f"第 {attempt}/{MAX_ATTEMPTS} 次尝试抓取 Google Scholar 数据...")
        author = fetch_author()
        break
    except Exception as e:
        last_error = e
        print(f"第 {attempt} 次尝试失败: {e}")
        if attempt < MAX_ATTEMPTS:
            print(f"{RETRY_DELAY_SECONDS} 秒后换一组代理重试...")
            time.sleep(RETRY_DELAY_SECONDS)

if author is None:
    print(f"发生异常: {MAX_ATTEMPTS} 次尝试均失败，最后一次错误: {last_error}")
    sys.exit(1)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
print(json.dumps(author, indent=2))

print("正在创建结果目录...")
os.makedirs('results', exist_ok=True)

print("正在保存作者数据...")
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

print("正在生成 Shields.io 数据...")
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}

print("正在保存 Shields.io 数据...")
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("数据处理完成。")
