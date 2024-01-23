
class Configuration:
    #mongoDb
    connnectionString = "mongodb://localhost:27017/" #MongoDb connection string

    #influxdb
    token = "0f48ad9a1c4a43af9643a3c77f6dc4b42df38ffe0d0368551629082a567e5587" #Access token
    org = "tai"
    url = "http://localhost:8086"
    bucket = "labview"  #Repository

    #Client Information
    clientIPAddress = "10.41.74.22" #Labview Computer Ip Address
    socket = 1234 #socket port number. Server opens this port and client shoud connect tihs port.  