from faker import Faker

myfake = Faker()

Faker.seed(2)

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())

# myfake = Faker('ko_KR')

# print(myfake.name())
# print(myfake.address())
# # print(myfake.text())
# # print(myfake.state())
# # print(myfake.sentence())
# print(myfake.random_number())