import pika, sys, os, json, asyncio
from kasa import Discover, Credentials

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='events')

    def callback(ch, method, properties, body):
        data = json.loads(body.decode())
        color = data["color"]
        print(f"Received color: {color}")
        asyncio.run(set_light_color(color))

    channel.basic_consume(queue='events',
                        auto_ack=True,
                        on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

async def set_light_color(hsv_data):
            credentials = Credentials(
                username="<insert_email_here>", #email ändern
                password="<insert_password_here>" #passwort ändern
            )
            
            device = await Discover.discover_single("192.168.178.31", credentials=credentials) #set your own ip address
            await device.update()
            await device.set_hsv(hsv_data[0], hsv_data[1], hsv_data[2])
            await device.disconnect()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)