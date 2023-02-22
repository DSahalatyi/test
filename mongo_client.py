# from pymongo import MongoClient
#
#
# class SetupMongoDB:
#     def __init__(self):
#         self.client = MongoClient("mongodb://127.0.0.1:27017/test-food-shop")
#         self.database = self.client["test-food-shop"]
#         self.users = self.database["users"]
#         self.tokens = self.database["tokens"]
#         self.fooditems = self.database["fooditems"]
#         self.foodsections = self.database["foodsections"]
#
#
#
#
#
# mongodb = SetupMongoDB()
# print(mongodb.client)
# import requests
#
# requests.post()
import json
payload = {"name": "Ice Cream",
               "food_section": "",
               "ordering_priority": 123,
               "price": 22.2,
               "image": "image",
               "is_available": True
               }
print(payload, "\n", json.dumps(payload))