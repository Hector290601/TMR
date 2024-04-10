#!/usr/bin/env python3
#----->Bibliotecas
#Bibliotecas de ROS
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

#----->Clases
#Clase Nodo Publisher de ROS2 que publica los grados de giro
class Node_Degree_Publisher(Node):
    def __init__(self):
        super().__init__('degrees_node')
        self.publisher_ = self.create_publisher(Int32, 'deegres_topic', 10)
        self.timer_period = 1  #Tiempo de publicación
        self.timer = self.create_timer(self.timer_period, self.publish_degree) #Cuando el timer lo demande, hacer la pregunta si queremos cambiar de angulo

    def deegree_validator (self,degree):
        while True:
            degree= (input("\n ¿Cuantos grados de angulo deseas?: "))
            if degree.isdigit():
                new_deegre= int (degree)
                if  new_deegre>180 or new_deegre<-180:
                    print('\n ---> Esta cantidad de grados puede romper al servo <---\n')
                else:
                    return new_deegre
            else:
                print('\n ---> Tipo de dato no permitido <---\n')

    def publish_degree(self):
        msg = Int32() #Estableciendo el valor del message
        ad=int()
        #-> Sistema de ingreso de datos
        ad=self.deegree_validator(ad)
        #-> Publicando mensaje
        msg.data = ad
        self.publisher_.publish(msg)
        self.get_logger().info('\n Su angulo seleccionado es: "%s" \n' % msg.data)


#----->Funciones
        
#[Funcion main]
def main(args=None):
    #->Inciando nuestro nodo y manteniendolo ejecutando
    rclpy.init(args=args)
    degree_publisher = Node_Degree_Publisher()

    #->Mecanismos de ROS2
    rclpy.spin(degree_publisher) #Elemento para mantener ejecutandoce ros2 (Código spin)
    #->Finalizanod nuestro nodo y ejecución
    degree_publisher.destroy_node() #Destruir publisher cuando terminemos la ejecución
    rclpy.shutdown() #Cerrar ROS2

#----->Ejecucion del programa
if __name__ == '__main__':
    main() #Funcion main