from ast import Str
import os
import json
import getpass
import datetime
# pensar na possibilidade de acrescentar rooms

class Employee():
    def __init__(self, login, password):
        self.__login = input("login: ")
        self.__password = input("senha: ")

class Room():
    def __init__(self):
        self.capacity = None
        self.schedule_availability = []

class RoomsManagement():

    def __init__(self):
        #self.room = {"sala a": [8, 9, 10, 11], "sala b": [4, 5, 6]}
        self.people = None
        self.timeInit = None
        self.timeEnd = None
        #self.show_available()
        #self.input_user()
        

    def show_available(self):
        print("As salas reservadas são:") # checkar se há disponíveis antes de imprimir
        try:
            os.chdir("schedules")
            with open ("schedule.txt", 'r') as s:
                lines = s.readlines()
                for line in lines:
                    if line.replace(" ", "") != "":
                        line2 = json.loads(line)
                        print(line2)
                s.close()
            os.chdir("..")
        except Exception as e:
            print(e)
            #with open("rooms", 'w') as f:
                #sala_a = [8, 9, 10, 11]
                #sala_b = [4, 5, 6]
                #f.write('sala_a = ' + str(int(sala_a)) + '\n')
                #f.write('sala_b = ' + str(int(sala_b)) + '\n')
                #f.close()

        
    def new_schedule(self, date, room, time_init, time_end):
        try:
            f = open(f"schedule.txt", 'a')
            user = self.username()
            dict = [room, date, time_init, time_end, user]
            check = self.check_schedule_conflict(room, date, time_init, time_end)
            if check == False:
                print("Não é possível registrar")
                os.chdir("..")
                return False
            else:
                pass
            f.write(json.dumps(dict) + "\n")
            f.close()
            return True
        except:
            print("Could not enter directory, please try again later.")
            
    def check_schedule_conflict(self, room, date, time_init, time_end):
        try:
            print("entrou no try")
            with open ("schedule.txt", 'r') as s:
                print("abriu o ficheiro")
                lines = s.readlines()
                print("leu as linhas")
                if lines == "":
                    print("retornou True")
                    return True
                for line in lines:
                    print("nao retornou True e entrou no for")
                    if line.replace(" ", "") != "":
                        line2 = json.loads(line)
                        if line2[0] == room:
                            print("entrou no json")
                            print(line2[1])
                            print(date)
                            t_obj = datetime.strptime(line2[1], '%d/%m/%y')
                            t_obj2 = datetime.strptime(date, '%d/%m/%y')
                            if t_obj == t_obj2:
                                print("invalid Imput!")
                                return False
                            else:
                                return True
                        else:
                            pass
            return True
        except Exception as e:
            print(e)
    
    def username(self):
        try:
            a = getpass.getuser()
            return a
        except Exception as j:
            print(j)
            a = os.getlogin()
            return a
        except:
            a = input("Falha ao identificar o utilizador, por favor insira o seu username: ")
            return a

    def check_schedules_data(self, data):
        print("test")
        resp = []
        try:
            #os.chdir("Backend")
            with open ("schedule.txt", 'r') as s:
                lines = s.readlines()
                if lines == "":
                    return resp # retornar nehum registro realizado
                for line in lines:
                    #if line.replace(" ", "") != "":
                    line2 = json.loads(line)
                    if line2[1] == data:
                        resp.append(line2)
                    else:
                        pass
            #os.chdir("..")
            return resp
        except Exception as e:
            print(e)



        

        