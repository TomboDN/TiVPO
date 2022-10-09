class UnitDict:
    length_dict = {
        'эксаметр': 1e18,
        'петаметр': 1e15,
        'тераметр': 1e12,
        'гигаметр': 1e9,
        'мегаметр': 1e6,
        'километр': 1e3,
        'гектометр': 1e2,
        'декаметр': 1e1,
        'метр': 1.0,
        'дециметр': 1e-1,
        'сантиметр': 1e-2,
        'миллиметр': 1e-3,
        'микрометр': 1e-6,
        'нанометр': 1e-9,
        'пикометр': 1e-12,
        'фемтометр': 1e-15,
        'аттометр': 1e-18,
        'точка': 0.254e-3,
        'линия': 2.54e-3,
        'дюйм': 2.54e-2,
        'вершок': 4.445e-2,
        'ладонь': 7.5e-2,
        'пядь': 17.78e-2,
        'фут': 30.48e-2,
        'локоть': 45e-2,
        'шаг': 71e-2,
        'аршин': 71.12e-2,
        'сажень': 2.1336,
        'верста': 1.0668e3,
        'миля': 7.4676e3,
        'твип': 1.76388888e-9,
        'мил': 25.4e-6,
        'точка (сша)': 352.778e-6,
        'дюйм (сша)': 25.4e-3,
        'фут (сша)': 0.3048,
        'ярд': 0.9144,
        'миля (сша)': 1.609344e3,
        'звено': 20.117e-2,
        'род': 5.029,
        'чейн': 20.116,
        'фурлонг': 201.168,
        'лига': 4.828e3,
        'морская сажень': 1.8288,
        'кабельтов': 0.219456e3,
        'морская миля': 1.852e3
    }


class Converter:
    @staticmethod
    def is_mode(mode):
        match mode.lower():
            case "длина":
                return True
            case "объём":
                return True
            case "масса":
                return True
            case _:
                return False

    @staticmethod
    def is_unit_of_mode(mode, unit):
        match mode.lower():
            case "длина":
                return unit.lower() in UnitDict.length_dict
            case "объём":
                return unit.lower() in UnitDict.volume_dict
            case "масса":
                return unit.lower() in UnitDict.mass_dict
            case _:
                return False

    @staticmethod
    def is_float_in_string(string):
        pass

    @staticmethod
    def convert(mode, unit1, unit2, value):
        pass


if __name__ == '__main__':
    while True:
        mode = input("Какие единицы измерения конвертировать? (Длина, объем, масса)\n")
        if not Converter.is_mode(mode):
            print("Неправильный режим")
        else:
            unit1 = input("Из какой единицы измерения конвертирвать? (Единственное число, именительный падеж)\n")
            if not Converter.is_unit_of_mode(mode, unit1):
                print("В данном режиме нет такой единицы измерения")
            else:
                unit2 = input("В какую единицу измерения конвертирвать? (Единственное число, именительный падеж)\n")
                if not Converter.is_unit_of_mode(mode, unit2):
                    print("В данном режиме нет такой единицы измерения")
                else:
                    value = input("Значение:\n")
                    if not Converter.is_float_in_string(value):
                        print("Вы ввели не число")
                    else:
                        print("Результат перевода {0} {1} в {2} = {3}".format(value, unit1, unit2,
                                                                              Converter.convert(mode, unit1, unit2,
                                                                                                value)))
        choice = input("Конвертировать снова - Y/y/Д/д, выход - любой другой символ\n")
        if choice.lower() == "y" or choice.lower() == "д":
            pass
        else:
            break
