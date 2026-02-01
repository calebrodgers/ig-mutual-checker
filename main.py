import json

FOLLOWING_FILE = "following.json"
FOLLOWERS_FILE = "followers_1.json"


def load_following(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    following_usernames = set()

    for entry in data.get("relationships_following", []):
        username = entry.get("title")
        if username:
            following_usernames.add(username.lower())

    return following_usernames


def load_followers(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    follower_usernames = set()

    for entry in data:
        string_list = entry.get("string_list_data", [])
        for item in string_list:
            username = item.get("value")
            if username:
                follower_usernames.add(username.lower())

    return follower_usernames


def main():
    following = load_following(FOLLOWING_FILE)
    followers = load_followers(FOLLOWERS_FILE)

    not_following_back = sorted(following - followers)

    print(f"You follow {len(following)} accounts")
    print(f"You have {len(followers)} followers")
    print(f"\n{len(not_following_back)} accounts do NOT follow you back:\n")

    for username in not_following_back:
        print(username)


if __name__ == "__main__":
    main()
