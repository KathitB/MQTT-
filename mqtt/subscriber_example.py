import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected = True
    else:
        print("Client is not connected")

def on_message(client,userdata,message):
    print("Message Recieved : " +str(message.payload.decode("utf-8"))) # message to be recieved can be either string or number
    print("Topic : "+str(message.topic))

connected = False
Messagerecieved =False

broker_address ="mqtt.eclipseprojects.io" #server address
port=1883 #server port

client= mqtt.Client("MQTT")
client.on_message=on_message
client.on_connect=on_connect
client.connect(broker_address,port=port) #connecting subsriber to publisher
client.subscribe("second")
client.loop_start()

while connected !=True:
    time.sleep(0.2)
while Messagerecieved !=True:
    time.sleep(0.2)
client.loop_stop()