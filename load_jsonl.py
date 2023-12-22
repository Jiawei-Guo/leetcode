import jsonlines
from DrissionPage import ChromiumPage
import time
# 用 d 模式创建页面对象（默认模式）
page = ChromiumPage()
 
file_jsonl_path = "leetcode-train.jsonl"
jsonl_path = "leetcode-relation-easy.jsonl"
jsonl_path1 = "leetcode-relation-medium.jsonl" 
with open(file_jsonl_path) as file:
    for item in jsonlines.Reader(file):
        diff = item["difficulty"]
        title = []
        difficulty = []
        title1 = []
        difficulty1 = []
        if diff == "Easy" and int(item["id"]) > 1257:
            url = 'https://leetcode.cn/problems/'+item["slug"]+'/description/'
            page.get(url)
            try:
                page.ele('.svg-inline--fa fa-list-tree absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2').click()
            except Exception as e:
                continue
            relate = page.eles('.text-sm font-medium transition-none text-label-1 dark:text-dark-label-1 hover:text-blue-s dark:hover:text-dark-blue-s')
            level = page.eles('.ml-4 flex-none')
            for num_j, j in enumerate(level):
                level_item = j.child().texts()
                if level_item[0] == '中等':
                    level_item = 'Medium'
                    difficulty.append(level_item)
                    title_item = relate[num_j].texts()
                    title.append(title_item[0])
                if level_item[0] == '困难':
                    level_item = 'Hard'
            data = {
                "id":item["id"],
                "title":item["title"],
                "relate":title,
                "level":difficulty
            }
            print(data)
            with jsonlines.open(jsonl_path,mode="a") as file_jsonl:
                file_jsonl.write(data)
            # time.sleep(10)
        if diff == "Medium" and int(item["id"]) > 1257:
            url = 'https://leetcode.cn/problems/'+item["slug"]+'/description/'
            page.get(url)
            try:
                page.ele('.svg-inline--fa fa-list-tree absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2').click()
            except Exception as e:
                continue
            relate = page.eles('.text-sm font-medium transition-none text-label-1 dark:text-dark-label-1 hover:text-blue-s dark:hover:text-dark-blue-s')
            level = page.eles('.ml-4 flex-none')
            for num_j, j in enumerate(level):
                level_item = j.child().texts()
                if level_item[0] == '困难':
                    level_item = 'Hard'
                    difficulty1.append(level_item)
                    title_item = relate[num_j].texts()
                    title1.append(title_item[0])
            data = {
                "id":item["id"],
                "title":item["title"],
                "relate":title1,
                "level":difficulty1
            }
            print(data)
            with jsonlines.open(jsonl_path1,mode="a") as file_jsonl1:
                file_jsonl1.write(data)
            # time.sleep(10)
        
            