import json

# Define a Trip class to hold trip details
class Trip:
    def _init_(self, destination, start_date, end_date, budget):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget

    def _str_(self):
        return f"Destination: {self.destination}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nBudget: ${self.budget}"

# Function to add a new trip
def add_trip(trip_list):
    destination = input("Enter the destination: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    budget = float(input("Enter the budget for the trip: $"))
    
    # Create a new trip and add to the trip list
    new_trip = Trip(destination, start_date, end_date, budget)
    trip_list.append(new_trip)
    print(f"Trip to {destination} added successfully!")

# Function to view all trips
def view_trips(trip_list):
    if not trip_list:
        print("No trips planned yet.")
    else:
        print("\n--- Your Upcoming Trips ---")
        for idx, trip in enumerate(trip_list):
            print(f"\nTrip {idx + 1}:")
            print(trip)
            print("--------------------------")

# Function to delete a trip by index
def delete_trip(trip_list):
    view_trips(trip_list)
    try:
        trip_index = int(input("Enter the trip number to delete: ")) - 1
        if 0 <= trip_index < len(trip_list):
            deleted_trip = trip_list.pop(trip_index)
            print(f"Trip to {deleted_trip.destination} has been deleted.")
        else:
            print("Invalid trip number.")
    except ValueError:
        print("Invalid input. Please enter a valid trip number.")

# Function to edit a trip by index
def edit_trip(trip_list):
    view_trips(trip_list)
    try:
        trip_index = int(input("Enter the trip number to edit: ")) - 1
        if 0 <= trip_index < len(trip_list):
            trip = trip_list[trip_index]
            print(f"Editing trip to {trip.destination}:")
            trip.destination = input(f"Enter new destination (current: {trip.destination}): ") or trip.destination
            trip.start_date = input(f"Enter new start date (current: {trip.start_date}): ") or trip.start_date
            trip.end_date = input(f"Enter new end date (current: {trip.end_date}): ") or trip.end_date
            trip.budget = float(input(f"Enter new budget (current: ${trip.budget}): ") or trip.budget)
            print(f"Trip to {trip.destination} updated successfully!")
        else:
            print("Invalid trip number.")
    except ValueError:
        print("Invalid input. Please enter a valid trip number.")

# Function to save trips to a file
def save_trips(trip_list, filename):
    with open(filename, 'w') as file:
        json.dump([trip._dict_ for trip in trip_list], file)
    print("Trips saved successfully!")

# Function to load trips from a file
def load_trips(filename):
    try:
        with open(filename, 'r') as file:
            trip_data = json.load(file)
            return [Trip(**trip) for trip in trip_data]
    except FileNotFoundError:
        print("No previous trips found. Starting fresh.")
        return []

# Main function for the travel planner
def travel_planner():
    trip_list = load_trips('trips.json')  # Load trips from a file if it exists

    while True:
        print("\n--- Travel Planner ---")
        print("1. Add a Trip")
        print("2. View All Trips")
        print("3. Edit a Trip")
        print("4. Delete a Trip")
        print("5. Save and Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_trip(trip_list)
        elif choice == '2':
            view_trips(trip_list)
        elif choice == '3':
            edit_trip(trip_list)
        elif choice == '4':
            delete_trip(trip_list)
        elif choice == '5':
            save_trips(trip_list, 'trips.json')
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the travel planner
if _name_ == "_main_":
    travel_planner()