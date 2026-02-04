# demo1—сравнение чисел
print(42 > 17)
print(42 == 17)
print(42 < 17)

# demo 2—приведение к bool
print(bool("Python"))
aura = "Python"
zen = -3
print(bool(aura))
print(bool(zen))

#demo3— значения, которые дают False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# demo4— объект, который считается False
class GhostBox:
    def __len__(self):
        return 0

shadow = GhostBox()
print(bool(shadow))

# demo 5 функция с логическим результатом
def crystal_switch():
    return True

if crystal_switch():
    print("Доступ разрешён ")
else:
    print("Доступ заблокирован ")
