class Student():
    # 一个空的类,pass代表直接跳过
    # 此处pass必须有
    student_id = 1724
    pass

# 定义一个类,用来描述学Python学生
class PythonStudent():
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进层级
    # 2.系统默认self参数
    def doHomework(self):
        print("做作业")
        # 推荐在函数末尾使用return
        return None
# 实例化一个叫std1的学生
std1 = PythonStudent()
print(std1.age)
print(std1.name)
# 注意成员函数的调用没有传递进入参数
std1.doHomework()
# 对象中的成员
print(std1.__dict__)
# 类所有中的成员
print(Student.__dict__)
