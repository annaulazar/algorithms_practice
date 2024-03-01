import json


def check_folder(directory: dict, flag=False):
    if directory.get("files", []):
        for file in directory["files"]:
            if file.endswith('.hack'):
                flag = True
        if flag:
            for _ in directory["files"]:
                counter[0] += 1
    if directory.get("folders", []):
        for folder in directory["folders"]:
            check_folder(folder, flag)


for _ in range(int(input())):
    n = int(input())
    input_json = []
    for _ in range(n):
        input_json.append(input())
    files = json.loads(''.join(input_json))
    counter = [0]
    check_folder(files)
    print(counter[0])


