my_dict = {"Имя": "Алексей", "Год рождения": 1990}
print(my_dict)

print(my_dict.get("Имя"))  # Выведет значение по ключу "Имя"
print(my_dict.get("Профессия"))  # Выведет None без ошибки

my_dict["Город"] = "Москва"
my_dict["Хобби"] = "футбол"

print(my_dict)

value_deleted = my_dict.pop("Год рождения")
print(value_deleted)

print(my_dict)