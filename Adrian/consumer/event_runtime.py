from event_definitions import EventBus, EventStore, StopRequestedEvent, StopStatusProjection


event_bus = EventBus()
event_store = EventStore()
projection = StopStatusProjection()


def handle_stop_requested(event: StopRequestedEvent):
    projection.apply(event)


event_bus.subscribe(handle_stop_requested)
