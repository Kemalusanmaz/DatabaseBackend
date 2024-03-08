import socket
from conf import Configuration as conf
class Client:

    def __init__(self,server_ip,server_port):
         self.server_ip = server_ip
         self.server_port = server_port

    def connect(self):
         
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
        # Sunucuya bağlanma
            client_socket.connect((self.server_ip, self.server_port))
            print("Sunucuya başarıyla bağlanıldı.")

        # Sunucudan mesaj alıp ekrana yazdırma
            # while True:
                # message = client_socket.recv(1024).decode("utf-8")
                # if not message:
                    # break
                # print("Sunucudan gelen mesaj:", message)

        except ConnectionRefusedError:
            print("Bağlantı reddedildi: Sunucu aktif değil veya yanlış IP/port.")
        except Exception as ex:
                print("Bağlantı hatası:", ex)
        finally:
        # Bağlantıyı kapatma
                client_socket.close()


clientConnection = Client("127.0.0.1",9898)
clientConnection.connect()