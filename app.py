import streamlit as st
from PIL import Image

st.title('<불량 원인 파악 및 공정 최적화>')
st.header('4주차 분석 프로젝트')
st.header('최종 결과 보고서')
st.write('**Date**: 2024.10.21~10.30') 
st.write('**Team**: 오호!조') 
st.write('**Member**: 강남규 김연예진 김재희 박수빈 이재준 최지원') # 해당 내용을 수정해서 사이트를 자유롭게 꾸밀 수 있다.
# st.subheader('개요')

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3, tab4, tab5 = st.tabs(['개요' , '데이터 탐색', 'IV 분석','의사결정나무 분석','결과 및 결론'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('분석 배경')
  st.image('3.png')
  st.image('4.png')
  st.image('5.png')
with tab2:
  #tab B를 누르면 표시될 내용
  st.image('6.png')
  st.image('7.png')
  st.image('8.png')
  st.image('9.png')
  st.image('10.png')
  st.image('11.png')
  st.image('12.png')
  st.image('13.png')
  st.image('14.png')
  st.image('15.png')
  st.image('16.png')
  st.image('17.png')
  st.image('18.png')
with tab3:
  #tab B를 누르면 표시될 내용
  st.image('19.png')
  st.image('20.png')
  st.image('21.png')
  st.image('22.png')
  st.image('23.png')
  st.image('24.png')
  st.image('25.png')
with tab4:
  #tab B를 누르면 표시될 내용
  st.write('hi')
  st.image('26.png')
  st.image('27.png')
  st.image('28.png')
  st.image('29.png')
with tab5:
  #tab B를 누르면 표시될 내용
  st.image('30.png')
  st.image('31.png')
  st.image('32.png')
  st.image('33.png')
  st.image('34.png')
  st.image('35.png')

# # 데이터 프레임
# import pandas as pd
# df = pd.DataFrame({
#      '첫 번째 컬럼': [1, 2, 3, 4],
#      '두 번째 컬럼': [10, 20, 30, 40]
#      })
# st.write(df)












