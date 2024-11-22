import json

# 数据预处理
def create_data(filename,wname):
    with open(filename,'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            text=[]
            labels=[]
            new_data={}
            line = json.loads(line)
            text=line["text"]
            labels = line["label"]
            # ["Location", "Location_Bluetooth", "Location_Cell_Tower", "Location_GPS", "Location_Wi
            for label in labels:
                new_data["text"] = text
                new_data["label"] = label
                with open(wname,'a',encoding='utf-8') as w:
                    w.write(json.dumps(new_data)+'\n')
create_data('./data/data/valid.json','./new_data/valid.json')