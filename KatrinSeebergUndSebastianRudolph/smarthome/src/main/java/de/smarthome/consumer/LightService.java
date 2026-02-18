package de.smarthome.consumer;

import de.smarthome.event.PersonArrivedEvent;
import de.smarthome.event.PersonLeftEvent;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class LightService {

    private boolean lightsOn = false;
    private int personsHome = 0;

    @RabbitListener(queues = "light-queue", messageConverter = "messageConverter")
    public void handleArrived(PersonArrivedEvent event) {
        personsHome++;
        lightsOn = true;
        System.out.println("Light turned on for " + event.getPerson());
    }

    @RabbitListener(queues = "light-queue", messageConverter = "messageConverter")
    public void handleLeft(PersonLeftEvent event) {
        personsHome--;
        if (personsHome <= 0) {
            personsHome = 0;
            lightsOn = false;
            System.out.println("Light turned of – nobody home");
        } else {
            System.out.println(event.getPerson() + " left the house, light stays on");
        }
    }
}