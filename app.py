import streamlit as st,pandas as pd
from predictor import predict_wait
st.set_page_config(page_title='QueueLess AI',page_icon='🚦',layout='wide')
st.title('🚦 QueueLess AI');st.subheader('Intelligent waiting-time prediction & queue optimization')
st.info('Prototype uses synthetic training data. Real deployment requires real queue observations.')
defaults=[('Counter A',8,2.8),('Counter B',10,1.5),('Counter C',5,4.5)]
rows=[]; cols=st.columns(3)
for i,(name,dp,ds) in enumerate(defaults):
    with cols[i]:
        st.markdown('### '+name)
        people=st.number_input('People in queue',0,100,dp,key=f'p{i}')
        service=st.number_input('Average service time (min)',.1,20.,float(ds),step=.1,key=f's{i}')
        hour=st.slider('Hour of day',0,23,13,key=f'h{i}')
        arrival=st.number_input('Arrival rate / min',0.,10.,1.,step=.1,key=f'a{i}')
        eff=st.number_input('Counter efficiency',.5,1.5,1.,step=.01,key=f'e{i}')
        rows.append({'Counter':name,'People':people,'Predicted wait (min)':round(predict_wait(people,service,hour,1,arrival,eff),1)})
r=pd.DataFrame(rows).sort_values('Predicted wait (min)');best=r.iloc[0]
st.success(f"🚀 Recommended: {best['Counter']} — predicted wait {best['Predicted wait (min)']} minutes")
st.dataframe(r,use_container_width=True,hide_index=True)
