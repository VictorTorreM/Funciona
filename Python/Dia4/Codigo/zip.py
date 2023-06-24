nombre = ["Ana","Hugo","Viti"]
edades =[65,29,42,55]
ciudades = ["Madrid","Mexico","Lima"]
combinados = list(zip(nombre,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")
    
    
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(capitales,paises))
for pais,capital in combinado:
    print(f"La capital de {pais} es {capital}")



uno   = [" uno" , "um" , "one"]
dos   = ["dos "," dois ", " two"]
tres  = ["tres ", "três" , "three"]
cuatro= ["cuatro ", "quatro", " four"]
cinco = ["cinco", "cinco","five"]

español = ["uno","dos","tres","cuatro","cinco"]
portugues= ["um","dois","três","quatro","cinco"]
ingles = ["one","two","three","four","five"]


numeros = list(zip(español,portugues,ingles))

print(numeros)