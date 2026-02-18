package de.smarthome.consumer;

import de.smarthome.event.PersonArrivedEvent;
import de.smarthome.event.PersonLeftEvent;
import de.smarthome.readmodel.HomeStatus;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class QueryService {

    private HomeStatus status = new HomeStatus();

    @RabbitListener(queues = "query-queue", messageConverter = "messageConverter")
    public void handleArrived(PersonArrivedEvent event) {
        status.getPresentPersons().add(event.getPerson());
        status.setLightsOn(true);
        status.setTemperature(22);
    }

    @RabbitListener(queues = "query-queue", messageConverter = "messageConverter")
    public void handleLeft(PersonLeftEvent event) {
        status.getPresentPersons().remove(event.getPerson());
        if (status.getPresentPersons().isEmpty()) {
            status.setLightsOn(false);
            status.setTemperature(16);
        }
    }

    public HomeStatus getStatus() {
        return status;
    }
}