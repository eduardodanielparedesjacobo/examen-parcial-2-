import serial #hacemos comunicacion con nuestro puerto serial
ser = serial.Serial('COM5', 9600)#abrimos una comunicacion serial en el puerto com5 a una acelaracion de 9600
while True : #hacemos un bucle indefinido
    try:#generamos un bloque que busca erroes y genera exepciones 
        state=ser.readline()#aqui generamos una lista de bits recibidos 
        st = str(state)#aqui hacemos que los bits que envia arduino los codifique en valores numericos
        st = st.replace("b'", "")#reemplasamos la informacion recibida por nueva codificacion 
        st = st.replace("\\r\\n'", "")##reestruturamos 
        num = int(st)#declaramos una nueva variable de numeros enteros 
        print(num)#imprimimos 
    except:#nos permite manejar el error
        pass
