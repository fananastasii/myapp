from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

company1 = {
    "company_id" : 1,
    "company_name" : "Google"
}
company2 = {
    "company_id" : 2, 
    "company_name" : "Amazon" 
}

companies = {
    1: company1,
    2: company2
}

profile1 = {
    "profile_id" : 1,
    "name" : "Anastasia",
    "last_name" : "Pletneva",
    "username" : "a.pletneva",
    "password" : generate_password_hash("1234"),
    "picture": "photo1.jpeg",
    "position": "Developer", 
    "experience" : [company1, company2]
}
profile2 = { 
    "profile_id" : 2,
    "name" : "Bob",
    "last_name" : "Smith",
    "username" : "b.smith",
    "password" : generate_password_hash("1234"),
    "picture": "photo2.jpeg",
    "position": "Designer"
}

test_profiles = {
    1 : profile1,
    2 : profile2
}

usernames_to_profiles = {
    "a.pletneva" : 1,
    "b.smith" : 2
}
