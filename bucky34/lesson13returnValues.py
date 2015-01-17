def allowed_to_date(my_age):
    girls_age = my_age/2 + 7
    return girls_age

my_limit = allowed_to_date(33)
creepy_joe = allowed_to_date(49)
print("Javier can date girls ", my_limit, " or older")
print("Creepy Joe can date girls ", creepy_joe, " or older")
