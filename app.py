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
