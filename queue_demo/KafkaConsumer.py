# 导入安装包
from pykafka import KafkaClient

# 设置客户端的连接信息
client = KafkaClient(hosts="fjr-yz-204-15:9092,fjr-yz-0-134:9092,fjr-yz-0-135:9092")
# 打印所有的topic
# print(client.topics)

client.topics
#  flink_dws_biz_loan_core_assets_repay_plan
# flink_dws_biz_loan_core_assets_loan
topic = client.topics["flink_dws_biz_loan_core_assets_repay_plan"]
#
# print(client.topics)
# print(topic.latest_available_offsets())

# consumer_group 与consumer_id值不能一样，不同group相互独立


consumer = topic.get_simple_consumer(
    consumer_group='18',
    auto_commit_enable=True,
    auto_commit_interval_ms=1,
    # consumer_id =1,
)

for message in consumer:
    if message is not None:
        print(message.offset, message.value.decode("UTF-8"))
