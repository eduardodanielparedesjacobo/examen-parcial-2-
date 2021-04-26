#define POTENCIOMETRO
//Usamos una variable de tamaño extendido para el almacenamiento de numero en bits 
long valor;
  
void setup()
{
   Serial.begin(9600); //inicializacion serial los 9600 es la velocidad en baudo
}
  
void loop()
{
  valor = analogRead(A0);// hacemos que lee el valor de pin analogo especificado que en este caso seria el pin A0
  Serial.println(valor);//hacemos la imprecion de datos de nuestra variable valor 
  delay(1000);//hacemos una pausa del programa cada segundo 
}
