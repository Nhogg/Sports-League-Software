from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb+srv://nathanhogg1223:GvCZzVvOcPOMTtvm@leaguecluster.wnclcwb.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)
    return client['league_db']


if __name__ == "__main__":
    dbname = get_database()
