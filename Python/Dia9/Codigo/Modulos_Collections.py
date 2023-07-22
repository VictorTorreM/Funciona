from collections import Counter,defaultdict,namedtuple

numeros = [5,4,1,2,3,4,567,7,3,3,2,2,2]

frase = "al pan pan y al vino vino"
print(Counter("mississippi"))

print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,1,3,3,3,3,3,4,4,4,4,4])

print(serie.most_common(1))


mi_dic = defaultdict(lambda: "nada")


mi_dic["uno"] = "verde"

print(mi_dic["cuatro"])

print(mi_dic)

Persona = namedtuple("Persona",["nombre","altura","peso"])

ariel = Persona("ariel","156","65")

print(ariel[2])