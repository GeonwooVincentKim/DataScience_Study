users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "David"}
]

for i in users:
    print("id : {0}".format(i["id"]))
    print("name : " + i["name"])
    print("\n")

for user in users:
    user["friends"] = []
    print(user["friends"])


friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for i in friendships:
    print("me: {0}".format(i))
    print("friends: {0}".format(friendships[0]))
    print("--------------------")

def find_users(i, users):
    for i in users:
        print("users: {0}".format(i))

    for i in user["friends"]:
        if user["friends"] == "":
            print("i -> {0} -- user[friends] -> {1}".format(i, user["friends"]))

        else:
            print("Not Null")


if __name__ == "__main__":
    for i in users:
        find_users(i, users)
