import MQTT
MQTT.publish_event_to_client('esp8266', 'switch status: ' + IONode.get_input('in1')['event_data']['value'])

