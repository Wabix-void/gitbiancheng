# 方式一 print直接输出
print(type("老铁666"))
print(type(666))
print(type(1.34))
# 方式二 用变量存储
string_type=type("asdfjkl;")
int_type=type(555)
float_type=type(1.342)
print(string_type)
print(int_type)
print(float_type)
# 方式三 用type语句查看变量中存储的数据类型信息
name="syg"
name_type=type(name)
print(name_type)

