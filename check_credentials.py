
#Not finished, authentication logic needs some work
import pymongo
from pymongo import MongoClient


def check_credentials(username, password):
    CONNECTION_STRING = "mongodb+srv://nathanhogg1223:GvCZzVvOcPOMTtvm@leaguecluster.wnclcwb.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)
    coaches = client.Coaches
    players = client.Players

    coach_data = coaches.find_one({"username": username, "password": password})
