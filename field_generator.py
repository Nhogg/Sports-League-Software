import random
import string
import json


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


class CreateTeam:
    def __init__(self, team_name, coach_name, member_count, league):
        self.team_name = team_name
        self.coach_name = coach_name
        self.member_count = member_count
        self.league = league
        self.join_key = self.createJoinKey()

    def createJoinKey(self):
        return self.team_name + ''.join(random.choices(string.digits, k=8))

    def createTeam(self, coach_name, member_count, league):
        return {
            "coach_name": coach_name,
            "member_count": member_count,
            "league": league,
            "join_key": self.createJoinKey()
        }


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
    print("Choose an option:")
    print("1. Create a Player")
    print("2. Create a Coach")
    print("3. Create a Team")
    choice = input("Enter the option number (1, 2, or 3): ")

    if choice == "1":
        name = input("Enter player's name: ")
        team_name = input("Enter team name: ")
        email_address = input("Enter email address: ")
        phone_number = input("Enter phone number: ")
        user1 = CreateUser(name, "Player", None, team_name, email_address, phone_number)
        player_data = user1.create_player(name, team_name, email_address, phone_number)
        existing_data = read_json('player_data.json')
        update_json(existing_data, player_data, 'player_data.json')

    elif choice == "2":
        name = input("Enter coach's name: ")
        team_name = input("Enter team name: ")
        email_address = input("Enter email address: ")
        phone_number = input("Enter phone number: ")
        user1 = CreateUser(name, "Coach", None, team_name, email_address, phone_number)
        coach_data = user1.create_coach(name, team_name, email_address, phone_number)
        existing_data = read_json('coach_data.json')
        update_json(existing_data, coach_data, 'coach_data.json')

    elif choice == "3":
        team_name = input("Enter team name: ")
        coach_name = input("Enter coach's name: ")
        member_count = input("Enter member count: ")
        league = input("Enter league: ")
        team1 = CreateTeam(team_name, coach_name, member_count, league)
        team_data = team1.createTeam(coach_name, member_count, league)
        existing_data = read_json('team_data.json')
        update_json(existing_data, team_data, 'team_data.json')

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
