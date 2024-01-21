import threading
from TCPServerClass import dBClient
from TCPServerClass import gatewayServer

#This part is main thread 
   
def runSequence(serverIPAddress,serverPort):
    
    serverInterface = gatewayServer(serverIPAddress,serverPort) #serverInterface variable keeps class with gatewayServer initalize arguments
    serverInterface.createServerSocket() #creating Server socket with the method in the class
    serverInterface.listenSocket() #open to listen server socket with method in the class
    conn,addr = serverInterface.acceptConnection()   #connections is kept in conn and addr variables

    thread = threading.Thread(target=serverInterface.handle_client, args=(conn,addr)) #this is a threat that is targeting to handle_client methond in the gatewayServer class andwhen this threat works, defined arguments send to the method.
    thread.start() #threat is started with this method 
    print(f"Active Connections: {threading.active_count() - 1}") #active threats are shown with threading.active_count method
    # return serverInterface
    
serverIPAddress = "localhost" #local IP address.This variable needs to be local address where run Labview
serverPort = 1000 #local port. This variable needs to add UGKB configuration

runSequence(serverIPAddress,serverPort)

def deleteall(serverIPAddress,serverPort):

    rw = dBClient("ReactionWheelDB","Tachometer TM")
    rw.deleteRecord()
    rw = dBClient("ReactionWheelDB","Direction of Rotation TM")
    rw.deleteRecord()
    rw = dBClient("ReactionWheelDB","Torque TC")
    rw.deleteRecord()
    an = dBClient("AnalogSensorDB","ANV TM")
    an.deleteRecord()
    an = dBClient("AnalogSensorDB","Analog Sensor Monitor TM")
    an.deleteRecord()
    an = dBClient("AnalogSensorDB","Pressure Transducer TM")
    an.deleteRecord()
    mub = dBClient("DigitalInterfacesDB","HPC")
    mub.deleteRecord()
    mub = dBClient("DigitalInterfacesDB","BSM")
    mub.deleteRecord()
# deleteall()