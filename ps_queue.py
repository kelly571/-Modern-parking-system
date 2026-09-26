from custom_queue import NodeBasedQueue

class ParkingSystemQueue:
    def __init__(self):
        self._queue = NodeBasedQueue()

    def add_to_waiting_line(self, vehicle_plate):
        self._queue.enqueue(vehicle_plate)

    def remove_from_waiting_line(self):
        if self._queue.is_empty():
            return None
        return self._queue.dequeue()

    def get_waiting_count(self):
        return len(self._queue)

    def check_is_empty(self):
        return self._queue.is_empty()
