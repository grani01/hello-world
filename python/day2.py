import json

inputSentence = "John was excited to see his friend John, who introduced him to another John. They all went to John's house, where they met yet another John."
inputWord=['John',"to","all","see","rani"]


def WriteJson(filepath:str,fileJsonlist:list)->None:
        with open(filepath, 'w', encoding='utf-8') as json_file:
           json.dump(fileJsonlist, json_file, ensure_ascii=False, indent=4)

def ReadJson(filepath:str)->None:
        with open(filepath, 'r') as file:
            return json.load(file)

def getWordCount(word:str,sentence:str)->int:
    wordCount = 0
    for _word in sentence.split(" "):
        if word.lower() in _word.lower():
            wordCount+=1
    return wordCount

_list = []
for word in inputWord:
    _list.append({
        "Word": word,
        "Count":getWordCount(word,inputSentence)
    })
# filepath = f"C:\Demo\TestApplication\data.json"
filepath=f"C:/Users/v-grani/Desktop/python/data.json"

data = ReadJson(filepath)
print(_list)
# list(data).append(_list)
# print(data)
WriteJson(filepath,_list)
# WriteJson(filepath,data)
data = ReadJson(filepath)
print(data)
