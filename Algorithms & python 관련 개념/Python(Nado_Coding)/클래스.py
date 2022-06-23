# __init__(생성자)  : 객체(class로부터 만들어지는 것들)가 생성될 때 자동으로 호출되는 부분

# 일반 유닛
class Unit :
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)


# 레이스 : 공중유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 =  Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
# python에서는 외부에서 추가로 객체의 변수를 만들어 쓸 수 았음 
wraith2.clocking = True   

if wraith2.clocking == True :
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")




# -----------------------------------------------------------

# 공격 유닛
class AttackUnit :
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location) :
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage) :
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0 :
            print(f"{self.name} : 파괴되었습니다.")

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)