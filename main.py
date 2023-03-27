
import pandas as pd
from os import system



class PlantsDict:
    def __init__(self, path='./data/Plants.csv'):
        self.PathToPlants = path
        self.df = pd.read_csv(self.PathToPlants, sep=',', header=0)
        self.dictNumToPlants = dict(zip(self.df['number'], self.df['plants']))
        self.dictPlantsToNum = dict(zip(self.df['plants'], self.df['number']))
        self.sum = len(self.dictNumToPlants)
        # # self.OutPutPathForPlants = './data/plants2.csv'
        # number from 1 to self.sum

    def safe(self):
        self.df.to_csv(self.PathToPlants, sep=',', index=False, header=True)

    def add(self, newPlant):
        for y in self.dictPlantsToNum:
            if y == newPlant:
                print("这个植物已经存在了")
                print("{}:{}".format(self.dictPlantsToNum[y], y))
                return
        self.sum += 1
        self.dictNumToPlants[self.sum] = newPlant
        self.dictPlantsToNum[newPlant] = self.sum
        self.df.loc[len(self.df.index)] = [self.sum, newPlant]
        # print(self.df)
        self.safe()

    def delete(self, plant):
        if isinstance(plant, int):
            plant = self.dictNumToPlants[plant]
        number = self.dictPlantsToNum[plant]
        for i in range(number, self.sum):
            self.dictNumToPlants[i] = self.dictNumToPlants[i+1]
            self.dictPlantsToNum[self.dictNumToPlants[i]] = i
            self.df.loc[i-1] = self.df.loc[i]
            self.df.loc[i-1, 'number'] = self.df.loc[i-1, 'number'] - 1
        del self.dictNumToPlants[self.sum]
        del self.dictPlantsToNum[plant]
        self.df = self.df.drop(self.sum-1)
        self.sum -= 1
        # print(self.df)
        self.safe()

    def show(self):
        for i in range(1, self.sum+1):
            s = str(i) + '.' + str(self.dictNumToPlants[i])
            print("{:<13}".format(s), end='')
            if i % 7 == 0: print()
        print()


class PlantsCharacterDict:
    def __init__(self, path='./data/PlantsCharacter.csv'):
        self.PathToCharacter = path
        self.df = pd.read_csv(self.PathToCharacter, sep=',', header=0)
        self.dictNumToCharacter = dict(zip(self.df['number'], self.df['character']))
        self.dictCharacterToNum = dict(zip(self.df['character'], self.df['number']))
        self.sum = len(self.dictNumToCharacter)
        # # self.OutPutPathForPlants = './data/plants2.csv'
        # number from 1 to self.sum

    def safe(self):
        self.df.to_csv(self.PathToCharacter, sep=',', index=False, header=True)

    def add(self, newCharacter):
        for y in self.dictCharacterToNum:
            if y == newCharacter:
                print("这个特征已经存在了")
                print("{}:{}".format(self.dictCharacterToNum[y], y))
                return
        self.sum += 1
        self.dictNumToCharacter[self.sum] = newCharacter
        self.dictCharacterToNum[newCharacter] = self.sum
        self.df.loc[len(self.df.index)] = [self.sum, newCharacter]
        # print(self.df)
        self.safe()

    def delete(self, Character):
        if isinstance(Character, int):
            Character = self.dictNumToCharacter[Character]
        number = self.dictCharacterToNum[Character]
        for i in range(number, self.sum):
            self.dictNumToCharacter[i] = self.dictNumToCharacter[i+1]
            self.dictCharacterToNum[self.dictNumToCharacter[i]] = i
            self.df.loc[i-1] = self.df.loc[i]
            self.df.loc[i-1, 'number'] = self.df.loc[i-1, 'number'] - 1
        del self.dictNumToCharacter[self.sum]
        del self.dictCharacterToNum[Character]
        self.df = self.df.drop(self.sum-1)
        self.sum -= 1
        # print(self.df)
        self.safe()

    def show(self):
        for i in range(1, self.sum+1):
            s = str(i) + '.' + str(self.dictNumToCharacter[i])
            print("{:<13}".format(s), end='')
            if i % 7 == 0: print()

        print()


