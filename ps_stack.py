from custom_stack import NodeBasedStack

class ParkingSystemStack:
    def __init__(self):
        self._stack = NodeBasedStack()

    def record_action(self, action_type, vehicle_plate):
        self._stack.push((action_type, vehicle_plate))

    def revert_last_action(self):
        if self._stack.is_empty():
            return None
        return self._stack.pop()

    def get_history_count(self):
        return len(self._stack)

    def check_is_empty(self):
        return self._stack.is_empty()
