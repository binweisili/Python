"""
 3种方式
"""
# 1
print(type("我要code"))
print(type(13))
print(type(13.14))
print("-----------")
# 2
String_type = type("我要code")
int_type = type(666)
float_type = type(13.14)
print(String_type)
print(int_type)
print(float_type)
print("-----------------")
# 3
name = "一味的code"
name_type = type(name)
print(name_type)