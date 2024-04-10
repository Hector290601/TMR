#!/usr/bin/env python3
#----->Bibliotecas
#Bibliotecas de ROS
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

#----->Clases
#Clase Nodo Publisher de ROS2 que publica los grados de giro
class Node_LED_Publisher(Node):
    def __init__(self):
        super().__init__('led_configuration_node')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'led_topic', 10)
        self.timer_period = 1  #Tiempo de publicación
        self.timer = self.create_timer(self.timer_period, self.publish_led) #Cuando el timer lo demande, hacer la pregunta si queremos cambiar de angulo
        self.get_logger().info("Publisher de leds creado")

    def led_validator (self, led):
        led=[1,1]
        #---->Selector de Leds
        while True:
            print("""
                \n
                +================================================================================+
                |  1 -----> Led de Reversa                                                       |
                |  2 -----> Led de Intermitente Izquierda                                        |
                |  3 -----> Led de Intermitente Derecha                                          |
                |  4 -----> Led de Luz Diurna                                                    |
                +================================================================================+
                \n  

                    """)
            led [0]= (input("\n Seleccione un Led: "))
            if led [0].isdigit():
                new_led= float (led[0])
                if  new_led>4 or new_led<=0:
                    print('\n ---> Esta entrada no existe <---\n')
                else:
                    led[0]= float(new_led-1)
                    break
            else:
                print('\n ---> Tipo de dato no permitido <---\n')

        #---->Selector de frecuencia
        while True:
            print("""
                \n
                +================================================================================+
                | Frecuencia soportada de 0 HZ a 85 MHz                                          |
                +================================================================================+
                \n  
                    """)
                    
            led [1]= (input("\n Seleccione su frecuencia (Dato en Hertz): "))
            if led[1].replace(".", "", 1).isdigit():
                new_led= float (led[1])
                if  new_led>85000000 or new_led==0:
                    print('\n ---> Valor fuera del rango permitido <---\n')
                else:
                    led[1]= new_led
                    return led
            else:
                print('\n ---> Tipo de dato no permitido <---\n')

    def publish_led(self):
        msg = Float32MultiArray() #Estableciendo el valor del message
        msg.data=[1,1]
        ad = [1,1]
        #-> Sistema de ingreso de datos
        ad=self.led_validator(ad)
        #-> Publicando mensaje
        msg.data= [ad[0],ad[1]]
        self.publisher_.publish(msg)
        print ("\n")
        self.get_logger().info(f'El led número {int (msg.data [0]+1)} a una frecuencia de {msg.data [1]} Hz, ha sido publicado')
        print ("\n")


#----->Funciones
        
#[Funcion main]
def main(args=None):
    #->Inciando nuestro nodo y manteniendolo ejecutando
    rclpy.init(args=args)
    LED_publisher = Node_LED_Publisher()
    #->Mecanismos de ROS2
    rclpy.spin(LED_publisher) #Elemento para mantener ejecutandoce ros2 (Código spin)
    #->Finalizanod nuestro nodo y ejecución
    LED_publisher.destroy_node() #Destruir publisher cuando terminemos la ejecución
    rclpy.shutdown() #Cerrar ROS2

#----->Ejecucion del programa
if __name__ == '__main__':
    main() #Funcion main