import unittest
from unit_converter import Converter


class ConverterTest(unittest.TestCase):
    def test_is_mode(self):
        self.assertEqual(Converter.is_mode("Длина"), True)
        self.assertEqual(Converter.is_mode("дЛиНа"), True)
        self.assertEqual(Converter.is_mode("режим"), False)
        self.assertEqual(Converter.is_mode(""), False)

    def test_is_unit_of_mode(self):
        self.assertEqual(Converter.is_unit_of_mode("Длина", "метр"), True)
        self.assertEqual(Converter.is_unit_of_mode("ДЛина", "мЕтр"), True)
        self.assertEqual(Converter.is_unit_of_mode("Длина", ""), False)
        self.assertEqual(Converter.is_unit_of_mode("", "метр"), False)
        self.assertEqual(Converter.is_unit_of_mode("", ""), False)

    def test_is_float_in_string(self):
        string = "2"
        string2 = "34.23"
        string3 = "0"
        string4 = "-43.2"
        self.assertEqual(Converter.is_float_in_string(string), True)
        self.assertEqual(Converter.is_float_in_string(string2), True)
        self.assertEqual(Converter.is_float_in_string(string3), True)
        self.assertEqual(Converter.is_float_in_string(string4), True)

        self.assertEqual(float(string), 2.0)
        self.assertEqual(float(string2), 34.23)
        self.assertEqual(float(string3), 0.0)
        self.assertEqual(float(string4), -43.2)

    def test_convert_equality(self):
        self.assertEqual(Converter.convert("Длина", "сантиметр", "дециметр", "23"), 2.3)
        self.assertEqual(Converter.convert("Длина", "дециметр", "сантиметр", "0.23"), 2.3)
        self.assertEqual(Converter.convert("Длина", "сантиметр", "дециметр", "23"),
                         Converter.convert("Длина", "дециметр", "сантиметр", "0.23"))

    def test_convert_empty_data(self):
        self.assertEqual(Converter.convert("", "сантиметр", "дециметр", "23"), None)
        self.assertEqual(Converter.convert("Длина", "", "дециметр", "23"), None)
        self.assertEqual(Converter.convert("Длина", "сантиметр", "", "23"), None)
        self.assertEqual(Converter.convert("Длина", "сантиметр", "дециметр", ""), None)

    def test_convert_length(self):
        self.assertEqual(Converter.convert("Длина", "метр", "аршин", "1"), 1.40607424072)
        self.assertEqual(Converter.convert("Длина", "верста", "метр", "1"), 1066.8)
        self.assertEqual(Converter.convert("Длина", "дюйм (США)", "метр", "1"), 0.0254)

    def test_convert_volume(self):
        self.assertEqual(Converter.convert("Объём", "гигалитр", "нанолитр", "1"), 1e+18)
        self.assertEqual(Converter.convert("объём", "миллилитр", "четверик", "100"), 0.00381112085)
        self.assertEqual(Converter.convert("объЁм", "жидкая унция", "кружка", "12"), 0.27048959966)

    def test_convert_mass(self):
        self.assertEqual(Converter.convert("Масса", "пуд", "килограмм", "1"), 16.3807)
        self.assertEqual(Converter.convert("масса", "фунт (сша)", "фунт", "1"), 1.10762720626)
        self.assertEqual(Converter.convert("маСса", "унция (сша)", "грамм", "12"), 340.1942775)

    def test_convert_wrong_types(self):
        self.assertEqual(Converter.convert("Масса", "пуд", "литр", "1"), None)
        self.assertEqual(Converter.convert("объём", "пуд", "литр", "1"), None)
        self.assertEqual(Converter.convert("длина", "пуд", "литр", "1"), None)

    def test_is_unit_of_wrong_mode(self):
        self.assertEqual(Converter.is_unit_of_mode("ДЛина", "метр"), True)
        self.assertEqual(Converter.is_unit_of_mode("ДЛина", "литр"), False)
        self.assertEqual(Converter.is_unit_of_mode("ДЛина", "грамм"), False)

