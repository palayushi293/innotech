import streamlit as st # type: ignore

from streamlit_option_menu import option_menu # type: ignore # type:


import corn, crop_recommend,tomato,wheat,fertilizer

st.set_page_config(
    page_title="Agriculture"
)

class MultiApp:

    def __init__(self):
        self.apps=[]

    def add_app(self, title, function):
        self.apps.append({
            "title":title,
            "function":function
        }) 


    def run():

        with  st.sidebar: 
                

            
                app = option_menu(
                
                options=['Corn', 'Crop_Rec', 'Fertilizer', 'Tomato', 'Wheat'],  # Comma added here
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "white", "font-size": "23px"},
        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

                
            


        if app=='Tomato':
             tomato.app()

        if app=='Corn':
             corn.app()

        if app=='Crop_Rec':
             crop_recommend.app()

        if app=='Fertilizer':
             fertilizer.app()  

        if app=='Wheat':
             wheat.app()            



