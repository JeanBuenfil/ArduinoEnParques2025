import streamlit as st
from styles import styles

styles()
facebook_link = 'https://www.facebook.com/people/Arduino-en-Parques/100063786720445/'

#Sección de inicio
intro_container = st.container()
intro_container.title('Arduino en parques')
intro_container.subheader('Conoce el mundo del arduino con un fácil aprendizaje')
intro_container.link_button('Inscríbete', '')

#Elementos de la sidebar
st.sidebar.markdown(':deciduous_tree: ARDUINO EN PARQUES :deciduous_tree:')
st.sidebar.link_button('Inscríbete', '')
st.sidebar.link_button('Conócenos', facebook_link)
st.sidebar.image('logotipo.png')



#Sección "Aprendizaje"
aprendizaje_container = st.container()
aprendizaje_container.subheader('Aprendizaje')
aprendizaje_container.markdown('Adéntrate en el mundo del arduino para aprender cosas ¡INCREÍBLES!')
col1, col2, col3 = st.columns(3)
with col1:
    st.image('disenio.svg')
    st.markdown('<p class="card-title">Diseño</p>', unsafe_allow_html=True)
    st.markdown('<p class="card-text">Aprenderemos a diseñar pequeños circuitos basados en Arduino</p>', unsafe_allow_html=True)
with col2:
    st.image('programacion.svg')
    st.markdown('<p class="card-title">Programación</p>', unsafe_allow_html=True)
    st.markdown('<p class="card-text">Conceptos básicos de programación de bloques,   '
    'dirigido a prototipos en Arduino</p>', unsafe_allow_html=True)
with col3:
    st.image('imaginacion.svg')
    st.markdown('<p class="card-title">Imaginación</p>', unsafe_allow_html=True)
    st.markdown('<p class="card-text">La imaginación es el límite, crea lo que   '
    'imaginas y diviértete mientras aprendes</p>', unsafe_allow_html=True)

#Sección con información del proyecto
#Centrar secciones h4
center_alignment="""<style>
h4{
text-align: center;
}
</style>
"""
info_container = st.container()
info_container.subheader('Sobre el proyecto')
info_container.image('logo.png')
info_container.markdown('<h4>Los Mejores Maestros</h4>' + center_alignment, unsafe_allow_html=True)

info_container.markdown(':sunglasses: Un grupo especializado de alumnos de la Facultad de Matemáticas   '
'y la Facultad de Contaduria de la UADY, estaran guiandote por este fabuloso Mundo del Arduino donde   '
'tu imaginación es el limite. :sunglasses:')

info_container.markdown('<h4>¿Qué es el arduino?</h4>' + center_alignment, unsafe_allow_html=True)

info_container.markdown(':robot_face: Es una pequeña tarjeta similar a una computadora la cual nos ayudara a crear   '
'muchos diseños, prototipos y hasta robots, con el cual podras aprender los principios basicos de programación y   '
'electrónica. :robot_face:')

info_container.link_button('Visitar la página del proyecto', facebook_link)

#Sección con fotos de los cursos
cursos_container = st.container()
cursos_container.subheader('Cursos')

#Sección de contacto
contacto_container = st.container()
contacto_container.subheader('CONTACTO Y LUGAR')
contacto_container.markdown(':e-mail: Correo electrónico: arduinoenparques@gmail.com')
contacto_container.markdown(':national_park: Lugar: ')
contacto_container.button('Ayuda')


