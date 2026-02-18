package de.smarthome.consumer;

import de.smarthome.event.PersonArrivedEvent;
import de.smarthome.event.PersonLeftEvent;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class HeatingService {

    private int temperature = 16;
    private int personsHome = 0;

    @RabbitListener(queues = "heating-queue", messageConverter = "messageConverter")
    public void handleArrived(PersonArrivedEvent event) {
        personsHome++;
        temperature = 22;
        System.out.println("temperature set to 22°C for " + event.getPerson());
    }

    @RabbitListener(queues = "heating-queue", messageConverter = "messageConverter")
    public void handleLeft(PersonLeftEvent event) {
        personsHome--;
        if (personsHome <= 0) {
            personsHome = 0;
            temperature = 16;
            System.out.println("temperature set to 16°C – nobody home");
        } else {
            System.out.println(event.getPerson() + " left the house, temperature stays at 22°C");
        }
    }
}