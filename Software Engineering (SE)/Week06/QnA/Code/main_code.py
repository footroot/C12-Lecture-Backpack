import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from typing import List
from employees_definitions import *

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.employees = []
        self.large_font = tkFont.Font(family="Helvetica", size=13)
        self.create_widgets()
       
    def create_widgets(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Add Employee", padding="10", )
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
       
        # Basic input fields
        ttk.Label(input_frame, text="Name:", font=self.large_font).grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.name_var, font=self.large_font).grid(row=0, column=1, padx=5)
       
        ttk.Label(input_frame, text="ID:", font=self.large_font).grid(row=1, column=0, sticky="w")
        self.id_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.id_var, font=self.large_font).grid(row=1, column=1, padx=5)
       
        ttk.Label(input_frame, text="Salary:", font=self.large_font).grid(row=2, column=0, sticky="w")
        self.salary_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.salary_var, font=self.large_font).grid(row=2, column=1, padx=5)
       
        ttk.Label(input_frame, text="Role:", font=self.large_font).grid(row=3, column=0, sticky="w")
        self.role_var = tk.StringVar()
        roles = ["Developer", "Team Lead", "Manager", "Business Analyst", "CEO"]
        role_combo = ttk.Combobox(input_frame, textvariable=self.role_var, values=roles)
        role_combo.grid(row=3, column=1, padx=5)
        role_combo.set(roles[0])
       
        # Additional info frame
        self.additional_frame = ttk.LabelFrame(input_frame, text="Additional Information", padding="5")
        self.additional_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="nsew")
       
        # Add button
        ttk.Button(input_frame, text="Add Employee", command=self.add_employee).grid(row=5, column=0, columnspan=2, pady=10)
       
        # Display Frame
        display_frame = ttk.LabelFrame(self.root, text="Employees", padding="10")
        display_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
       
        # Treeview for employees
        self.tree = ttk.Treeview(display_frame, columns=("Name", "ID", "Role", "Salary", "Skills"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Role", text="Role")
        self.tree.heading("Salary", text="Salary")
        self.tree.heading("Skills", text="Skills")
        self.tree.grid(row=0, column=0, pady=5)
       
        # Compare button
        ttk.Button(display_frame, text="Compare Selected Salaries",
                    command=self.compare_salaries).grid(row=1, column=0, pady=5)
       
    def update_additional_fields(self, *args):
        for widget in self.additional_frame.winfo_children():
            widget.destroy()
           
        role = self.role_var.get()
       
        # Role-specific fields
        if role == "Developer":
            ttk.Label(self.additional_frame, text="Programming Languages (comma-separated):", font=self.large_font).pack()
            self.languages_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.languages_var).pack()
           
            ttk.Label(self.additional_frame, text="Technical Certifications (comma-separated):", font=self.large_font).pack()
            self.cert_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.cert_var).pack()
           
        elif role == "Team Lead":
            ttk.Label(self.additional_frame, text="Team Size:", font=self.large_font).pack()
            self.team_size_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.team_size_var).pack()
           
            ttk.Label(self.additional_frame, text="Leadership Level (1-5):", font=self.large_font).pack()
            self.leadership_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.leadership_var).pack()
           
        elif role == "Manager":
            ttk.Label(self.additional_frame, text="Department:", font=self.large_font).pack()
            self.department_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.department_var).pack()
           
            ttk.Label(self.additional_frame, text="Leadership Level (1-5):", font=self.large_font).pack()
            self.leadership_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.leadership_var).pack()
           
        elif role == "Business Analyst":
            ttk.Label(self.additional_frame, text="Projects (comma-separated):", font=self.large_font).pack()
            self.projects_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.projects_var).pack()
           
            ttk.Label(self.additional_frame, text="Technical Certifications (comma-separated):", font=self.large_font).pack()
            self.cert_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.cert_var).pack()
           
        elif role == "CEO":
            ttk.Label(self.additional_frame, text="Years of Experience:", font=self.large_font).pack()
            self.experience_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.experience_var).pack()
           
            ttk.Label(self.additional_frame, text="Leadership Level (1-5):", font=self.large_font).pack()
            self.leadership_var = tk.StringVar()
            ttk.Entry(self.additional_frame, textvariable=self.leadership_var).pack()

    def get_skills_summary(self, employee):
        skills = []
        if isinstance(employee, TechnicalSkills):
            skills.append(f"Tech Certs: {len(employee.certifications)}")
        if isinstance(employee, ManagementSkills):
            skills.append(f"Leadership: L{employee.leadership_level}")
        return ", ".join(skills) if skills else "N/A"
            
    def add_employee(self):
        try:
            name = self.name_var.get()
            id = self.id_var.get()
            salary = float(self.salary_var.get())
            role = self.role_var.get()
            
            if role == "Developer":
                employee = Developer(
                    name, id, salary,
                    self.languages_var.get().split(','),
                    self.cert_var.get().split(',')
                )
            elif role == "Team Lead":
                employee = TeamLead(
                    name, id, salary,
                    int(self.team_size_var.get()),
                    int(self.leadership_var.get())
                )
            elif role == "Manager":
                employee = Manager(
                    name, id, salary,
                    self.department_var.get(),
                    int(self.leadership_var.get())
                )
            elif role == "Business Analyst":
                employee = BusinessAnalyst(
                    name, id, salary,
                    self.projects_var.get().split(','),
                    self.cert_var.get().split(',')
                )
            elif role == "CEO":
                employee = CEO(
                    name, id, salary,
                    int(self.experience_var.get()),
                    int(self.leadership_var.get())
                )
                
            self.employees.append(employee)
            skills = self.get_skills_summary(employee)
            self.tree.insert("", "end", values=(name, id, role, f"£{salary:,.2f}", skills))
            
            # Clear inputs
            self.name_var.set("")
            self.id_var.set("")
            self.salary_var.set("")
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid values for all fields")
            
    def compare_salaries(self):
        selected_items = self.tree.selection()
        if len(selected_items) != 2:
            messagebox.showwarning("Warning", "Please select exactly two employees to compare")
            return
            
        emp1_idx = self.tree.index(selected_items[0])
        emp2_idx = self.tree.index(selected_items[1])
        
        emp1 = self.employees[emp1_idx]
        emp2 = self.employees[emp2_idx]
        
        if emp1 > emp2:
            messagebox.showinfo("Salary Comparison", 
                              f"{emp1.name} ({emp1.__class__.__name__}) has a higher salary: £{emp1.salary:,.2f}\n"
                              f"{emp2.name} ({emp2.__class__.__name__}) has a lower salary: £{emp2.salary:,.2f}")
        elif emp1 < emp2:
            messagebox.showinfo("Salary Comparison", 
                              f"{emp2.name} ({emp2.__class__.__name__}) has a higher salary: £{emp2.salary:,.2f}\n"
                              f"{emp1.name} ({emp1.__class__.__name__}) has a lower salary: £{emp1.salary:,.2f}")
        else:
            messagebox.showinfo("Salary Comparison", "Both employees have the same salary")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    app.role_var.trace('w', app.update_additional_fields)
    app.update_additional_fields()
    root.mainloop()