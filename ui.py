import tkinter as tk
from tkinter import messagebox

class HazardReport:
    def __init__(self, location, hazard_type, description):
        self.location = location
        self.hazard_type = hazard_type
        self.description = description

class HazardReportingSystem:
    def __init__(self):
        self.reports = []

    def submit_hazard_report(self, report):
        self.reports.append(report)
        # Additional logic to process and store the report data

    def get_all_reports(self):
        return self.reports

class HazardReportUI:
    def __init__(self, reporting_system):
        self.reporting_system = reporting_system
        self.window = tk.Tk()
        self.window.title("RoadGuard")

        # Hazard Type Options
        self.hazard_types = ["Accident", "Road Construction", "Traffic Jam", "Other"]

        # Location Entry
        self.location_label = tk.Label(self.window, text="Location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(self.window)
        self.location_entry.pack()

        # Hazard Type Selection
        self.hazard_type_label = tk.Label(self.window, text="Hazard Type:")
        self.hazard_type_label.pack()
        self.hazard_type_var = tk.StringVar(self.window)
        self.hazard_type_var.set(self.hazard_types[0])
        self.hazard_type_dropdown = tk.OptionMenu(self.window, self.hazard_type_var, *self.hazard_types)
        self.hazard_type_dropdown.pack()

        # Description Entry
        self.description_label = tk.Label(self.window, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.window)
        self.description_entry.pack()

        # Username Entry
        self.username_label = tk.Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        # Password Entry
        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_report)
        self.submit_button.pack()

    def submit_report(self):
        location = self.location_entry.get()
        hazard_type = self.hazard_type_var.get()
        description = self.description_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password!")
            return

        if not location or not description:
            messagebox.showerror("Error", "Please fill in all the fields!")
            return

        # Validate user credentials (dummy validation for demonstration purposes)
        if not self.validate_user(username, password):
            messagebox.showerror("Error", "Invalid username or password!")
            return

        report = HazardReport(location, hazard_type, description)
        self.reporting_system.submit_hazard_report(report)
        messagebox.showinfo("Success", "Hazard report submitted successfully!")
        self.clear_form()

    def validate_user(self, username, password):
        # Dummy validation for demonstration purposes
        valid_users = {
            "user1": "password1",
            "user2": "password2",
            # Add more users and passwords as needed
        }
        return username in valid_users and valid_users[username] == password

    def clear_form(self):
        self.location_entry.delete(0, tk.END)
        self.hazard_type_var.set(self.hazard_types[0])
        self.description_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

# Usage example
hazard_system = HazardReportingSystem()

# Submit hazard reports
report1 = HazardReport("Location1", "Accident", "Car accident on Main Street")
hazard_system.submit_hazard_report(report1)

report2 = HazardReport("Location2", "Road Construction", "Road construction work causing delays")
hazard_system.submit_hazard_report(report2)

# Get all hazard reports
all_reports = hazard_system.get_all_reports()
print("All Hazard Reports:")
for report in all_reports:
    print(f"Location: {report.location}, Type: {report.hazard_type}, Description: {report.description}")

# Usage example
reporting_system = HazardReportingSystem()
ui = HazardReportUI(reporting_system)
ui.run()
