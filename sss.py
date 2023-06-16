import pickle
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    try:
        with open('contacts.pickle', 'rb') as file:
            contacts = pickle.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.pickle', 'wb') as file:
        pickle.dump(contacts, file)
        
def add_n_update_contact():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    contacts = load_contacts()

    contact = {'name': name, 'phone': phone}
    contacts[id] = contact

    save_contacts(contacts)

    messagebox.showinfo('Готово', 'Ваш контакт сохранен или обновлен')

def delete_contact():
    id = id_entry.get()
    contacts = load_contacts()

    if id in contacts:
            del contacts[id]
            save_contacts(contacts)
            messagebox.showinfo('Готово', 'Контакт удален')
    else:
        messagebox.showwarning('Ошибка', 'Контакт с указанным id не найден')

def show_contacts():
    contacts = load_contacts()

    if contacts:
        contacts_text = '\n'.join([f"ID: {id}\nИмя: {contact['name']}\nНомер: {contact['phone']}\n" for id, contact in contacts.items()])
        messagebox.showinfo('Контакты', contacts_text)
    else:
        messagebox.showwarning('Ошибка', 'У вас нет контактов')

root = tk.Tk()
root.title('Адресная книга')
root.geometry("622x350")

# background_image = tk.PhotoImage("gojo.png")
# background_label = tk.Label(root, image = background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# background_label.pack()

id_label = tk.Label(root, text='ID')
id_label.pack(pady=7)
id_entry = tk.Entry(root)
id_entry.pack(pady=7)

name_label = tk.Label(root, text='Имя')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=7)

phone_label = tk.Label(root, text='Номер')
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack(pady=7)

add_button = tk.Button(root, text='Добавить/Обновить', command=add_n_update_contact)
add_button.pack(pady=10)

delete_button = tk.Button(root, text='Удалить', command=delete_contact)
delete_button.pack(pady=10)

show_button = tk.Button(root, text='Список контактов', command=show_contacts)
show_button.pack(pady=10)

root.mainloop()