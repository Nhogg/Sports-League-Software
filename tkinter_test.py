import tkinter as tk
from tkinter import messagebox
import json
import random
import string
from pymongo_get_database import get_database


class CreateUser:
    def __init__(self, name, position, coach_key, team_name, email_address, phone_number):
        self.coach_key = coach_key
        self.team_name = team_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.name = name
        self.position = position

    def create_player(self, name, team_name, email_address, phone_number):
        self.name = name
        self.team_name = team_name
        self.email_address = email_address
        self.phone_number = phone_number
        return {
            "name": name,
            "team_name": team_name,
            "email_address": email_address,
            "phone_number": phone_number
        }

    def createCoachKey(self):
        return self.name + ''.join(random.choices(string.digits, k=4))

    def create_coach(self, name, team_name, email_address, phone_number):
        self.name = name
        self.team_name = team_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.coach_key = self.createCoachKey()
        return {
            "name": name,
            "team_name": team_name,
            "email_address": email_address,
            "phone_number": phone_number,
            "coach_key": self.coach_key
        }


# (Your CreateTeam class remains unchanged)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("User Management")
        self.pages = {}  # Dictionary to store different pages

        # Variables for login
        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()

        # Variables for create user
        self.create_username = tk.StringVar()
        self.create_email = tk.StringVar()
        self.create_password = tk.StringVar()
        self.confirm_password = tk.StringVar()
        self.create_phone = tk.StringVar()
        self.create_league = tk.StringVar()
        self.create_team_code = tk.StringVar()

        # Widgets for login
        self.login_frame = tk.Frame(master)
        tk.Label(self.login_frame, text="Username:").pack(pady=5)
        tk.Entry(self.login_frame, textvariable=self.login_username).pack(pady=5)
        tk.Label(self.login_frame, text="Password:").pack(pady=5)
        tk.Entry(self.login_frame, textvariable=self.login_password, show="*").pack(pady=5)
        tk.Button(self.login_frame, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(self.login_frame, text="Create User", command=lambda: self.show_page("create_user")).pack(pady=10)

        # Widgets for create user
        self.create_user_frame = tk.Frame(master)
        tk.Label(self.create_user_frame, text="Create User").pack(pady=10)
        tk.Label(self.create_user_frame, text="Username:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_username).pack(pady=5)
        tk.Label(self.create_user_frame, text="Email:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_email).pack(pady=5)
        tk.Label(self.create_user_frame, text="Password:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_password, show="*").pack(pady=5)
        tk.Label(self.create_user_frame, text="Confirm Password:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.confirm_password, show="*").pack(pady=5)
        tk.Label(self.create_user_frame, text="Phone Number:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_phone).pack(pady=5)
        tk.Label(self.create_user_frame, text="League:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_league).pack(pady=5)
        tk.Label(self.create_user_frame, text="Team Code:").pack(pady=5)
        tk.Entry(self.create_user_frame, textvariable=self.create_team_code).pack(pady=5)
        tk.Button(self.create_user_frame, text="Create Player", command=self.create_player).pack(pady=5)
        tk.Button(self.create_user_frame, text="Create Coach", command=self.create_coach).pack(pady=5)

        # Initialize pages
        self.pages["login"] = self.login_frame
        self.pages["create_user"] = self.create_user_frame

        # Show login page initially
        self.show_page("login")

    def show_page(self, page_name):
        page = self.pages.get(page_name)
        if page:
            page.pack()
            for other_page_name, other_page in self.pages.items():
                if other_page_name != page_name:
                    other_page.pack_forget()

    def login_user(self):
        username = self.login_username.get()
        password = self.login_password.get()

        # Add your authentication logic here
        # ...

        messagebox.showinfo("Login", "Login Successful!\nUsername: {}\nPassword: {}".format(username, password))

        # After successful login, show the create user page
        self.show_page("create_user")

    def create_player(self):
        username = self.create_username.get()
        email = self.create_email.get()
        password = self.create_password.get()
        confirm_password = self.confirm_password.get()
        phone = self.create_phone.get()
        league = self.create_league.get()

        # Validate passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Create player data
        user1 = CreateUser(username, "Player", None, None, email, phone)
        player_data = user1.create_player(username, None, email, phone)

        # Update JSON and MongoDB (adjust paths and database names accordingly)
        existing_data = read_json('player_data.json')
        update_json(existing_data, player_data, 'player_data.json')

        # Insert into MongoDB
        dbname = get_database()
        collection_name = dbname["Players"]
        collection_name.insert_one(player_data)

        # Show a success message (you can customize this as needed)
        messagebox.showinfo("Player Created", "Player '{}' created successfully.".format(username))

    def create_coach(self):
        username = self.create_username.get()
        email = self.create_email.get()
        password = self.create_password.get()
        confirm_password = self.confirm_password.get()
        phone = self.create_phone.get()
        league = self.create_league.get()

        # Validate passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Create coach data
        user1 = CreateUser(username, "Coach", None, None, email, phone)
        coach_data = user1.create_coach(username, None, email, phone)

        # Update JSON and MongoDB (adjust paths and database names accordingly)
        existing_data = read_json('coach_data.json')
        update_json(existing_data, coach_data, 'coach_data.json')

        # Insert into MongoDB
        dbname = get_database()
        collection_name = dbname["Coaches"]
        collection_name.insert_one(coach_data)

        # Show the coach page with coach code
        self.show_coach_page(coach_data)

    def show_coach_page(self, coach_data):
        # Create a new page for the coach with coach code
        coach_page = tk.Frame(self.master)

        tk.Label(coach_page, text="Coach Code: {}".format(coach_data["coach_key"])).pack(pady=10)
        tk.Button(coach_page, text="Create Team", command=lambda: self.show_page("create_team")).pack(pady=10)

        # Add the coach page to the dictionary
        self.pages["coach_page"] = coach_page

        # Show the coach page
        self.show_page("coach_page")

    def create_team(self):
        # Create a new page for creating a team
        create_team_page = tk.Frame(self.master)

        tk.Label(create_team_page, text="Create Team").pack(pady=10)
        tk.Label(create_team_page, text="Team Name:").pack(pady=5)
        team_name_entry = tk.Entry(create_team_page)
        team_name_entry.pack(pady=5)
        tk.Label(create_team_page, text="Location:").pack(pady=5)
        location_entry = tk.Entry(create_team_page)
        location_entry.pack(pady=5)
        tk.Label(create_team_page, text="Number of Members:").pack(pady=5)
        num_members_entry = tk.Entry(create_team_page)
        num_members_entry.pack(pady=5)
        tk.Button(create_team_page, text="Create Team", command=lambda: self.create_team_action(team_name_entry.get(),
                                                                                                location_entry.get(),
                                                                                                num_members_entry.get())).pack(
            pady=10)

        # Add the create team page to the dictionary
        self.pages["create_team"] = create_team_page

        # Show the create team page
        self.show_page("create_team")

    def create_team_action(self, team_name, location, num_members):
        coach_name = self.create_username.get()  # Assuming the coach's username is the coach name
        league = self.create_league.get()

        # Validate the input (you may need more validation based on your requirements)
        if not team_name or not location or not num_members:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create team data
        team1 = self.create_team(team_name, coach_name, num_members, league)
        team_data = team1.createTeam(coach_name, num_members, league)

        # Update JSON and MongoDB (adjust paths and database names accordingly)
        existing_data = read_json('team_data.json')
        update_json(existing_data, team_data, 'team_data.json')

        # Insert into MongoDB
        dbname = get_database()
        collection_name = dbname["Teams"]
        collection_name.insert_one(team_data)

        # Show the team join code
        self.show_team_join_code(team_data)

    def show_team_join_code(self, team_data):
        # Create a new page for displaying the team join code
        team_code_page = tk.Frame(self.master)

        tk.Label(team_code_page, text="Team Join Code: {}".format(team_data["join_key"])).pack(pady=10)

        # Add the team code page to the dictionary
        self.pages["team_code_page"] = team_code_page

        # Show the team code page
        self.show_page("team_code_page")


def read_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data


def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def update_json(data, new_entry, filename):
    if isinstance(data, list):
        data.append(new_entry)
    elif isinstance(data, dict):
        data.update(new_entry)
    write_to_json(data, filename)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
