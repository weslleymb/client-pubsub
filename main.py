from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
project_id = "sandbox-testes"
topic_id = "sandbox-testes-topic"
topic_path = publisher.topic_path(project_id, topic_id)

print("topic_path")