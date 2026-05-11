import os.path
import json
import getpass


def load_key(keyname: str) -> object:
    file_name = "Keys.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            Key = json.load(file)

        if keyname in Key and Key[keyname]:
            return Key[keyname]
        else:
            keyval = input("配置文件中没有相应项，请输入对应配置信息：").strip()
            Key[keyname] = keyval

            with open(file_name, "w") as file:
                json.dump(Key, file, indent=4)

            return keyval
    else:
        keyval = input("配置文件中没有相应项，请输入对应配置信息：").strip()
        Key = {
            keyname: keyval
        }

        with open(file_name, "w") as file:
            json.dump(Key, file, indent=4)

        return keyval


if __name__ == "__main__":
    print(load_key("DEEPSEEK_API_KEY"))