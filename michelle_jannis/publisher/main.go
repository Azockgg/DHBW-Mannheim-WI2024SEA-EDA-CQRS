package main

import (
	"github.com/ThreeDotsLabs/watermill"
	"github.com/ThreeDotsLabs/watermill-amqp/v3/pkg/amqp"
	"github.com/ThreeDotsLabs/watermill/message"
)

var amqpURI = "amqp://guest:guest@localhost:5672/"

func main() {
	println("Hello World!")

	amqpConfig := amqp.NewDurableQueueConfig(amqpURI)

	publisher, err := amqp.NewPublisher(amqpConfig, watermill.NewStdLogger(false, false))
	if err != nil {
		panic(err)
	}

	msg := message.NewMessage(watermill.NewUUID(), []byte("Hello, world!"))

	if err := publisher.Publish("example-topic", msg); err != nil {
		panic(err)
	}

	println("Message published successfully to 'example-topic'!")
}
