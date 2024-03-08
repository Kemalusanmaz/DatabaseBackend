
class Configuration:
    #mongoDb
    # connnectionString = "mongodb://localhost:27017/" #MongoDb connection string
    connnectionString = "mongodb://rootuser:rootpass@mongodb:27017/" #MongoDb connection string

    #influxdb
    token = "0f48ad9a1c4a43af9643a3c77f6dc4b42df38ffe0d0368551629082a567e5587" #Access token
    org = "tai"
    url = "http://influxdb:8086"
    bucket = "labview"  #Repository

    #Client Information
    serverIPAddress = "0.0.0.0" #Server Computer Ip Address
    socket = 9898 #socket port number. Server opens this port and client shoud connect tihs port.  3.12.0