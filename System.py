from parking_operations import SmartParkingManager
import recursion_vs_stack

def start_console_runtime():
    parking_terminal = SmartParkingManager(maximum_bays=3)
    
    while True:
        print("\n" + "#"*50)
        print("     AUTOMATED GARAGE MANAGEMENT INTERFACE")
        print("#"*50)
        print("  [A] Trigger Vehicle Arrival Sequence")
        print("  [B] Trigger Vehicle Departure & Bill Settlement")
        print("  [C] Run Mathematical Factorial Trace (Module Demo)")
        print("  [D] Exit Core Environment Application")
        
        user_intent = input("\nEnter chosen operation key [A-D]: ").strip().upper()
        
        if user_intent == "A":
            car_plate = input("Input Vehicle License Number: ").strip().upper()
            if car_plate: parking_terminal.process_arrival(car_plate)
        elif user_intent == "B":
            car_plate = input("Input Exiting Vehicle License Number: ").strip().upper()
            if car_plate: parking_terminal.process_departure(car_plate)
        elif user_intent == "C":
            digit = int(input("Enter evaluation integer: "))
            print(f" -> Standard Loop output: {recursion_vs_stack.fact_loop(digit)}")
            print(f" -> Native Call-Stack output: {recursion_vs_stack.fact_recurse(digit)}")
            print(f" -> Custom Stack ADT output: {recursion_vs_stack.fact_stack_adt(digit)}")
        elif user_intent == "D":
            print("\nShutting down automated terminal nodes. Operation Terminated.")
            break
        else:
            print("Selection out of bounds. Please input a choice between A and D.")

if __name__ == "__main__":
    start_console_runtime()
