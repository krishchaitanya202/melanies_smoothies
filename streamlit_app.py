# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'choose upto 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
     )

if ingredients_list:
   ingredients_string = ''
    
for fruit_chosen in ingredients_list:
    ingredients_string += fruit_chosen + ' '
    
#st.write(ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

#st.write(my_insert_stmt)
#st.stop()
time_to_insert = st.button('Submit Order')
    
   
    
