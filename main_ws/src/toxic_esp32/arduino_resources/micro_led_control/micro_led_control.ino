//----[Librerias a utilizar]----
#include <micro_ros_arduino.h>

#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>

//Liberias necesarias para el control de nuestro array aunque no sean del tipo de array que buscamos construir
#include <std_msgs/msg/int32.h>
#include <std_msgs/msg/float32_multi_array.h>
#include <std_msgs/msg/int64_multi_array.h>
#include <std_msgs/msg/multi_array_dimension.h>
//--->Libreria de control de tiempos y frecuencia
#include <Ticker.h>

//----[Estableciendo los elementos neesarios para el funcionamiento de nuestro node]----
rcl_subscription_t subscriber; //En este se declara que usaremos un subscriber
//---->Configurando del msg
std_msgs__msg__Float32MultiArray msg;//Mensaje al cual nos subscribiremos

//---->Estableciendo los elementos de ejecución y timers de nuestro controlador
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;
//-->Pines de los leds
int led_r=14;
int led_il=15;
int led_ir=16;
int led_ld=17;

//-->Configuración de encendido y apagado
Ticker blink1;
Ticker blink2;
Ticker blink3;
Ticker blink4;


//----[Defines]---
#define LED_PIN 13 //Mismo led y puerto

//Checks en caso de que haya un fallo (Siempre necesario)
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

//----[Funciones]----
/*
void blinker (intn frecuencia): hace titilar el led en un cierto espacio de tiempo que nosotros requiramos en este caso segundos que mediante una formula podemos convertilo a hertz
*/
void blinker1(){
  digitalWrite(led_r, !digitalRead(led_r));
}

void blinker2(){
  digitalWrite(led_il, !digitalRead(led_il));
}

void blinker3(){
  digitalWrite(led_ir, !digitalRead(led_ir));
}

void blinker4(){
  digitalWrite(led_ld, !digitalRead(led_ld));

}

/*
int hz_to_seg(int val)= Convierte un valor dado en hertz a su version de segundos
*/
float hz_to_seg(float val){
  float seg= 1/val;
  return seg;
}

/*
void error_loop: En caso de que haya un error en nuestro sistema, parpadara el led conectado en el pin 13 (NECESARIA SI QUIERES UN INDICADOR DE ERROR)
*/
void error_loop(){
  while(1){
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    delay(100);
  }
}

/*
void subscription_callback: Establece el callback del subscriber (Siempre necesario)
Un callback de suscriptor es una función que se ejecuta automáticamente cada vez que un nodo suscrito recibe un nuevo mensaje en un topic al que está suscrito. 
*/
void subscription_callback(const void * msgin)
{ //Ejecutando nuestro const void para que sea del mismo tipo de msgs mediante un cast
  const std_msgs__msg__Float32MultiArray * msg = (const std_msgs__msg__Float32MultiArray*)msgin;
  //Si nuestro led funciona
  digitalWrite(LED_PIN, HIGH);
  //--->Accediendo a los valores dados por nuestro publisher y asignandolos a variables
  float led_pin=msg->data.data[0];
  float frechz=msg->data.data[1];
  float frecseg= hz_to_seg(frechz);
  int selector= (int)led_pin;
  
  //Selector de casos
  switch(selector){
    case 0:
      blink1.detach();
      digitalWrite(led_r,HIGH);  
      blink1.attach(frecseg , blinker1);
      break;

    case 1: 
      blink2.detach();
      digitalWrite(led_il,HIGH);  
      blink2.attach(frecseg, blinker2);
      break;

    case 2:
    blink3.detach();
    digitalWrite(led_ir,HIGH);  
    blink3.attach(frecseg , blinker3);
    break;
  
    case 3:
      blink4.detach();
      digitalWrite(led_ld,HIGH);  
      blink4.attach(frecseg , blinker4);
      break;

    default:
      blink1.detach();
      digitalWrite(led_r,LOW);  

      blink2.detach();
      digitalWrite(led_il,LOW);  

      blink3.detach();
      digitalWrite(led_ir,LOW); 

      blink4.detach();
      digitalWrite(led_ld,LOW);  

      error_loop();

  

  }
}

/*
void setup(): Funcion principal de Arduino, da ejecución a las variables o elementos iniciales del programa (NECESARIA EN TODOS LOS PROGRAMAS)
*/
void setup() {
  //Todo similar al publisher, esto es un estandar
  set_microros_transports();
  
  //Si todo funciona bien nuestro led se mantiene encendido
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);

  //Led funcionando inicialmente
  pinMode(led_r,OUTPUT);
  digitalWrite(led_r,LOW);  
  pinMode(led_il,OUTPUT);
  digitalWrite(led_il,LOW);  
  pinMode(led_ir,OUTPUT);
  digitalWrite(led_ir,LOW);  
  pinMode(led_ld,OUTPUT);
  digitalWrite(led_ld,LOW);  

  delay(2000);

//---->Configurando nuestro subscriber
  allocator = rcl_get_default_allocator();


  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  //Creando nuestro nodo 
  RCCHECK(rclc_node_init_default(&node, "led_control", "", &support));

  //Creando nuestro subscriber
  RCCHECK(rclc_subscription_init_default(
    &subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32MultiArray), //Tipo de mensaje que el subscriber recibira
    "led_topic"));

  //---->Configurando nuestro array msg declarado anteriormente para que no tenga datos basura 
  //Seleccionando algunos datos para que nuestro array no este lleno de datos basura en el capacity
  msg.data.capacity=10;
  msg.data.size=0;
  msg.data.data = (float_t*) malloc(msg.data.capacity * sizeof(float_t));
  msg.layout.dim.data = (std_msgs__msg__MultiArrayDimension*) malloc(msg.layout.dim.capacity * sizeof(std_msgs__msg__MultiArrayDimension));
  //Estableciendo configuraciones del layout
  msg.layout.dim.capacity = 10;
  msg.layout.dim.size = 0;
  msg.layout.dim.data = (std_msgs__msg__MultiArrayDimension*) malloc(msg.layout.dim.capacity * sizeof(std_msgs__msg__MultiArrayDimension));
  //Rellenando de datos nuestro msg
  for(size_t i = 0; i < msg.layout.dim.capacity; i++){
      msg.layout.dim.data[i].label.capacity = 10;
      msg.layout.dim.data[i].label.size = 0;
      msg.layout.dim.data[i].label.data = (char*) malloc(msg.layout.dim.data[i].label.capacity * sizeof(char));
  }

  //---->Ejecutando nuestro subscriber mediante un executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &msg, &subscription_callback, ON_NEW_DATA)); //Aqui establecemos la función callback de nuestro subscriber

}

void loop() {
  //Ejecución de nuestra busqueda
  delay(10);
  RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(1000)));
}
