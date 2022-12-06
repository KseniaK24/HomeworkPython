import model
import view
import storage as st

def start():
    view.show_data('Справочник сотрудников компании ООО "К"!')
    model.add_from_file('list_jobs.txt', st.number, st.surname, st.name, st.patr, st.tel, st.job)
    model.formation_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
    while True:
        view.show_data('Выберите действие:\n1 - Показать список сотрудников')
        view.show_data('2 - Выгрузить список сотрудников\n3 - Найти сотрудника' )
        view.show_data('4 - Добавить сотрудника\n5 - Изменить данные сотрудника' )
        view.show_data('6 - Удалить сотрудника\n7 - Выход' )
        do = view.get_data('Введите цифру: ')
        view.show_data('')
        if do == '1':
            view.show_data('Выберите формат:\n1 - № табельный, ФИО, телефон, должность')
            view.show_data('2 - должность, № табельный, ФИО, телефон')
            while True:
                do1 = view.get_data('Введите цифру: ')
                view.show_data('')
                if do1 == '1':
                    data1 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
                    data1 = model.formation_str(data1)
                    view.show_data(data1)
                    break
                if do1 == '2':
                    data1 = model.generate_data(st.job,st.number,st.surname,st.name,st.patr,st.tel)
                    data1 = model.formation_str(data1)
                    view.show_data(data1)
                    break
                view.show_data('Неверный ввод. Введите цифру 1 или 2')
        if do == '2':
            file = view.get_data('Введите имя файла: ')
            data2 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
            data2 = model.formation_str(data2)
            model.write_to_file(file,'w', data2)
        if do == '3':
            find_data = view.get_data('Введите параметр поиска: ')
            indx_data = model.find_data(find_data,st.number,st.surname,st.name,st.patr,st.tel,st.job)
            if indx_data == []:
                view.show_data('Сотрудник не найден')
            data3 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
            found_data = model.select_data(indx_data, data3)
            found_data = model.formation_str(found_data)   
            view.show_data(found_data)
        if do == '4':
            d1 = view.get_data('Введите фамилию: ')
            d2 = view.get_data('Введите имя: ')
            d3 = view.get_data('Введите отчество: ')
            d4 = view.get_data('Введите табельный номер: ')
            d5 = view.get_data('Введите должность: ')
            d6 = view.get_data('Введите телефон: ')
            data_add = model.assemble_line(d4, d1, d2, d3, d6, d5)
            model.write_to_file('list_jobs.txt','a', data_add)
            st.number = model.reset_data(st.number)
            st.name = model.reset_data(st.name)
            st.surname = model.reset_data(st.surname)
            st.patr = model.reset_data(st.patr)
            st.tel = model.reset_data(st.tel)
            st.job = model.reset_data(st.job)
            model.add_from_file('list_jobs.txt', st.number, st.surname, st.name, st.patr, st.tel, st.job)
            model.formation_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
        if do == "5":
            find_data = view.get_data('Введите ФИО сотрудника: ')
            indx_data = model.find_data(find_data,st.number,st.surname,st.name,st.patr,st.tel,st.job)
            if indx_data != []:
                data4 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
                found_data = model.select_data(indx_data, data4)
                found_data = model.formation_str(found_data)
                view.show_data(found_data)
                view.show_data('Выберите данные, которые хотите изменить')
                view.show_data('1 - Табельный номер\n2 - Фамилию\n3 - Имя\n4 - Отчество')
                view.show_data('5 - Телефон\n6 - Должность')
                while True:
                    do1 = view.get_data('Введите цифру: ')
                    if do1 == '1'or do1 =='2' or do1 == '3' or do1 =='4' or do1 =='5' or do1 == '6':
                        new_data = view.get_data('Введите новые данные: ')
                        if do1 == '1':
                            st.number = model.change_data(indx_data,new_data,st.number)
                        if do1 == '2':
                            st.surname = model.change_data(indx_data,new_data,st.surname)
                        if do1 == '3':
                            st.name = model.change_data(indx_data,new_data,st.name)
                        if do1 == '4':
                            st.patr = model.change_data(indx_data,new_data,st.patr)
                        if do1 == '5':
                            st.tel = model.change_data(indx_data,new_data,st.tel)
                        if do1 == '6':
                            st.job = model.change_data(indx_data,new_data,st.job)
                        data5 = model.formation_data(st.number,st.surname,st.name,st.patr,st.tel,st.job)
                        data5 = model.generate_data(st.number,st.surname,st.name,st.patr,st.tel,st.job)
                        data5 = model.formation_str(data5)
                        model.write_to_file('list_jobs.txt','w', data5)
                        break
                    view.show_data('Неверный ввод. введите цифру от 1 до 6')
            else:
                view.show_data('Сотрудник не найден\n')
        if do == '6':
            find_data = view.get_data('Введите ФИО сотрудника: ')
            indx_data = model.find_data(find_data,st.number,st.surname,st.name,st.patr,st.tel,st.job)
            if indx_data != []:
                data6 = model.generate_data(st.number,st.surname,st.name,st.patr,st.tel,st.job)
                found_data = model.select_data(indx_data, data6)
                found_data = model.formation_str(found_data)
                view.show_data(found_data)
                view.show_data('Удалить сотрудника?\n1 - да\n2 - нет')
                do1 = view.get_data('Введите цифру: ')
                if do1 == '1':
                    data6 = model.delete_data(indx_data, data6)
                    data6 = model.formation_str(data6)
                    model.write_to_file('list_jobs.txt','w', data6)
                    st.number = model.reset_data(st.number)
                    st.name = model.reset_data(st.name)
                    st.surname = model.reset_data(st.surname)
                    st.patr = model.reset_data(st.patr)
                    st.tel = model.reset_data(st.tel)
                    st.job = model.reset_data(st.job)
                    model.add_from_file('list_jobs.txt', st.number, st.surname, st.name, st.patr, st.tel, st.job)
                    model.formation_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
            else: view.show_data('Сотрудник не найден')
        if do == '7':
            break
        
            




    
    
    


