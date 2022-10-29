import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected = True
    else:
        print("Client is not connected")

connected = False

broker_address ="mqtt.eclipseprojects.io"
port=1883


client= mqtt.Client("MQTT")
client.on_connect=on_connect
client.connect(broker_address,port=port)
client.loop_start()
while connected !=True:
    time.sleep(0.2)
    a=10+40 #here a is an integer value but it can be replaced accordingly to get send desired message (eg string ,etc)
client.publish("first",a) #publishing integer to the client
client.loop_stop()

