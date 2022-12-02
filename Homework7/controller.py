import model
import view
import storage as st

def start():
    view.show_data('Добро пожаловать в телефонный справочник!')
    model.add_from_file('phbook.txt',st.surname, st.name, st.patr, st.tel)
    while True:
        view.show_data('Выберите действие:\n1 - Показать контакты')
        view.show_data('2 - Добавить контакты\n3 - Закрыть справочник')
        do = view.get_data('Введите цифру: ')
        if do == '1':
            view.show_data('')
            view.show_data('Выберите действие:\n1 - Показать в консоле')
            view.show_data('2 - Показать в файле phonebook.txt')
            do1 = view.get_data('Введите цифру: ')
            view.show_data('')
            view.show_data('Выберите формат:\n1 - ФИО телефон\n2 - телефон ФИО')
            do2 = view.get_data('Введите цифру: ')
            view.show_data('')
            if do2 == '1':
                data = model.generate_data(st.surname, st.name, st.patr, st.tel)
            if do2 == '2':
                data = model.generate_data(st.tel, st.surname, st.name, st.patr)
            data = model.formation_str(data)
            if do1 == '1':
                view.show_data(data)
            if do1 == '2':
                model.write_to_file('phonebook.txt','w', data)
        if do == '2':
            view.show_data('')
            view.show_data('Выберите действие:\n1 - Добавить через консоль')
            view.show_data('2 - Добавить из файла')
            do1 = view.get_data('Введите цифру: ')
            view.show_data('')
            if do1 == '1':
                view.show_data('Выберите формат:\n1 - ФИО телефон\n2 - телефон ФИО')
                do2 = view.get_data('Введите цифру: ')
                view.show_data('')
                if do2 == '2':
                    d4 = view.get_data('Введите телефон: ')
                d1 = view.get_data('Введите фамилию: ')
                d2 = view.get_data('Введите имя: ')
                d3 = view.get_data('Введите отчество: ')
                if do2 == '1':
                    d4 = view.get_data('Введите телефон: ')
                data = model.assemble_line(d1, d2, d3, d4)
                model.write_to_file('phbook.txt','a', data)
            if do1 == '2':
                file = view.get_data('Введите имя файла: ')
                data = model.read_file(file)
                model.write_to_file('phbook.txt','a', data)
        if do == '3':
            view.show_data('До скорой встречи!')
            break




    
    
    


