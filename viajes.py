import clips  # type: ignore
viajes = clips.Environment() #viajes. asi toca declarar todo y creamos el entorno
viajes.clear()

# 1 DESTINO + CLIMA

# Playa
viajes.build("""(defrule playa-calido (destino playa)(clima calido) =>
    (assert (recomendacion "Empaca ropa ligera, bloqueador solar y gafas de sol")))""")

viajes.build("""(defrule playa-frio (destino playa)(clima frio) =>
    (assert (recomendacion "Aunque es playa, lleva ropa ligera para el dia, chaqueta para la noche y zapatos cerrados")))""")

viajes.build("""(defrule playa-lluvioso (destino playa)(clima lluvioso) =>
    (assert (recomendacion "Empaca ropa ligera y de secado rapido, impermeables y ten cuidado en las olas")))""")

# Montaña
viajes.build("""(defrule montaña-calido (destino montaña)(clima calido) =>
    (assert (recomendacion "Ropa ligera y transpirable, Calzado comodo para caminar y Repelente de insectos")))""")

viajes.build("""(defrule montaña-frio(destino montaña)(clima frio) =>
    (assert (recomendacion "Abrigo grueso, guantes, bufanda, Linterna y Termo con bebidas calientes")))""")

viajes.build("""(defrule montaña-lluvioso (destino montaña)(clima lluvioso)=>
    (assert (recomendacion "Impermeable, repelente y Botas resistentes al agua")))""")

# Ciudad
viajes.build("""(defrule ciudad-calido (destino ciudad)(clima calido) =>
    (assert (recomendacion "Ropa comoda, botella de agua y gorra")))""")

viajes.build("""(defrule ciudad-frio(destino ciudad)(clima frio) =>
    (assert (recomendacion "chaqueta, guantes, bufanda y Balsamo labial")))""")

viajes.build("""(defrule ciudad-lluvioso(destino ciudad)(clima lluvioso) =>
    (assert (recomendacion "paraguas y llevar chaqueta o impermeable")))""")

# Extranjero
viajes.build("""(defrule extranjero-calido (destino extranjero)(clima calido) =>
    (assert (recomendacion "Ropa fresca, Protector solar y medicamentos personales")))""")

viajes.build("""(defrule extranjero-frio(destino extranjero)(clima frio) =>
    (assert (recomendacion "Ropa térmica, Guantes, bufanda y gorro")))""")

viajes.build("""(defrule extranjero-lluvioso(destino extranjero)(clima lluvioso) =>
    (assert (recomendacion "Impermeable, paraguas portatil y ropa de secado rapido")))""")

# 2 TRANSPORTE

viajes.build("""(defrule transporte-avion(transporte avion) =>
    (assert (recomendacion "No olvidar pasaporte, maleta de mano y restriccion de liquidos")))""")

viajes.build("""(defrule transporte-carro(transporte carro) =>
    (assert (recomendacion "Llevar botiquín, kit de carretera y snacks")))""")

# 3 DURACION

viajes.build("""(defrule duracion-corto(duracion corto) =>
    (assert (recomendacion "Solo lo esencial, equipaje ligero")))""")

viajes.build("""(defrule duracion-medio(duracion medio) =>
    (assert (recomendacion "ropa practica, un libro y kit de aseo personal")))""")

viajes.build("""(defrule duracion-largo(duracion largo) =>
    (assert (recomendacion "Maleta grande, ropa extra y mas dinero")))""")

# 4. ACTIVIDAD

viajes.build("""(defrule actividad-piscina(actividad piscina) =>
    (assert (recomendacion "traje de baño, bloqueador solar y toalla")))""")

viajes.build("""(defrule actividad-senderismo(actividad senderismo) =>
    (assert (recomendacion "botas de trekking, cantimplora con agua y baston de apoyo")))""")

viajes.build("""(defrule actividad-evento(actividad evento) =>
    (assert (recomendacion "Ropa elegante, entradas y dinero extra")))""")

viajes.build("""(defrule actividad-trabajo(actividad trabajo) =>
    (assert (recomendacion "traje formal, laptop y documentos necesarios")))""")

# Función para ejecutar el sistema con hechos seleccionados
def obtener_recomendaciones(hechos):
    # Crear un nuevo entorno cada vez (para no acumular reglas ni hechos)
    entorno = clips.Environment()

    # Copiamos las reglas de viajes al nuevo entorno
    for rule in viajes.rules():
        entorno.build(str(rule))

    # Insertamos hechos del usuario
    for hecho in hechos:
        entorno.assert_string(hecho)

    entorno.run()

    # Recuperamos las recomendaciones
    recomendaciones = []
    for fact in entorno.facts():
        if "recomendacion" in str(fact):
            recomendaciones.append(str(fact))

    return recomendaciones
