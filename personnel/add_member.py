# =====================================================
#  personnel/add_member.py — คนรับผิดชอบ: Bank
# =====================================================
# from data import family_members

# TODO: สร้างฟังก์ชัน add_member(name, age, power, money)
#   - คำนวณ role: power >= 8 -> "Hitman" | money >= 1000000 -> "Sponsor" | นอกนั้น -> "Slave"
#   - สร้าง dict สมาชิกใหม่ (key: name, age, role, power, money, equipment เริ่มต้น "ไม่มี")
#   - เพิ่มเข้า family_members แล้ว return dict นั้น

add_member = []
def member(name,age,power,money):
    new_member = {"name":name,
                  "age":age,
                  "power":power,
                  "money":money
                  }
    add_member.append(new_member)
while True:
        name = input("Enter Name:")
        age = int(input("Enter age:"))
        power = int(input("Enter power:"))
        if power >= 8:
            print("Hit_man")
        else:
            print("Noman")
        money = float(input("Enter money:"))
        if money >= 1000000:
            print("Sponsor")
        else:
            print("Slave")
        print("add member success")

# ทดสอบ: python -m personnel.add_member
# if __name__ == "__main__":
#     add_member("Vito", 20, 9, 500)
#     print(family_members)   # ต้องเห็น Vito ต่อท้าย และ role เป็น Hitman
