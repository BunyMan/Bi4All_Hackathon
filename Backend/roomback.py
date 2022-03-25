from ast import Str
import os
import json
import getpass
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
        

    # def show_available(self):
    #     print("As salas reservadas são:") # checkar se há disponíveis antes de imprimir
    #     try:
    #         os.chdir("schedules")
    #         with open ("schedule.txt", 'r') as s:
    #             lines = s.readlines()
    #             for line in lines:
    #                 if line.replace(" ", "") != "":
    #                     line2 = json.loads(line)
    #                     print(line2)
    #             s.close()
    #         os.chdir("..")
    #     except Exception as e:
    #         print(e)
            #with open("rooms", 'w') as f:
                #sala_a = [8, 9, 10, 11]
                #sala_b = [4, 5, 6]
                #f.write('sala_a = ' + str(int(sala_a)) + '\n')
                #f.write('sala_b = ' + str(int(sala_b)) + '\n')
                #f.close()

    
    # def looking_for_room(self):
    #     j = 0
    #     for i in self.room.values():
    #         for n in i:
    #             if n == self.timeInit:
    #                 key = self.get_key(n)
    #                 book = input(f"A {key} está disponível para o horário {n}. Deseja reservá-la (yes/no)? ").lower()
    #                 if book == "yes":
    #                     self.book_room(key, n)
    #                     return
    #                 else:
    #                     return self.__init__
    #         print("horário indisponível")
    #         j += 1
    
    # def get_key(self, val):
    #     for key, value in self.room.items():
    #         for n in value:
    #             if n == val:
    #                 return key
    
    # def book_room(self, key, val):
    #     for key, value in self.room.items():
    #         for n in value:
    #             if n == val:
    #                 return False
    #     return True
        
    def new_schedule(self, date, room, time_init, time_end):
        try:
            #os.chdir("Backend")
            f = open(f"schedule.txt", 'a')
            user = self.username()
            dict = [room, date, time_init, time_end, user]
            check = self.check_schedual(room, date, time_init, time_end, user)
            if check == False:
                print("Não é possível registrar")
                #os.chdir("..")
                return False
            else:
                pass
            f.write(json.dumps(dict) + "\n")
            f.close()
            #os.chdir("..")
            return True
        except:
            print("Could not enter directory, please try again later.")
            
    def check_schedual(self, room, date, time_init, time_end, user):
        try:
            with open ("schedule.txt", 'r') as s:
                lines = s.readlines()
                if lines == "":
                    return True
                for line in lines:
                    if line.replace(" ", "") != "":
                        line2 = json.loads(line)
                        if line2[0] == room:
                            if line2[1] == date and (line2[2] == time_init and line2[3] == time_end) or (line2[2] < time_init and line2[3] > time_end):
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
        resp = []
        try:
            with open ("schedule.txt", 'r') as s:
                lines = s.readlines()
                if lines == "":
                    return False # retornar nehum registro realizado
                for line in lines:
                    if line.replace(" ", "") != "":
                        line2 = json.loads(line)
                        if line2[1] == data:
                            resp.append(line2)
                        else:
                            pass
            print(resp)
            return resp
        except Exception as e:
            print(e)



        

        