# PALETA DE COLORES:
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


# \\\\\\\\\\INICO DE REGISTRO DE USUARIO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def presentacion():
    print(WHITE + "  <<-------------------------------------->>")
    print(BLUE + "               RUBL0XIL.STUDIOS-GAME")
    print(MAGENTA + "                  COMPANY-BANK ")
    print(WHITE + "  <<-------------------------------------->>\n")


def MENU_CANTIDADES():
    # cantidades de abono
    print("   10.000      >1")
    print("   100.000     >2")
    print("   200.000     >3")
    print("   OTRO        >4")


def CARGADOR_1():
    X = 0
    while X < 101:
        print(MAGENTA + f"{X} \n")
        X += 1


# ALMACEN DE DATOS DE USUARIO
DATA = []
saldo = 0.000
# constante borrable> def presentacion>

while True:
    print(GREEN + "CREAR CUENTA \ REGISTRAR--> 1")
    print(WHITE + "ACCEDER                 --> 2")
    SELECION_OPCION = int(input("Digite el numero :"))

    while SELECION_OPCION > 3 and SELECION_OPCION !=1234567890:
        print(RED + "HA DISGITADO MAL LA OPCION")
        selecion = int(input("Digite el numero :"))

    DATA_usuario_sistema = {}  # este es el acceso de imformacion por parte del usuario
    if SELECION_OPCION == 1234567890:
        def DESPEDIDA_CORDIAL():
            # salido despedida cordial
            print(WHITE + "  <<-------------------------------------->>")
            print(WHITE + f"                       QUE ESTE BIEN  SEÑOR {ACCESO_ADMINISTRADOR}")
            print(YELLOW + f" \t \tsaldo actual :{saldo:.3f}")
            print(YELLOW + "                                    MODO:")
            print(RED + "                                       ADMINISRADOR-CERRADO")
        def recalcacion_MODO():
            # recalcacion de modo
            print(WHITE + "  <<-------------------------------------->>")
            print(WHITE + f"                       SEA BIEN BENID0 SEÑOR:{ACCESO_ADMINISTRADOR}")
            print(YELLOW + "                                     MODO:")
            print(RED + "                                       ADMINISRADOR")


        print(YELLOW + " \n \t \t  \t         MODO ADMINISTRADOR ACTIVADO \n ")

        #   CONTADOR DE INTENTOS (BUCLE MADRE)
        CONTADOR = 1
        while CONTADOR <= 3:
            ACCESO_ADMINISTRADOR = str(input(WHITE + "Nombre de Administaror:")).upper()
            PASSWORD_ADMINISTRADOR = input(WHITE + "Contraseña :")
            # ACCESO ___MODO ADMISTRADOR
            if ACCESO_ADMINISTRADOR == 'RUBIEL' and PASSWORD_ADMINISTRADOR == 'xdd':
                print(GREEN + "LOS DATOS SON CORRECTOS")
                CONTADOR = 4

                recalcacion_MODO()
                # menu-transacciones

                saldo = 300000.000
                print(YELLOW + f"SALDO : {saldo:.3f}")
                print(WHITE + "      DEPOSITAR     >1")
                print(GREEN + "      RETIRAR       <2 ")
                print(CYAN+"MOSTRAR DATA (USUARIOS) <3")
                print(RED + "      salir         >4")
                selecion1 = int(input(WHITE + "Digite el numero :"))
                while selecion1 > 4:
                    print(RED + "Error,esta opcion no se encuentra")
                    selecion1 = int(input(WHITE + "Digite el numero :"))

                # menu de abonos

                if selecion1 == 1:  # OPCION DE ABONOAR A SALDO

                    MENU_CANTIDADES()
                    depositar = int(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                    while depositar > 5:
                        print(RED + "ESTA OPCION NO SE ENCUENTRA")
                        depositar = int(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                    if depositar == 1:
                        saldo += 1000.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    elif depositar == 2:
                        saldo += 100.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    elif depositar == 3:
                        saldo += 200.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    else:

                        depositar1 = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                        saldo += depositar1
                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                elif selecion1 == 2:  # OPCION NUMERO :2 RETIRAR

                    print(YELLOW + f"saldo:{saldo:.3f}")

                    MENU_CANTIDADES()

                    depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                    while depositar > 5:
                        print(RED + "ESTA OPCION NO SE ENCUENTRA")
                        depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))

                    if depositar == 1:
                        saldo -= 1000.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    elif depositar == 2:
                        saldo -= 100.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    elif depositar == 3:
                        saldo -= 200.000

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break

                    else:

                        depositar1 = float(input(GREEN + "CUANTO DESEA RETIRAR:"))
                        while depositar1 > 300000.000:
                            print(RED + "USTED NO POSEE ESTA CANTIDAD DE DINERO")
                            depositar1 = float(input(GREEN + "CUANTO DESEA RETIRAR:"))
                        saldo -= depositar1

                        DESPEDIDA_CORDIAL()
                        presentacion()
                        break


                elif selecion1 == 3: #VISOR DE DATOS

                    recalcacion_MODO()
                    print(BLUE+f"TOTAL DE DATOS:{len(DATA)}")
                    print(RESET+f"{DATA}")

                    DESPEDIDA_CORDIAL()



                else:# OPCION NUMERO 3 :SALIR
                    print(RED + "SALIEDO")

                    DESPEDIDA_CORDIAL()
                    presentacion()
                    CARGADOR_1()

            # fIN DE modo ADMINSTRADOR\/\/\//\/\/\/\

            else:
                if CONTADOR == 3:
                    print(RED + "ERROR, LOS DATOS PRESENTADOS SON ICORRECTOS")
                    print(RED + "\n \t (comunicate con el administrador)")
                    print(RED + " \t ERROR,VUELVA A CARGAR LA PAGINA")
                    presentacion()
                    break
                CONTADOR = CONTADOR + 1
                #  modo ADMINSTRADOR CERRADO:(INTERPRETACION = no registarasda)/\//\/\/\/\
    ###########################################################

    elif SELECION_OPCION == 1:
        print(YELLOW + "....                              RESGISTRANDO\n")

        CREADA_USUARIO = input(WHITE + "Nombre del usuario :")
        DATA.append(CREADA_USUARIO)
        DATA_usuario_sistema["Nombre del usuario :"] = CREADA_USUARIO

        CREADA_PASSWORD = input(WHITE + "Contraseña :")
        DATA.append(CREADA_PASSWORD)
        DATA_usuario_sistema["Contraseña :"] = CREADA_PASSWORD

        BANCO_REFERENCIA = input(WHITE + "Banco de refrecia :")
        DATA_usuario_sistema["Banco de referencia :"] = BANCO_REFERENCIA
        DATA.append(BANCO_REFERENCIA)

        SERIAL_TARJETA = input(WHITE + "Serial de trajeta (7caracteres) :")
        DATA_usuario_sistema["SERIAL TARJETA:"] = SERIAL_TARJETA
        DATA.append(SERIAL_TARJETA)

        # vereficador de caracteres

        cierre_datos_usuario = set(DATA)  # conjunto dre almacen de datos la cual no se podran cambiar

        # continuacion de usuario
        presentacion()
        print(GREEN + "ACCEDIENO y COMPROVANDO IMFORMACON")
        CARGADOR_1()
        print(YELLOW + "TODO EN ORDEN \n")
        presentacion()

        # menu-transacciones
        print(YELLOW + f"SALDO : {saldo:.3f}")
        print(WHITE + "    DEPOSITAR     >1")
        print(BLUE + "     RETIRAR     >2")
        print(RED + "    salir         >3")
        selecion1 = int(input(WHITE + "Digite el numero :"))
        while selecion1 > 3:
            print(RED + "Error,esta opcion no se encuentra")
            selecion1 = int(input(WHITE + "Digite el numero :"))


        def saldo_presentacion_salida():
            DATA_usuario_sistema["saldo:"] = saldo
            print(WHITE + " \n Gracias por usar :")
            presentacion()


        # menu de transferencias
        if selecion1 == 1:  # DEPOSITAR
            MENU_CANTIDADES()

            depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
            while depositar > 5:
                print(RED + "ESTA OPCION NO SE ENCUENTRA")
                depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))

            if depositar == 1:
                saldo += 10.000
                DATA.append(saldo)
                print(YELLOW + f"saldo actual :{saldo:.3f}")
                saldo_presentacion_salida()



            elif depositar == 2:
                saldo += 100.000
                print(YELLOW + f"saldo actual :{saldo:.3f}")
                DATA.append(saldo)
                saldo_presentacion_salida()


            elif depositar == 3:
                saldo += 200.000
                print(YELLOW + f"saldo actual :{saldo:.3f}")
                DATA.append(saldo)
                saldo_presentacion_salida()


            # menu de tranderencua_opcion 4
            elif depositar == 4:
                depositar1 = float(input("CUANTO DESEA DEPOSITAR:"))
                saldo += depositar1
                print(YELLOW + f"saldo actual :{saldo:.3f}")
                DATA.append(saldo)
                saldo_presentacion_salida()

        # OPCION 2 :RETIRAR
        elif selecion1 == 2:
            if saldo > 0:
                print(f"{saldo:.3f}")
                MENU_CANTIDADES()
                depositar = float(input(GREEN + "CUANTO DESEA RETIRAR:"))
                while depositar > 5:
                    print(RED + "ESTA OPCION NO SE ENCUENTRA")
                    depositar = float(input(GREEN + "CUANTO DESEA RETIRAR:"))

                if depositar == 1:
                    saldo -= 10.000
                    DATA.append(saldo)
                    print(YELLOW + f"saldo actual :{saldo:.3f}")
                    saldo_presentacion_salida()
                    print(DATA)


                elif depositar == 2:
                    saldo -= 100.000
                    print(YELLOW + f"saldo actual :{saldo:.3f}")
                    DATA.append(saldo)
                    saldo_presentacion_salida()


                elif depositar == 3:
                    saldo -= 200.000
                    print(YELLOW + f"saldo actual :{saldo:.3f}")
                    DATA.append(saldo)
                    saldo_presentacion_salida()

                    # menu de tranderencua_opcion 4
                elif depositar == 4:
                    depositar1 = float(input("CUANTO DESEA DEPOSITAR:"))
                    saldo -= depositar1
                    print(YELLOW + f"saldo actual :{saldo:.3f}")
                    DATA.append(saldo)
                    saldo_presentacion_salida()
            else:
                print(RED + "usted no tiene este dinero")

        # OPCION 3:SALIR (USUARIO)
        else:
            print(MAGENTA + "saliedo,su cuenta ha sido creada con exito")
            CARGADOR_1()
            print("GRACIAS POR PREFERIRNOS")
            presentacion()
    # ACCESO
    else:
        presentacion()
        print(YELLOW + "....                              ACCESDIENDO A CUENTA\n")

        saldo_1 = 0.000

        CONTADOR = 1
        while CONTADOR <= 3:
            ACCESO_USUARIO = input(WHITE + "Nombre del usuario :")
            PASSWORD = input(WHITE + "Contraseña :")
            if ACCESO_USUARIO in DATA and PASSWORD in DATA:
                print(BLUE + f"SEA BIEN VENIDO SEÑOR@{ACCESO_USUARIO}")
                print("LOS DATOS SON CORRECTOS")
                CONTADOR = 4

                presentacion()
                print(GREEN + "ACCEDIENO y COMPROVANDO IMFORMACON")
                CARGADOR_1()
                print(YELLOW + "TODO EN ORDEN \n")
                presentacion()

                # menu-transacciones
                print(YELLOW + f"SALDO : {saldo:.3f}")
                print(WHITE + "    DEPOSITAR     >1")
                print(BLUE + "     RETIRAR     >2")
                print(CYAN + " MOSTRAR DATOS   <3")
                print(RED + "    salir         >4")

                selecion1 = int(input(WHITE + "Digite el numero :"))
                while selecion1 > 2:
                    print(RED + "Error,esta opcion no se encuentra")
                    selecion1 = int(input(WHITE + "Digite el numero :"))


                def saldo_presentacion_salida():
                    DATA_usuario_sistema["saldo:"] = saldo
                    print(WHITE + " \n Gracias por usar :")
                    presentacion()


                # menu de transferencias
                if selecion1 == 1:  # DEPOSITAR
                    MENU_CANTIDADES()

                    depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                    while depositar > 5:
                        print(RED + "ESTA OPCION NO SE ENCUENTRA")
                        depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))

                    if depositar == 1:
                        saldo += 10.000
                        DATA.append(saldo)
                        print(YELLOW + f"saldo actual :{saldo:.3f}")
                        saldo_presentacion_salida()


                    elif depositar == 2:
                        saldo += 100.000
                        print(YELLOW + f"saldo actual :{saldo:.3f}")
                        DATA.append(saldo)
                        saldo_presentacion_salida()


                    elif depositar == 3:
                        saldo += 200.000
                        print(YELLOW + f"saldo actual :{saldo:.3f}")
                        DATA.append(saldo)
                        saldo_presentacion_salida()


                    # menu de tranderencua_opcion 4
                    elif depositar == 4:
                        depositar1 = float(input("CUANTO DESEA DEPOSITAR:"))
                        saldo += depositar1
                        print(YELLOW + f"saldo actual :{saldo:.3f}")
                        DATA.append(saldo)
                        saldo_presentacion_salida()

                # OPCION 2 :RETIRAR
                elif selecion1 == 2:
                    if saldo > 0:
                        print(YELLOW+f"{saldo:.3f}")
                        MENU_CANTIDADES()
                        depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))
                        while depositar > 5:
                            print(RED + "ESTA OPCION NO SE ENCUENTRA")
                            depositar = float(input(GREEN + "CUANTO DESEA DEPOSITAR:"))

                        if depositar == 1:
                            saldo -= 10.000
                            DATA.append(saldo)
                            print(YELLOW + f"saldo actual :{saldo:.3f}")
                            saldo_presentacion_salida()
                            print(DATA)


                        elif depositar == 2:
                            saldo -= 100.000
                            print(YELLOW + f"saldo actual :{saldo:.3f}")
                            DATA.append(saldo)
                            saldo_presentacion_salida()


                        elif depositar == 3:
                            saldo -= 200.000
                            print(YELLOW + f"saldo actual :{saldo:.3f}")
                            DATA.append(saldo)
                            saldo_presentacion_salida()

                            # menu de tranderencua_opcion 4
                        elif depositar == 4:
                            depositar1 = float(input("CUANTO DESEA DEPOSITAR:"))
                            saldo -= depositar1
                            print(YELLOW + f"saldo actual :{saldo:.3f}")
                            DATA.append(saldo)
                            saldo_presentacion_salida()
                    else:
                        print(RED + "usted no tiene este dinero")


                # MOSTRAR DATOS DEL USUARIO (OPCION 3)
                elif selecion1 == 3:
                    print(YELLOW + "....                              DATOS\n")
                    PASSWORD = input(WHITE + "Contraseña :")
                    if ACCESO_USUARIO in DATA and PASSWORD in DATA:
                        print(BLUE + f"SEA BIEN VENIDO SEÑOR@{ACCESO_USUARIO}")
                        print("LOS DATOS SON CORRECTOS")

                    CONTADOR = 1
                    while CONTADOR <= 3:
                        PASSWORD = input(WHITE + "Contraseña :")
                        if PASSWORD in DATA:
                            print("CONTRASEÑA CORRECTA")
                            print(DATA_usuario_sistema)
                            CONTADOR = 4
                        else:
                            print("ERROR, LOS DATOS SON ICORRECTOS")
                            if CONTADOR == 3:
                                print("comunicate con el administrador")
                            CONTADOR = CONTADOR + 1

                # OPCION 4:SALIR (USUARIO)
                else:
                    CARGADOR_1()
                    print(f"GRACIAS POR PREFERIRNOS SEÑOR@ {ACCESO_USUARIO}")
                    presentacion()

            else:
                print(RED+"ERROR, LOS DATOS SON ICORRECTOS")
                if CONTADOR == 3:
                    print(CYAN+"comunicate con el administrador")
                CONTADOR = CONTADOR + 1