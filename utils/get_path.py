import os.path


def get_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'File', 'demo2.jpg')
    return path
# os.path.realpath是获取当前文件路径
# print(os.path.realpath(__file__))

# os.path.dirname是获取上一级文件路径
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# os.path.join选择当前文件路径下的路径，第二个参数表示文件夹名称，第三个参数表示文件名称，注意：文件名称需要加上后缀
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'File','demo2.jpg'))

def download_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'File')
    return path

def del_file():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'File','LATEST_RELEASE')
    return path