
eleccion1 = input("Estas en un bosque, hacia donde quieres ir? derecha o izquierda Escribe ")
if eleccion1 == "derecha":
    print("Caiste en un agujero, Game Over")

if eleccion1 == "izquierda":
    print("Llegaste a un lago, hay una isla en medio del lago. escribe que quieres hacer ")
    
eleccion2 = input("Quieres nadar hasta la isla, esperar rescate, o sentarte a la orilla  " )
    
if eleccion2 == "nadar hasta la isla":
    print("Te comio una bestia marina, Game Over")
    
if eleccion2 == "sentarte en la orilla":
    print("subio la marea y te ahogaste.Game over")
    
if eleccion2 == "esperar rescate":
    print("llego un bote y te llevo a la isla, Llegaste a una casa con 3 puertas coloridas ")

eleccion3 = input("Que puerta quieres abrir? la roja, la amarilla o la azul? ")
    
if eleccion3 == "la azul":
    print("Te comio una bestia, Game Over")
    
if eleccion3 == "la amarilla":
    print("te quemaste con fuego, Game Over")
    
if eleccion3 == "la roja":
    print("Has entrado a la casa del tesoro,donde buscaras??")
    
eleccion4 = input("hacia donde buscaras: en la habitacion, sotano o cobertizo? escribe ")

if eleccion4 == "en la habitacion":
    print("sale un fantasma y te roba la energia. Game over")
    
if eleccion4 == "sotano":
    print("sale un gran mostruo hambriento y te devora.Game over")
    
if eleccion4 == "cobertizo":
    print("has encontrado el mapa del tesoro hacia donde apunta norte, sur, este u oeste?")
    
eleccion5 = input("hacia donde vas:norte, sur, este u oeste? ")

if eleccion5 == "norte":
    print("te ha salido un perro de tes cabezas y te ha herido.Game over")
    
if eleccion5 == "sur":
    print("has llegado al tesoro, solo cava y lo encontraras, eres el ganador!")
    
else:
    print("Game over!!")
    
    
    

