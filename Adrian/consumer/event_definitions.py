from dataclasses import dataclass
from queue import Queue
from threading import Thread
from typing import Callable


@dataclass(frozen=True)
class StopRequestedEvent:
    event_id: str
    bus_id: str
    occurred_at: str


class EventBus:
    def __init__(self) -> None:
        self._handlers: list[Callable[[StopRequestedEvent], None]] = []
        self._queue: Queue[StopRequestedEvent] = Queue()
        self._worker = Thread(target=self._dispatch_loop, daemon=True)
        self._worker.start()

    def subscribe(self, handler: Callable[[StopRequestedEvent], None]) -> None:
        self._handlers.append(handler)

    def publish(self, event: StopRequestedEvent) -> None:
        self._queue.put(event)

    def _dispatch_loop(self) -> None:
        while True:
            event = self._queue.get()
            for handler in self._handlers:
                handler(event)
            self._queue.task_done()


class EventStore:
    def __init__(self) -> None:
        self.events: list[StopRequestedEvent] = []

    def append(self, event: StopRequestedEvent) -> None:
        self.events.append(event)


class StopStatusProjection:
    def __init__(self) -> None:
        self.total_stop_requests = 0
        self.last_bus_id = None
        self.last_event_at = None

    def apply(self, event: StopRequestedEvent) -> None:
        self.total_stop_requests += 1
        self.last_bus_id = event.bus_id
        self.last_event_at = event.occurred_at

    def to_dict(self) -> dict:
        return {
            "totalStopRequests": self.total_stop_requests,
            "lastBusId": self.last_bus_id,
            "lastEventAt": self.last_event_at,
        }
