import yaml


def get_data():
    with open("..//config//test01.yaml","r",encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data

if __name__ == '__main__':
    print(get_data()['mobile_params'])