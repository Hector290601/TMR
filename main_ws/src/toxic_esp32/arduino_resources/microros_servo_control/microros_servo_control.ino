//---->Librerias a utilizar
//Librerias de micro-ros
#include <micro_ros_arduino.h>

#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>

#include <std_msgs/msg/int32.h>

//Libreria para control de servo con ESP32
#include <ESP32Servo.h>


//---->Estableciendo los elementos necesarios para el funcionamiento de nuestro node
rcl_subscription_t subscriber; //En este se declara que usaremos un subscriber
std_msgs__msg__Int32 msg; //Mensaje al cual nos subscribiremos
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;

//---->Defines y variables globales
#define LED_PIN 13 //Pin del led
#define SERVO_PIN 15 //Pin del servo
int ipos=0; //Posicion inicial

Servo servo1; //Servomotor sg90 numero 1
// Podemos controlar y crear 16 objetos tipos Servo en la ESP32


//Checks en caso de que haya un fallo (Siempre necesario)
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

//----[Funciones]----

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
*/
void subscription_callback(const void * msgin)
{  
  const std_msgs__msg__Int32 * msg = (const std_msgs__msg__Int32 *)msgin; //COmprueba si el dato enviado es tipo int32
  servo1.write(int (msg->data));  // Mover el servo al ángulo recibido
  delay(10);
}

/*
void setup(): Funcion principal de Arduino, da ejecución a las variables o elementos iniciales del programa (NECESARIA EN TODOS LOS PROGRAMAS)
*/
void setup() {
  //->Configuracion de microros de transporte de datos
  set_microros_transports();
  
  //->Definiendo los pines de saldia y entrada además de estados iniciales

  //Led
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);  
  
  //Servomotor
  //Activa el timer para localizar el servo en el pin PWM
  servo1.attach(SERVO_PIN,500,2500);//Attach de nuestro servo osea lo relacionamos con un pin
  //Los valores que establecemos son un rango de velocidades que manejara nuestro servo
  servo1.write(ipos); //Inicializando el motor
  delay(15);

 //->Configurando nuestro subscriber
  allocator = rcl_get_default_allocator();
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  //Creando nuestro nodo 
  RCCHECK(rclc_node_init_default(&node, "servo_control", "", &support));

  //Creando nuestro subscriber
  RCCHECK(rclc_subscription_init_default(
    &subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32), //Tipo de mensaje que el subscriber recibira
    "deegres_topic"));

  //Creando un ejecutor esto es un estandar
  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &msg, &subscription_callback, ON_NEW_DATA)); //Aqui establecemos la función callback de nuestro subscriber
}

void loop() {
  //Ejecución normal
  delay(10);
  RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
}