class PlantsDictControl:
    def __init__(self, xPlants, xPlantsCharacter):
        self.Plants = xPlants
        self.PlantsCharacter = xPlantsCharacter

    def AddPlants(self, newPlants):
        self.Plants.add(newPlants)
        self.PlantsCharacter.add(newPlants)

    def AddCharacter(self, newcharacter):
        self.PlantsCharacter.add(newcharacter)

    def DeletePlants(self, plants):
        self.Plants.delete(plants)
        self.PlantsCharacter.delete(plants)

    def DeleteCharacter(self, character):
        self.PlantsCharacter.delete(character)

    def ShowCharacter(self):
        cnt = 0
        for i in range(1, self.PlantsCharacter.sum + 1):
            if self.PlantsCharacter.dictNumToCharacter[i] in self.Plants.dictPlantsToNum:
                continue
            cnt += 1
            s = str(i) + '.' + str(self.PlantsCharacter.dictNumToCharacter[i])
            print("{:<13}".format(s), end='')
            if cnt % 7 == 0:
                print()
        print()

class PlantsRuleBase:
    def __init__(self, xPlantsCharacterDict):
        self.PathToRule = './data/PlantsRuleBase.csv'
        self.df = pd.read_csv(self.PathToRule, sep=',', header=0)
        self.Character = xPlantsCharacterDict
        self.sum = len(self.df.index)

    def add(self, p, q):
        li = p.split(' & ')
        for i in range(len(li)-1):
            for j in range(i+1, len(li)):
                if self.Character.dictCharacterToNum[li[i]] > self.Character.dictCharacterToNum[li[j]]:
                    t = li[i]
                    li[i] = li[j]
                    li[j] = t
        pp = str(li[0])
        for i in range(1, len(li)):
            pp += ' & ' + str(li[i])
        self.df.loc[len(self.df.index)] = [pp, q]
        self.safe()
        self.sum += 1

    def delete(self, x):
        self.df = self.df.drop(x)
        rule.sum -= 1

    def safe(self):
        self.df.to_csv(self.PathToRule, sep=',', index=False, header=True)

def sortByDict(li, dict):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if dict[li[i]] > dict[li[j]]:
                t = li[i]
                li[i] = li[j]
                li[j] = t


system('chcp 65001')
plants = PlantsDict()
character = PlantsCharacterDict()
rule = PlantsRuleBase(character)
control = PlantsDictControl(plants, character)

# 输入阶段
print(f'''输入对应条件前面的数字:
*****************************************************************************************************''')
control.ShowCharacter()
print('''****************************************************************************************************
***************************************当输入数字0时!程序结束*****************************************
''')
ConditionList = []
while 1:
    try:
        inputNum = int(input("请输入: "))
    except ValueError:
        print("请输入正确的整数")
        continue
    if inputNum == 0:
        break
    if inputNum <= 0 or inputNum > character.sum - plants.sum:
        print("输入超出范围！")
        continue
    ConditionList.append(character.dictNumToCharacter[inputNum])


print('\n')
print("前提条件为: ")
for i in range(len(ConditionList)):
    print("{}:".format(i+1), end='')
    print(ConditionList[i], end=' ')
print('\n')

# 按字典排序
sortByDict(ConditionList, character.dictCharacterToNum)

# 推理过程
print("推理过程如下")

flag = False
# 刷sum遍
for o in range(rule.sum):
    # 对照每一条规则
    for i in range(rule.sum):
        # 在条件队列中就不用推
        if rule.df.loc[i]['consequent'] in ConditionList:
            continue
        li = rule.df.loc[i]['antecedent'].split(" & ")
        ii = 0
        jj = 0
        while ii < len(ConditionList) and jj < len(li):
            if li[jj] == ConditionList[ii]:
                jj += 1
            ii += 1
        if jj == len(li):
            ConditionList.append(rule.df.loc[i]['consequent'])
            print(rule.df.loc[i]['antecedent'], ' -> ', rule.df.loc[i]['consequent'])
            if rule.df.loc[i]['consequent'] in plants.dictPlantsToNum:
                # 结束推理！
                print("所识别的植物为{}".format(rule.df.loc[i]['consequent']))
                flag = True
                break
            for tt in range(len(ConditionList)-1, 0, -1):
                if character.dictCharacterToNum[ConditionList[tt]] < character.dictCharacterToNum[ConditionList[tt-1]]:
                    t = ConditionList[tt]
                    ConditionList[tt] = ConditionList[tt-1]
                    ConditionList[tt-1] = t
    if flag:
        break
if not flag:
    print("抱歉，并没能推理出对应的生物")
