
# Кортежи — упорядоченные, неизменяемые, допускают дубликаты, индексируемые


# demo 1 —создание кортежей с необычными именами
cosmic_tuple = ("quark", "lepton", "boson")
#если один элемент — запятая обязательна
single_particle = ("neutrino",)
print(type(single_particle))

cosmic_tuple = tuple(("quark", "lepton", "boson"))#двойные скобки
print(cosmic_tuple)

# demo 2проверка наличия элемента + конвертация
if "quark" in cosmic_tuple:
    print("Да, 'quark' присутствует в космическом кортеже")

#конвертация кортежа в список, изменение и обратно в кортеж
particles = ("gluon", "photon", "meson")
particles_list = list(particles)
particles_list[1] = "tachyon"
particles = tuple(particles_list)
print(particles)

#добавление кортежа к другому кортежу
extra_particle = ("graviton",)
cosmic_tuple += extra_particle
print(cosmic_tuple)

del cosmic_tuple  # удаляем кортеж полностью

# demo 3 — распаковка кортежей
fundamentals = ("up", "down", "strange")
(a1, a2, a3) = fundamentals
print(a1)
print(a2)
print(a3)

#распаковка с остатком
particles_mix = ("electron", "muon", "tau", "charm", "bottom")
(x1, x2, *rest_particles) = particles_mix  # * собирает остаток в список
print(x1)
print(x2)
print(rest_particles)

#demo 4 — повторение кортежей
duplicated_particles = particles_mix * 2
print(duplicated_particles)

# demo 5 — методы кортежей
print(particles_mix.index("muon"))   # индекс первого вхождения
print(particles_mix.count("muon"))   # количество вхождений
