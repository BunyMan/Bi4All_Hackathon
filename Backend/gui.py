from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
from roomback import *
from tkcalendar import Calendar

root = Tk()

class gui():
    def __init__(self):
        self.room_type = None
        self.date = None
        self.time_init = None
        self.time_end = None
        self.lista = []

    def room4all(self):
        root.title("Room4All 🏠")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.resizable(0, 0)
        root.attributes("-topmost", True)
        self.e1 = RoomsManagement()
        # Label - Input
        self.led = ttk.Label(mainframe, text='Tipo de Sala: ')
        self.led1 = ttk.Label(mainframe, text="Dia: ")
        self.led2 = ttk.Label(mainframe, text="Horário de Início: ")
        self.led3 = ttk.Label(mainframe, text="Horário de Término: ")
        #led4 = ttk.Label(mainframe, text="Número do CRI: ")
        
        self.text0 = StringVar(mainframe)
        self.text0.set('Choices')
        self.rooms = ['Smart (3 pessoas)', 'Standar (6 pessoas)', 'Super (8 pessoas)', 'Ioga', 'Auditorium', 'Padel', 'Gim']
        self.ed = ttk.OptionMenu(mainframe, self.text0, *self.rooms)

        self.ed1 = ttk.Button(mainframe, text="Seleciona Aqui!", command=self.calendar_page)
        #self.date_text = self.ed1.
        #print(self.date_text)
        
        self.text2 = StringVar(mainframe)
        self.text2.set('Horas')
        self.rooms2 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00','12:30', '13:00','13:30', '14:00','14:30', '15:00','15:30', '16:00 ','16:30','17:00', '17:30', '18:00','18:30','19:00', '19:30', '20:00','20:30', '21:00'  ]
        self.ed2 = ttk.OptionMenu(mainframe, self.text2, *self.rooms2)
        
        self.text3 = StringVar(mainframe)
        self.text3.set('Horas')
        self.rooms3 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00','12:30', '13:00','13:30', '14:00','14:30', '15:00','15:30', '16:00 ','16:30','17:00', '17:30', '18:00','18:30','19:00', '19:30', '20:00','20:30', '21:00'  ] 
        self.ed3 = ttk.OptionMenu(mainframe, self.text3, *self.rooms3)
        
        self.led.grid(row=1, column=0, sticky=W)
        self.led1.grid(row=2, column=0, sticky=W)
        self.led2.grid(row=3, column=0, sticky=W)
        self.led3.grid(row=4, column=0, sticky=W)

        self.ed.grid(row=1, column=1, sticky=W, padx=5)
        self.ed1.grid(row=2, column=1, sticky=W, padx=5)
        self.ed2.grid(row=3, column=1, sticky=W, padx=5)
        self.ed3.grid(row=4, column=1, sticky=W, padx=5)

        # def exit():
        #     self.e1.show_available()
        #     #root.quit()

        self.space_start = ttk.Label(mainframe, text="")
        self.space_start.grid(row=0, column=0)

        self.space_end = ttk.Label(mainframe, text="")
        self.space_end.grid(row=5, column=0)

        self.bt = ttk.Button(mainframe, text="Fazer Reserva", command=self.room)
        self.bt.grid(row=6, column=2, pady=10)

        self.bt1 = ttk.Button(mainframe, text="Ver Reservas", command=self.see_requires)
        self.bt1.grid(row=6, column=1, pady=10)

        self.help_button = ttk.Button(mainframe, text="Ajuda", command=self.help_gui)
        self.help_button.grid(row=6, column=0, pady=10, ipadx=12)

        root.bind('<Return>', ttk.Button)

        root.mainloop()
        return self.lista
    root.quit()

    def room(self):
        self.room_type = self.text0.get()
        self.date = self.var
        self.time_init = self.text2.get()
        self.time_end = self.text3.get()
        self.lista = [self.room_type, self.date, self.time_init, self.time_end]
        check = self.e1.new_schedule(self.date, self.room_type, self.time_init, self.time_end)
        if check == False:
            self.require_denied()
            self.room4all()
        else:
            self.require_accepted()
            self.room4all()
        return self.lista

    def table_requires_date(self):
        self.tablerequiresdate = Toplevel(root)
        self.tablerequiresdate.title("" + self.data_info)
        self.tablerequiresdate_frame = ttk.Frame(self.tablerequiresdate, padding="3 3 12 12")
        self.tablerequiresdate_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.tablerequiresdate.columnconfigure(0, weight=1)
        self.tablerequiresdate.rowconfigure(0, weight=1)
        self.tablerequiresdate.resizable(0, 0)
        self.tablerequiresdate.attributes("-topmost", True)
        
        self.header1 = ttk.Label(self.tablerequiresdate, text="Sala")
        self.header1.grid(row=0, column=0, pady=10, padx=10)
        self.header1 = ttk.Label(self.tablerequiresdate, text="Hora [Start]")
        self.header1.grid(row=0, column=1, pady=10, padx=10)
        self.header1 = ttk.Label(self.tablerequiresdate, text="Hora [End]")
        self.header1.grid(row=0, column=2, pady=10, padx=10)
        self.header1 = ttk.Label(self.tablerequiresdate, text="User ID 🪪")
        self.header1.grid(row=0, column=3, pady=10, padx=10)

        j = 1
        for line in self.array_data:
            self.selectedroom = ttk.Label(self.tablerequiresdate, text=line[0])
            self.selectedroom.grid(row=j, column=0, pady=3, padx=10)
            self.hour_start = ttk.Label(self.tablerequiresdate, text=line[2])
            self.hour_start.grid(row=j, column=1, pady=3, padx=10)
            self.hour_end = ttk.Label(self.tablerequiresdate, text=line[3])
            self.hour_end.grid(row=j, column=2, pady=3, padx=10)
            self.user_id = ttk.Label(self.tablerequiresdate, text=line[4])
            self.user_id.grid(row=j, column=3, pady=3, padx=10)
            j += 1

    def see_requires(self):
        self.seerequires = Toplevel(root)
        self.seerequires.title("Selecione a Data 📆")
        self.seerequires_frame = ttk.Frame(self.seerequires, padding="3 3 12 12")
        self.seerequires_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.seerequires.columnconfigure(0, weight=1)
        self.seerequires.rowconfigure(0, weight=1)
        self.seerequires.resizable(0, 0)
        self.seerequires.attributes("-topmost", True)
        self.see_date = Calendar(self.seerequires, selectmode = 'day')
        self.see_date.grid(row=0,column=0)
        confirm_to_see = ttk.Button(self.seerequires, text="Confirmar 👍", command=self.getting_date)
        confirm_to_see.grid(row=1, column=0, pady=10)

    def getting_date(self):
        self.data_info = self.see_date.get_date()
        self.array_data = self.e1.check_schedules_data(self.data_info)
        self.table_requires_date()
        self.seerequires.destroy()

    def help_gui(self):
        self.helpmenu = Toplevel(root)
        self.helpmenu.title("Ajuda 🆘")
        self.helpmenu_frame = ttk.Frame(self.helpmenu, padding="3 3 12 12")
        self.helpmenu_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.helpmenu.columnconfigure(0, weight=1)
        self.helpmenu.rowconfigure(0, weight=1)
        self.helpmenu.resizable(0, 0)
        self.helpmenu.attributes("-topmost", True)

        self.msg_tipodesala = ttk.Label(self.helpmenu, text="  Tipo de Sala:  ")
        self.msg_tipodesala.configure(font='BOLD')
        self.msg_tipodesala.grid(row=0, column=0, pady=10, sticky=(W))
        self.msg_tipodesala_help = ttk.Label(self.helpmenu, text="Local onde é selecionada a sala do envento.")
        self.msg_tipodesala_help.grid(row=0, column=1, pady=10, sticky=(W))

        self.msg_escolherdia = ttk.Label(self.helpmenu, text="  Dia:  ")
        self.msg_escolherdia.configure(font='BOLD')
        self.msg_escolherdia.grid(row=1, column=0, pady=10, sticky=(W))
        self.msg_escolherdia_help = ttk.Label(self.helpmenu, text="Local onde é selecionado o dia do evento.")
        self.msg_escolherdia_help.grid(row=1, column=1, pady=10, sticky=(W))

        self.msg_hora_inicio = ttk.Label(self.helpmenu, text="  Hora de Ínicio:  ")
        self.msg_hora_inicio.configure(font='BOLD')
        self.msg_hora_inicio.grid(row=2, column=0, pady=10, sticky=(W))
        self.msg_hora_inicio_help = ttk.Label(self.helpmenu, text="Local onde é selecionada a hora\n inicial do evento.")
        self.msg_hora_inicio_help.grid(row=2, column=1, pady=10, sticky=(W))

        self.msg_hora_fim = ttk.Label(self.helpmenu, text="  Hora de Término:  ")
        self.msg_hora_fim.configure(font='BOLD')
        self.msg_hora_fim.grid(row=3, column=0, pady=10, sticky=(W))
        self.msg_hora_fim_help = ttk.Label(self.helpmenu, text="Local onde é selecionada a hora destinada\npara o término do evento.")
        self.msg_hora_fim_help.grid(row=3, column=1, pady=10, sticky=(W))

    def require_denied(self):
        self.requiredenied = Toplevel(root)
        self.requiredenied.title("Pedido Negado! ❌")
        self.requiredeniedframe = ttk.Frame(self.requiredenied, padding="3 3 12 12")
        self.requiredeniedframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.requiredenied.columnconfigure(0, weight=1)
        self.requiredenied.rowconfigure(0, weight=1)
        self.requiredenied.attributes("-topmost", True)
        self.require_denied_msg = ttk.Label(self.requiredenied, text="Horário indisponível para a reserva! ")
        self.require_denied_msg.grid(row=0, column=0, pady=10, padx=5)
        self.require_denied_tryagain = ttk.Label(self.requiredenied, text="Consulte: Ver Reservas ")
        self.require_denied_tryagain.grid(row=2, column=0, pady=10, padx=10)
        self.requiredenied.resizable(0, 0)
        
    def require_accepted(self):
        self.requireaccepted = Toplevel(root)
        self.requireaccepted.title("Marcação Aceite! ✅")
        self.requireacceptframe = ttk.Frame(self.requireaccepted, padding="3 3 12 12")
        self.requireacceptframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.requireaccepted.columnconfigure(0, weight=1)
        self.requireaccepted.rowconfigure(0, weight=1)
        self.requireaccepted.resizable(0, 0)
        self.requireaccepted.attributes("-topmost", True)
        self.require_accepted_msg = ttk.Label(self.requireaccepted, text="Pedido Aceite!")
        #self.require_accepted_msg.grid(row=0, column=0, pady=10, sticky=(W, E))

        self.require_accepted_room = ttk.Label(self.requireaccepted, text="Sala:", font=(20))
        self.require_accepted_room.grid(row=1, column=0, padx=10, sticky=(W))
        self.require_accepted_room_info = ttk.Label(self.requireaccepted, text="" + self.room_type, font=(20))
        self.require_accepted_room_info.grid(row=1, column=1, padx=5, sticky=(W))

        self.require_accepted_date = ttk.Label(self.requireaccepted, text="Data:", font=(20))
        self.require_accepted_date.grid(row=2, column=0, padx=10, sticky=(W))
        self.require_accepted_date_info = ttk.Label(self.requireaccepted, text="" + self.date, font=(20))
        self.require_accepted_date_info.grid(row=2, column=1, padx=5, sticky=(W))

        self.require_accepted_starth = ttk.Label(self.requireaccepted, text="Hora [Início]:", font=(20))
        self.require_accepted_starth.grid(row=3, column=0, padx=10, sticky=(W))
        self.require_accepted_starth_info = ttk.Label(self.requireaccepted, text="" + self.time_init, font=(20))
        self.require_accepted_starth_info.grid(row=3, column=1, padx=5, sticky=(W))

        self.require_accepted_endh = ttk.Label(self.requireaccepted, text="Hora [Fim]:", font=(20))
        self.require_accepted_endh.grid(row=4, column=0, padx=10, sticky=(W))
        self.require_accepted_endh_info = ttk.Label(self.requireaccepted, text="" + self.time_end, font=(20))
        self.require_accepted_endh_info.grid(row=4, column=1, padx=5, sticky=(W))

        self.confirm_button = ttk.Button(self.requireaccepted, text="Confirmar 👍", command=self.close_confirm)
        self.confirm_button.grid(row=5, column=1, pady=10)
        self.cancel_button = ttk.Button(self.requireaccepted, text="Cancelar 👎", command=self.close_confirm)
        self.cancel_button.grid(row=5, column=0, pady=10)
    
    def close_confirm(self):
            self.requireaccepted.destroy()


    def calendar_page(self):
        self.calendarpage = Toplevel(root)
        self.calendarpage.title("Calendar")
        self.calframe = ttk.Frame(self.calendarpage, padding="3 3 12 12")
        self.calframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.calendarpage.columnconfigure(0, weight=1)
        self.calendarpage.rowconfigure(0, weight=1)
        self.calendarpage.resizable(0, 0)
        self.calendarpage.attributes("-topmost", True)
        self.cal = Calendar(self.calendarpage, selectmode = 'day')
        self.cal.grid(row=0,column=0)
        confirm_date = ttk.Button(self.calendarpage, text="Confirmar 👍", command=self.grad_date)
        confirm_date.grid(row=1, column=0, pady=10)
    
    def grad_date(self):
        self.ed1.config(text = self.cal.get_date())
        self.var = self.cal.get_date()
        self.calendarpage.destroy()
