import model
import storage as st

text = None

async def start(update, context):
    await update.message.reply_text(f'{update.effective_user.first_name},'' добро пожаловать в справочник сотрудников компании ООО "К"!')
    await update.message.reply_text('Выберите действие:\n/1 - Показать список сотрудников\n/2 - Найти сотрудника\n/3 - Добавить сотрудника')

async def command_1 (update, context):
    model.add_from_file('list_jobs.txt', st.number, st.surname, st.name, st.patr, st.tel, st.job)
    data1 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
    data1 = model.formation_str(data1)
    st.number = model.reset_data(st.number)
    st.name = model.reset_data(st.name)
    st.surname = model.reset_data(st.surname)
    st.patr = model.reset_data(st.patr)
    st.tel = model.reset_data(st.tel)
    st.job = model.reset_data(st.job)
    await update.message.reply_text(data1)

async def command_2 (update, context):
    await update.message.reply_text('Отправьте параметр поиска, затем отправьте /find')
    
async def command_3 (update, context):
    await update.message.reply_text('Отправьте данные сотрудника через пробел: табельный номер, фамилию, имя, отчество, телефон, должность, затем отправьте /add')

async def msg (update, context):
    global text
    text = update.message.text

async def find (update, context):
    model.add_from_file('list_jobs.txt', st.number, st.surname, st.name, st.patr, st.tel, st.job)
    find_data = text
    indx_data = model.find_data(find_data,st.number,st.surname,st.name,st.patr,st.tel,st.job)
    if indx_data == []:
        await update.message.reply_text('Сотрудник не найден')
    data3 = model.generate_data(st.number, st.surname, st.name, st.patr, st.tel, st.job)
    found_data = model.select_data(indx_data, data3)
    found_data = model.formation_str(found_data) 
    st.number = model.reset_data(st.number)
    st.name = model.reset_data(st.name)
    st.surname = model.reset_data(st.surname)
    st.patr = model.reset_data(st.patr)
    st.tel = model.reset_data(st.tel)
    st.job = model.reset_data(st.job)
    await update.message.reply_text(found_data)

async def add (update, context):
    data_add = text
    model.write_to_file('list_jobs.txt','a', data_add)
    await update.message.reply_text('Сотрудник добавлен')

