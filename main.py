
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
        print("加入成功~")

    def delete(self, Plant):
        try:
            itemp = int(Plant)
            Plant = itemp
        except ValueError:
            pass
        if isinstance(Plant, int):
            if Plant > self.sum:
                print("超出范围！")
                return
            Plant = self.dictNumToPlants[Plant]
        number = self.dictPlantsToNum[Plant]
        for i in range(number, self.sum):
            self.dictNumToPlants[i] = self.dictNumToPlants[i+1]
            self.dictPlantsToNum[self.dictNumToPlants[i]] = i
            self.df.loc[i-1] = self.df.loc[i]
            self.df.loc[i-1, 'number'] = self.df.loc[i-1, 'number'] - 1
        del self.dictNumToPlants[self.sum]
        del self.dictPlantsToNum[Plant]
        self.df = self.df.drop(self.sum-1)
        self.sum -= 1
        # print(self.df)
        self.safe()
        print("删除成功~")

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
        print("加入成功~")

    def delete(self, Character):
        # 检查输入是否是数字,如果是就转换到对应的Character
        try:
            itemp = int(Character)
            Character = itemp
        except ValueError:
            pass
        if isinstance(Character, int):
            if Character > self.sum:
                print("超出范围！")
                return
            Character = self.dictNumToCharacter[Character]
        # 开始删除
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
        print("删除成功~")

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

    def DeletePlant(self, Plant):
        try:
            itemp = int(Plant)
            Plant = itemp
        except ValueError:
            pass
        if Plant > self.Plants.sum or Plant <= 0:
            print("超出范围！")
            return
        Plant = self.Plants.dictNumToPlants[Plant]
        self.Plants.delete(Plant)
        self.PlantsCharacter.delete(Plant)

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
    def __init__(self, xPlantsCharacterDict, xPathToRule = './data/PlantsRuleBase.csv'):
        self.PathToRule = xPathToRule
        self.df = pd.read_csv(self.PathToRule, sep=',', header=0)
        self.Character = xPlantsCharacterDict
        self.sum = len(self.df.index)

    def show(self):
        print(self.df)
    def add(self, p, q):
        li = p.split(' & ')
        for i in li:
            try:
                self.Character.dictCharacterToNum[i]
            except KeyError:
                print("条件\'{}\'不在特征列表。请先将其加到特征列表！".format(i))
                return
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
        print("加入成功~")

    def delete(self, x):
        if x > self.sum:
            print("超出范围！")
            return
        self.df = self.df.drop(x)
        rule.sum -= 1
        print("删除成功~")

    def safe(self):
        self.df.to_csv(self.PathToRule, sep=',', index=False, header=True)

def sortByDict(li, dict):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if dict[li[i]] > dict[li[j]]:
                t = li[i]
                li[i] = li[j]
                li[j] = t

def Confirm():
    s = input("请确认, y/n\n").strip()
    if s == 'y':
        return True
    else:
        return False

def RemoveExrtaSpace(ins):
    s = ins.strip()
    n = len(s)
    anss = s[0]
    for i in range(1, n):
        if s[i-1] == ' ' and s[i] == ' ':
            continue
        else:
            anss += s[i]
    return anss

def ModeSelect():
    print("模式选择: 1.用户模式  2.管理员模式")
    ModeSelectScd = False
    while not ModeSelectScd:
        ModeSelectScd = True
        sMode = input("请输入数字: ")
        try:
            OutiMode = int(sMode.strip())
            if OutiMode < 1 or OutiMode > 2:
                ModeSelectScd = False
                print("输入有误！")
        except ValueError:
            ModeSelectScd = False
            print("输入有误！")
        if ModeSelectScd == True:
            break
    return OutiMode

def Manage(plants, character, rule, control):
    while 1:
        print("选择: 0.退出  1.增加植物  2.删除植物  3.增加特性  4.删除特性  5.增加规则  6.删除规则")
        print("进入模式后输入\'go back\'可回到该选择界面")
        ModeSelectScd = False
        iMode = 1
        while not ModeSelectScd:
            ModeSelectScd = True
            sMode = input("请输入数字: ")
            try:
                iMode = int(sMode.strip())
                if iMode < 0 or iMode > 6:
                    ModeSelectScd = False
                    print("输入有误！")
            except ValueError:
                ModeSelectScd = False
                print("输入有误！")
            if ModeSelectScd == True:
                break
    #TODO manage mode has not been done
        if iMode == 0:
            break
        elif iMode == 1:
            print("已有植物:")
            plants.show()
            s = input("请输入植物名称:\n").strip()
            if s == 'go back':
                continue
            if Confirm():
                control.AddPlants(s)
        elif iMode == 2:
            print("已有植物:")
            plants.show()
            s = input("请输入要删除的植物名称:\n").strip()
            if s == 'go back':
                continue
            if Confirm():
                control.DeletePlant(s)
        elif iMode == 3:
            print("已有特征:")
            character.show()
            s = input("请输入要加入的特征:\n").strip()
            if s == 'go back':
                continue
            if Confirm():
                control.AddCharacter(s)
        elif iMode == 4:
            print("已有特征:")
            character.show()
            s = input("请输入要删除的特征:\n").strip()
            if s == 'go back':
                continue
            if Confirm():
                control.DeleteCharacter(s)
        elif iMode == 5:
            print("已有规则:")
            rule.show()
            print("输入样例:A & B & C -> D")
            s = input("请输入: ").strip()
            if s == 'go back':
                continue
            if Confirm():
                s = s.split(' -> ')
                s[0].strip(), s[1].strip()
                rule.add(s[0], s[1])
        elif iMode == 6:
            print("已有规则:")
            rule.show()
            s = input("请输入序号: ").strip()
            if s == 'go back':
                continue
            if Confirm():
                num = int(s)
                rule.delete(num)

def InputWithNum(OutConditionList):
    inputscd = False
    while not inputscd:
        s = RemoveExrtaSpace(input('请输入: '))
        inputscd = True
        for i in s.split(' '):
            try:
                x = int(i)
                if x <= 0 or x > character.sum - plants.sum:
                    print("\'{}\'超出输入范围！".format(x))
                    inputscd = False
            except ValueError:
                print("\'{}\'并不是数字，请输入正确的整数".format(i))
                inputscd = False
        if inputscd:
            for i in s.split(' '):
                if character.dictNumToCharacter[int(i)] not in OutConditionList:
                    OutConditionList.append(character.dictNumToCharacter[int(i)])


def Inference(plants, character, rule, control):
    # 输入阶段
    print(f'''输入对应条件前面的数字:
*****************************************************************************************************''')
    control.ShowCharacter()
    print('''****************************************************************************************************
***************************************请以空格隔开输入对应数字*****************************************
    ''')
    ConditionList = []
    InputWithNum(ConditionList)

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
                print(rule.df.loc[i]['antecedent'], '->', rule.df.loc[i]['consequent'])
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



system('chcp 65001')
plants = PlantsDict()
character = PlantsCharacterDict()
rule = PlantsRuleBase(character)
control = PlantsDictControl(plants, character)

iMode = ModeSelect()

if iMode == 1:
    Inference(plants, character, rule, control)
elif iMode == 2:
    Manage(plants, character, rule, control)


