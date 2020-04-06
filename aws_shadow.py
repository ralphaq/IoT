import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

# For certificate based connection
myShadowClient = AWSIoTMQTTShadowClient("myClientID")
#myShadowClient.configureEndpoint("-", 8$
#myShadowClient.configureCredentials("/home/pi/aws/AmazonRootCA1.pem","/home/pi/aws/c$
myShadowClient.configureEndpoint("endpoint", 8883)
myShadowClient.configureCredentials("/home/pi/aws/AmazonRootCA1.pem","/h.key","/home/pi/aws/ccate.$

#myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
#myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec
#myMQTTClient.connect()
myMQTTClient = myShadowClient.getMQTTConnection()
myMQTTClient.connect()
data  = {
    "state" : {
        "desired" : {
            "color" : "red",
            "power" : "on"
         }
     }
}
myMQTTClient.publish("$aws/things/test/shadow/update", json.dumps(data), 1)
myMQTTClient.disconnect()



