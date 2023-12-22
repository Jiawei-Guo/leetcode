import jsonlines
from DrissionPage import ChromiumPage
import time
# 用 d 模式创建页面对象（默认模式）
 
# file_jsonl_path = "leetcode-train.jsonl"
jsonl_path = "leetcode-relation-easy.jsonl"
jsonl_path1 = "leetcode-relation-medium.jsonl" 
jsonl_path2 = "leetcode-chain.jsonl"
# with open(jsonl_path) as file:
#     for item in jsonlines.Reader(file):
#         for i in item["relate"]:
#             data = {
#                 "Easy": item["title"],
#                 "Medium": i,
#             }
#             print(data)
#             with jsonlines.open(jsonl_path2, mode="a") as file_jsonl:
#                 file_jsonl.write(data)


with open(jsonl_path1) as file1:
    for item1 in jsonlines.Reader(file1):
        for j in item1["relate"]:
            data = {
                "Medium": item1["title"],
                "Hard": j,
            }
            print(data)
            with jsonlines.open(jsonl_path2, mode="a") as file_jsonl:
                file_jsonl.write(data)

                  
            