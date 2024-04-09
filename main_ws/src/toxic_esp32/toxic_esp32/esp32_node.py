#!/usr/bin/env python3
#----->Bibliotecas
#Bibliotecas de ROS
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

#----->Clases
#Clase Nodo Publisher de ROS2 que publica los grados de giro
class Node_MIX_Publisher(Node):
    def __init__(self):
        super().__init__('esp32_node')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'esp32_topic', 10)
        self.timer_period = 1  #Tiempo de publicación
        self.timer = self.create_timer(self.timer_period, self.publish_led) #Cuando el timer lo demande, hacer la pregunta si queremos cambiar de angulo
        self.get_logger().info("Publisher Esp32 creado....")

    def select_validator (self, option):
        option=[1,1]
        #---->Selector de opciones 
        while True:
            print("""
                \n
                +================================================================================+
                |  1 -----> Led de Reversa                                                       |
                |  2 -----> Led de Intermitente Izquierda                                        |
                |  3 -----> Led de Intermitente Derecha                                          |
                |  4 -----> Led de Luz Diurna                                                    |
                |  5 -----> Control de Servo                                                     |
                +================================================================================+
                \n  

                    """)
            option [0]= (input("\n Seleccione una opción: "))
            if option [0].isdigit():
                new_op= float (option[0])
                if  new_op>5 or new_op<=0:
                    print('\n ---> Esta entrada no existe <---\n')

                elif new_op ==5:
                    option[0]= float(new_op-1)
                    #----->Selector de grados
                    while True:
                        degree= (input("\n ¿Cuantos grados de angulo deseas? (Rango de 5-50 grados): "))
                        if degree.isdigit():
                            new_deegre= float (degree)
                            if  new_deegre>50 or new_deegre<=5:
                                print('\n ---> Esta cantidad de grados puede romper al servo <---\n')
                            else:
                                option[1]=float(new_deegre)
                                return option
                        else:
                            print('\n ---> Tipo de dato no permitido <---\n')
                else:
                    option[0]= float(new_op-1)
                    
                    #---->Selector de frecuencia
                    while True:
                        print("""
                            \n
                            +================================================================================+
                            | Frecuencia soportada de 0 HZ a 85 MHz                                          |
                            +================================================================================+
                            \n  
                                """)
                                
                        new_op = (input("\n Seleccione su frecuencia (Dato en Hertz): "))
                        if new_op.replace(".", "", 1).isdigit():
                            new_op= float (option[1])
                            if  new_op>85000000 or new_op<0:
                                print('\n ---> Valor fuera del rango permitido <---\n')
                            else:
                                option[1]= new_op
                                return option
                        else:
                            print('\n ---> Tipo de dato no permitido <---\n')      
            else:
                print('\n ---> Tipo de dato no permitido <---\n')

        

    def publish_led(self):
        msg = Float32MultiArray() #Estableciendo el valor del message
        msg.data=[1,1]
        ad = [1,1]
        #-> Sistema de ingreso de datos
        ad=self.select_validator(ad)
        #-> Publicando mensaje
        msg.data= [ad[0],ad[1]]
        self.publisher_.publish(msg)

#----->Funciones
        
#[Funcion main]
def main(args=None):
    #->Inciando nuestro nodo y manteniendolo ejecutando
    rclpy.init(args=args)
    General_publisher = Node_MIX_Publisher()
    #->Mecanismos de ROS2
    rclpy.spin(General_publisher) #Elemento para mantener ejecutandoce ros2 (Código spin)
    #->Finalizanod nuestro nodo y ejecución
    General_publisher.destroy_node() #Destruir publisher cuando terminemos la ejecución
    rclpy.shutdown() #Cerrar ROS2

#----->Ejecucion del programa
if __name__ == '__main__':
    main() #Funcion main