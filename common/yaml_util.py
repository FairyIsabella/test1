import os
import yaml


# 获得项目的根路径
def get_object_path():
    path = os.path.abspath(os.getcwd().split('common')[0])
    # path = os.getcwd().split('common')[0]
    return path

def read_config_file(node1,node2):
        with open(get_object_path()+'config.yml',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[node1][node2]

# 读取extract.yml文件
def read_extract_file(node):
    with open(get_object_path() + 'extract.yml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[node]

# 写入extract.yml文件
def write_extract_file(data):
    with open(get_object_path()+'extract.yml', encoding='utf-8',mode='a') as f:
        yaml.dump(data,stream=f,allow_unicode=True)


# 清空extract.yml文件
def clear_extract_file():
    with open(get_object_path()+'extract.yml', encoding='utf-8',mode='w') as f:
        f.truncate()


if __name__ == '__main__':
    print(read_config_file('Env','test_base_url'))