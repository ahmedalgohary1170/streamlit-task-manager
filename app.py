import streamlit as st
from database import create_task , all_task, get_task,update_task,delete_task
from utils import generate_id



def main():
    st.title("Task Manager ")

    myprocess=['Create','Read','Update','Delete']
    choises = st.sidebar.selectbox("Menu",myprocess)
    if choises == "Create":
        st.subheader('Creat Task')

        title = st.text_input("Title")
        description = st.text_area("Description")
        if st.button("Add Task"):
            if title and description:
                create_task(id = generate_id(), title=title ,description=description)
                st.success("Task Added Successfully")
            else:
                st.warning("please enter eny value.")



    if choises == "Read":
        st.subheader('Viow Tasks')
        for task in all_task():
            st.write(f'ID  :  {task.id}')
            st.write(f'Title  :  {task.title}')
            st.write(f'Description  :  {task.description}')
            st.write("---------------")


    if choises == "Update":
        st.subheader("Update Task")
        if id := st.number_input('Enter ID ',step=1):
            
            task = get_task(id)
            title = st.text_input('title ',value=task.title)
            description = st.text_area('Description ',value=task.description)
            if st.button("Update"):

                update_task(id=id,title=title,description=description)
                st.success("Update Task Successfully")
        else:
            st.warning('Task Is Not Found')

    if choises == "Delete":
        st.subheader('Delete Task')
        id = st.number_input('ID',step=1)
        if st.button("Delete"):
            if id:
                delete_task(id=id)
                st.success("Delete Task is Successfully")
            else:
                st.warning("Please Enter  A Valid Value")


if __name__ =='__main__':
    main()