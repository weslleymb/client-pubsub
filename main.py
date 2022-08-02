from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
project_id = "sandbox-testes"
topic_id = "sandbox-testes-topic"
topic_path = publisher.topic_path(project_id, topic_id)

#print(f"Nome do projeto é: {topic_path}")

for i in range(1, 10):
    mensagem = "Número: {}".format(i)
    mensagem_codificada = mensagem.encode("utf-8")
    publisher.publish(topic_path, mensagem_codificada)