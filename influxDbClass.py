import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS



class influxDbClass:

  
    def __init__(self,token,org,url,bucket):
       self.token = token
       self.org = org
       self.url = url
       self.bucket = bucket

    def connectDb(self):
       try:
        self.write_client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.org)
        # print("InfluxDb ile bağlantı sağlandı")
        
       except Exception as ex:
            print(ex)  

    def disconnectDb(self):
       try:
        self.write_client.close()
        print("InfluxDb ile bağlantı sonlandıırldı")
       except Exception as ex:
          print("InfluxDb ile bağlantı sonlandırılamadı",ex)

    def writeData(self, interface, key1, key2, key3, value1, value2, value3):
        try:
            write_api = self.write_client.write_api(write_options=SYNCHRONOUS)
            point = (
                Point(interface)
                .field(key1, float(value1))
                .field(key2, float(value2))
                .field(key3, float(value3))
            )
            write_api.write(bucket=self.bucket, org=self.org, record=point)
            # print("Veri gönderildi.")
        except Exception as ex:
            print("Veri gönderilemedi.", ex)



    # deneme
    def writeData1(self):
        try:

            
            bucket=self.bucket

            write_api = self.write_client.write_api(write_options=SYNCHRONOUS)
            
            for value in range(5):
                point = (
                    Point("measurement1")
                    .tag("tagname1", "tagvalue1")
                    .field("field1", value)
                    
                )
                write_api.write(bucket=bucket, org="TAI", record=point)
                # time.sleep(1) # separate points by 1 second

            # print("Data gönderildi.")
        except Exception as ex:
           print("Data gönderilemedi.", ex)
       


# # Örnek kullanım
# # token = os.environ.get("INFLUXDB_TOKEN") #token bilgisi environment variable'e kaydedilmişti. os paketinden çekilir.
# token = "Ow9zVHjndViYOZBgDKq2GZYuH_AhfM5FrxHc0vuvkLpIcSneB4Cg6FAhSAQOnRGImA3LPxypVmwQiKleh604Jg=="
# org = "TAI"
# url = "http://localhost:8086"
# bucket = "Labview"

# # influxDbClass sınıfının örneğini oluştur
# influxdatabase= influxDbClass(token, org, url, bucket)

# influxdatabase.connectDb()
# # influxdatabase.disconnectDb()
# influxdatabase.writeData1()
