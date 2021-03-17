__author__ = 'Crypt0Cr1s'

import  time





def cabezal(posicion):
    cont1 = 0;
    cabeza = "";
    time.sleep(2)

    while(cont1<posicion):
        cabeza=cabeza+" ";
        cont1=cont1+1

    if(cont1==0):
        cabeza = cabeza + "¶";
        return(cabeza)
        cabeza = ""
    else:
        cabeza = cabeza + "¶";
        return(cabeza)





def palindromos(cadena):
    estadoact = "q0";
    posicion = 0;
    cinta =cadena+"      ";
    while estadoact != "q11":
        # ENTRAN A'S

        if (cinta[posicion] == "a" and estadoact == "q0"):
            estadoact = "q1"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "a" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "a" and estadoact == "q5"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q8"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "a" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        # ENTRAN B'S

        elif (cinta[posicion] == "b" and estadoact == "q0"):
            estadoact = "q5"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "b" and estadoact == "q5"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q7"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "b" and estadoact == "q8"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "b" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        # ENTRAN C'S

        elif (cinta[posicion] == "c" and estadoact == "q0"):
            estadoact = "q8"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "c" and estadoact == "q5"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q8"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "c" and estadoact == "q10"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        # ENTRAN ε'S

        elif (cinta[posicion] == " " and estadoact == "q0"):
            estadoact = "q11"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q1"):
            estadoact = "q11"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q2"):
            estadoact = "q3"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q4"):
            estadoact = "q0"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q5"):
            estadoact = "q11"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q6"):
            estadoact = "q7"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q8"):
            estadoact = "q11"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q9"):
            estadoact = "q10"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1
    print("Si es palindromo")





def copia(cadena):
    estadoact = "q0";
    posicion = 0;
    cinta = cadena+"                                                                ";
    while estadoact != "q17":
        # ENTRAN A'S

        if (cinta[posicion] == "a" and estadoact == "q0"):
            estadoact = "q1"
            cinta =" "+cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "a" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q4"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "X" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q8"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "a" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "a" and estadoact == "q10"):
            estadoact = "q10"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "a" and estadoact == "q11"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "a" and estadoact == "q12"):
            estadoact = "q13"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q13"):
            estadoact = "q13"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q14"):
            estadoact = "q14"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q15"):
            estadoact = "q15"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "a" and estadoact == "q16"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        # ENTRAN B'S

        elif (cinta[posicion] == "b" and estadoact == "q0"):
            estadoact = "q1"
            cinta =" "+cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "b" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q4"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "X" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q8"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "b" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "b" and estadoact == "q10"):
            estadoact = "q10"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "b" and estadoact == "q11"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "b" and estadoact == "q12"):
            estadoact = "q14"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q13"):
            estadoact = "q13"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q14"):
            estadoact = "q14"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q15"):
            estadoact = "q15"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "b" and estadoact == "q16"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1



    # ENTRAN C'S

        elif (cinta[posicion] == "c" and estadoact == "q0"):
            estadoact = "q1"
            cinta =" "+cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "c" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q4"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "X" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q8"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "c" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "c" and estadoact == "q10"):
            estadoact = "q10"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "c" and estadoact == "q11"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "c" and estadoact == "q12"):
            estadoact = "q15"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q13"):
            estadoact = "q13"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q14"):
            estadoact = "q14"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q15"):
            estadoact = "q15"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "c" and estadoact == "q16"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        # ENTRAN ε'S


        elif (cinta[posicion] == " " and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == " " and estadoact == "q2"):
            estadoact = "q3"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == " " and estadoact == "q5"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == " " and estadoact == "q6"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == " " and estadoact == "q7"):
            estadoact = "q10"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == " " and estadoact == "q11"):
            estadoact = "q12"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == " " and estadoact == "q16"):
            estadoact = "q17"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            posicion = posicion + 1


        # ENTRAN Y'S


        elif (cinta[posicion] == "Y" and estadoact == "q4"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "Y" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "Y" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "Y" and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "Y" and estadoact == "q8"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "Y" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "Y" and estadoact == "q10"):
            estadoact = "q10"
            cinta = cinta[:posicion] + "Y" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "Y" and estadoact == "q13"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "Y" and estadoact == "q14"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "Y" and estadoact == "q15"):
            estadoact = "q16"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        # ENTRAN Y'S

        elif (cinta[posicion] == "X" and estadoact == "q8"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "a" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1


        elif (cinta[posicion] == "X" and estadoact == "q9"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "b" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)

            posicion = posicion + 1


        elif (cinta[posicion] == "X" and estadoact == "q10"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "c" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1







def multi(no1,no2):
    estadoact = "q0";
    posicion = 0;
    cinta =" "+no1 + " " + no2+"                                                                             "
    while (estadoact != "q13" or estadoact != "q14" or estadoact != "q16"):

         #Entran 1's

        if (cinta[posicion] == "1" and estadoact == "q0"):
            estadoact = "q2"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q7"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q8"):
            estadoact = "q8"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q9"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q10"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q11"):
            estadoact = "q11"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q12"):
            estadoact = "q13"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q13"):
            estadoact = "q13"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q14"):
            estadoact = "q14"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q15"):
            estadoact = "q15"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q16"):
            estadoact = "q16"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        #Entran ε's

        elif (cinta[posicion] == " " and estadoact == "q0"):
            estadoact = "q1"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q1"):
            estadoact = "q14"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q2"):
            estadoact = "q3"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q3"):
            estadoact = "q15"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q4"):
            estadoact = "q5"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q5"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q6"):
            estadoact = "q7"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q7"):
            estadoact = "q9"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q8"):
            estadoact = "q3"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q9"):
            estadoact = "q10"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q10"):
            estadoact = "q12"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q11"):
            estadoact = "q0"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q12"):
            estadoact = "q12"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q15"):
            estadoact = "q16"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1






