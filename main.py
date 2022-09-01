import json
import random
import logging


class UserDataLoder:

    def getSeparatorPath(self):  # zamknięcie w funkcji
        separator_path = input("Separators file location: ")
        if separator_path == "":
            separator_path = "./configs/data_separators.jason"
        else:
            separator_path = separator_path
        return (separator_path)

    def getFilePath(self):
        file_path = input("Data collected file location: ")
        if file_path == "":
            file_path = "./configs/data_config2.jason"
        else:
            file_path = file_path
        return (file_path)


class SpliterMixer:
    def SplitingFunction(self, imput_login_list):  # self jako ............
        splited_imput_login_list = []
        for x in imput_login_list:
            split_1 = x.split(" ")
            if len(split_1) != 1:
                splited_imput_login_list.extend(split_1)
            split_2 = x.split(".")
            if len(split_2) != 1:
                splited_imput_login_list.extend(split_2)
            split_3 = x.split("-")
            if len(split_3) != 1:
                splited_imput_login_list.extend(split_3)
            splited_imput_login_list.append(x)
        return (splited_imput_login_list)


class LoderEngine:
    def getJasonDataFromFile(self, separator_path):
        with open(separator_path, "r") as fp:  # with open otwiera i zamyka plik
            sep_load = json.load(fp)
        return sep_load

    def getJsonFilePath(self, file_path, sep_load):
        with open(file_path, "r") as fp:  # with open otwiera i zamyka plik
            dat_load = json.load(fp)
        sep_list = list(sep_load.values())
        print(sep_list)
        return sep_list, dat_load


def run():
    loder_engine = LoderEngine()

    spliter_mixer = SpliterMixer()

    user_data_loder = UserDataLoder()  # wywołanie klas dynamicznych

    logging.basicConfig(level=logging.DEBUG, filename="logs/logi.txt")  # todo: zancznik czasowy

    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    separator_path = user_data_loder.getSeparatorPath()  # wywołanie

    logger.debug("Separators file uploaded232")
    logging.warning("Separators file uploaded")

    # separator_path = "./configs/data_separators.jason"

    sep_load = loder_engine.getJasonDataFromFile(separator_path)

    file_path = user_data_loder.getFilePath()

    # "./configs/data_config2.jason" # TODO dopisac możliwośc z lini komend

    logging.debug("Data collected file uploaded")
    logging.debug("Login generator starts")

    sep_list, dat_load = loder_engine.getJsonFilePath(file_path, sep_load)  # zwraca dwie zmienne

    imput_login_list = list(dat_load.values())

    splited_imput_login_list = spliter_mixer.SplitingFunction(imput_login_list)

    # imput_separator_list = ["", "_", ".", "-"] # TODO wyrzucić do jsona

    random_data = random.choice(imput_login_list)
    random_data2 = random.choice(imput_login_list)
    random_sign = random.choice(separator_path)
    radom_login = random_data + random_sign + random_data2
    print(random_data)

    for x in splited_imput_login_list:
        for y in separator_path:
            for z in splited_imput_login_list:
                print(x + y + z)


run()
