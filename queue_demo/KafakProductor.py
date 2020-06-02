from pykafka import KafkaClient

host = "fjr-yz-204-15:9092,fjr-yz-0-134:9092,fjr-yz-0-135:9092"
client = KafkaClient(host)
print(client.topics)
topic_producer = client.topics["flink_dws_risk-manager-magpie_asset_info_risk_result"]
producer = topic_producer.get_producer()

for i in range(50):
    msg = "msg : %d" % i
    print(msg)
    producer.produce(msg.encode())
producer.stop()