def suma(no1,no2):
    estadoact = "q0";
    posicion = 0;
    cinta=" "+no1+" "+no2+" "
    while(estadoact != "q4"):

        # ENTRAN 1'S

        if (cinta[posicion]=="1" and estadoact=="q0"):
            estadoact="q1"
            cinta = cinta[:posicion]+"1"+cinta[posicion+1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion=posicion+1

        elif (cinta[posicion] == "1" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q3"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        #ENTRAN VACIOS

        elif (cinta[posicion] == " " and estadoact == "q0"):
            estadoact = "q0"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q2"):
            estadoact = "q3"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q3"):
            estadoact = "q3"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)







def resta(no1,no2):

    estadoact = "q0";
    posicion = 0;
    cinta = no1 + " " + no2+" "

    while(estadoact !="q6" or cinta.__contains__("0")):
        # ENTRAN 1'S

        if (cinta[posicion] == "1" and estadoact == "q0"):
            estadoact = "q0"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza=cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q2"):
            estadoact = "q3"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q3"):
            estadoact = "q3"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "1" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1


        elif (cinta[posicion] == "1" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + "1" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "1" and estadoact == "q7"):
            estadoact = "q0"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

    # ENTRAN 0'S

        elif (cinta[posicion] == "0" and estadoact == "q0"):
            estadoact = "q0"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "0" and estadoact == "q1"):
            estadoact = "q1"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "0" and estadoact == "q2"):
            estadoact = "q2"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "0" and estadoact == "q3"):
            estadoact = "q3"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "0" and estadoact == "q4"):
            estadoact = "q4"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == "0" and estadoact == "q5"):
            estadoact = "q5"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "0" and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == "0" and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + "0" + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        # ENTRAN ε'S

        elif (cinta[posicion] == " " and estadoact == "q0"):
            estadoact = "q1"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q1"):
            estadoact = "q2"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q2"):
            estadoact = "q4"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q3"):
            estadoact = "q7"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q4"):
            estadoact = "q5"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q5"):
            estadoact = "q6"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion - 1

        elif (cinta[posicion] == " " and estadoact == "q6"):
            estadoact = "q6"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

        elif (cinta[posicion] == " " and estadoact == "q7"):
            estadoact = "q7"
            cinta = cinta[:posicion] + " " + cinta[posicion + 1:]
            cabeza = cabezal(posicion)
            print(cinta)
            print(cabeza)
            posicion = posicion + 1

ifmenu = True
while ifmenu == True:
    print("Bienvenido al simulador de maquinas de turing")
    print("Este simulador tiene diferentes opciones")
    print("1.Detector de palindromos")
    print("2.Copia de patrones")
    print("3.Multiplicacion Unario")
    print("4.Suma unaria")
    print("5.Resta unaria")
    print("6.Salir")
    op = input("Ingrese el numero de la opcion que desea ")
    if op == '1':
        cadena = input("ingrese la cadena que desea verificar");
        palindromos(cadena);
    if op == '2':
        cadena = input("ingrese la cadena que desea copiar");
        copia(cadena);
    if op == '3':
        no1 = input("ingrese el primer numero");
        no2 = input("ingrese el primer numero");
        multi(no1,no2);
    if op == '4':
        no1 = input("ingrese el primer numero");
        no2 = input("ingrese el primer numero");
        suma(no1,no2);
    if op == '5':
        no1 = input("ingrese el primer numero");
        no2 = input("ingrese el primer numero");
        resta(no1,no2);
    if op == '6' :
        ifmenu = False


