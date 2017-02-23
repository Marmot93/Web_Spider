import pymongo

client = pymongo.MongoClient('localhost',27017)     #  接口到mongodb 本地服务器locoalhost 27017
walden = client['walden']                      # 创建标签瓦尔登
sheet_tab = walden['sheet_tab']               # 在瓦尔登里创建sheet_line  在什么里面创建对象就是方括号字符串

# with open('D:\walden.txt','r') as f :
#     lines = f.readlines()
#     for index,line  in enumerate(lines) :
#         data = {
#             'index':index,
#             'words': len(line.split()),
#             'line':line,
#         }
#         sheet_tab.insert_one(data)
        # print(data)

for item in sheet_tab.find():
    print(item['line'])