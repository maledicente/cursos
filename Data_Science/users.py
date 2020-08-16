#python 2.7
from __future__ import division
from collections import Counter
from collections import defaultdict

def number_of_friends(user):
   # quantos amigos o usuario tem?
   return len(user["friends"])

def not_the_same(user,other_user):
   return user["id"] !=other_user["id"]

def not_friends(user, other_user):
   return all(not_the_same(friend,other_user)
   for friend in user["friends"])

def friends_of_friend_ids(user):
   return Counter(foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if not_the_same(user,foaf) and not_friends(user,foaf))

def data_scientists_who_like(target_interest):
  return [user_id
   for user_id, user_interest in interests
   if user_interest == target_interest]

users = [
   {"id": 0, "name": "Hero"},
   {"id": 1, "name": "Dunn"},
   {"id": 2, "name": "Sue"},
   {"id": 3, "name": "Chi"},
   {"id": 4, "name": "Thor"},
   {"id": 5, "name": "Clive"},
   {"id": 6, "name": "Hicks"},
   {"id": 7, "name": "Devin"},
   {"id": 8, "name": "Kate"},
   {"id": 9, "name": "Klein"}
   ]

friendships = [
               (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
               ]

interests = [
   (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
   (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
   (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
   (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
   (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
   (3, "statistics"), (3, "regression"), (3, "probability"),
   (4, "machine learning"), (4, "regression"), (4, "decision trees"),
   (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
   (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
   (6, "probability"), (6, "mathematics"), (6, "theory"),
   (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
   (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
   (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
   (9, "Java"), (9, "MapReduce"), (9, "Big Data")]

for user in users: user["friends"] = []

for i, j in friendships:
   users[i]["friends"].append(users[j]) # adiciona i como um amigo de j
   users[j]["friends"].append(users[i]) # adiciona j como um amigo de i

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections/num_users

#cria uma lista(user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

#sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)

#print[friend["id"] for friend in users[0]["friends"]]
#print[friend["id"] for friend in users[1]["friends"]]
#print[friend["id"] for friend in users[2]["friends"]]

#print friends_of_friend_ids(users[5])

user_ids_by_interest = defaultdict(list) 
for user_id, interest in interests: 
   user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests: interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id 
    for interest in interests_by_user_id[user["id"]] 
    for interested_user_id in user_ids_by_interest[interest] 
    if interested_user_id != user["id"])