import streamlit as st
from src import send_message,set_date
import logging
import datetime

st.title("Whatsapp")

def main():
    try:
        number = st.text_input('Insert your mobile number')
        msg = st.text_input('enter your message')
        h=st.text_input("Enter hour(use 24-hour format)")
        m=st.text_input("Enter minutes")


      
        mob_number=''
        number_status=[]
        if st.button("Submit"):
            # logging.info("Button clicked")
            if number != None and len(number)==10:
                for i in number:
                    if i.isdigit():
                        continue
                    else:
                        return st.error("enter only numeric numbers")
                
                mob_number="+91"+number

            
            

                
            else:
                st.error("wrong number")
            
        # d = st.date_input("select the date of the mesaage")
        #     # d = st.date_input("select the date of the mesaage",datetime.date(2023,3,8),on_change=True)
        # st.write('The number is ', mob_number)

        
        # st.write('Your Date is:', d)
            # st.write("your date",your_date)
            
        send_message.send_sms(mob_number,msg,h,m)
    except Exception as e:
        st.error(str(e))

main()


