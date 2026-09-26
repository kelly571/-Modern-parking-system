import time
import math
import db_manager
from custom_stack import BoundedArrayStack
from custom_queue import LinearQueue

class SmartParkingManager:
    def __init__(self, maximum_bays=5):
        self.maximum_bays = maximum_bays
        self.current_occupancy = 0
        self.overflow_line = LinearQueue()
        self.modification_history = BoundedArrayStack()
        db_manager.initialize_tables()

    def process_arrival(self, registration_id):
        if self.current_occupancy < self.maximum_bays:
            timestamp_stamp = str(time.time())
            db_manager.log_vehicle_check_in(registration_id, timestamp_stamp)
            self.current_occupancy += 1
            self.modification_history.push(("IN_PROGRESS", registration_id))
            print(f"[ENTRY LOGGED] '{registration_id}' admitted. Vacant Bays: {self.maximum_bays - self.current_occupancy}")
        else:
            print(f"[BAY THRESHOLD REACHED] Moving '{registration_id}' into external line overflow buffer.")
            self.overflow_line.enqueue(registration_id)

    def process_departure(self, registration_id):
        import sqlite3
        connection = sqlite3.connect(db_manager.DATABASE_PATH)
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT check_in_epoch FROM live_garage WHERE plate_id = ?", (registration_id,))
        record = db_cursor.fetchone()
        connection.close()

        if not record:
            print(f"[DENIED] No checked-in logs match registration values: '{registration_id}'.")
            return

        starting_epoch = float(record)
        total_seconds = time.time() - starting_epoch
        
        computed_hours = math.ceil(total_seconds if total_seconds > 0 else 1)
        calculated_billing = computed_hours * 100
        
        db_manager.drop_active_and_archive(registration_id, computed_hours, calculated_billing)
        self.current_occupancy -= 1
        
        print(f"\n[BILL RECEIPT GENERATED] Car ID: {registration_id}")
        print(f" -> Time Computed: {computed_hours} Hour(s)")
        print(f" -> Amount Billed: KSH {calculated_billing}")
        
        if not self.overflow_line.is_empty():
            dispatched_car = self.overflow_line.dequeue()
            print(f" -> [AUTO-ADVANCE] Advancing car '{dispatched_car}' from queue into open bay...")
            self.process_arrival(dispatched_car)
