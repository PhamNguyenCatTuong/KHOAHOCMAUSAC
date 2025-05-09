import streamlit as st
import numpy as np
import colour

st.set_page_config(
    page_title="Khoa học màu sắc",layout='wide'   
)

st.write('## Chuyển đổi không gian màu')

chon_khong_gian_mau = st.sidebar.radio("Chuyển đổi không gian màu", ("sRGB to XYZ", "XYZ to sRGB", "Lab to XYZ", "XYZ to Lab", "Lab to sRGB", "XYZ to CMYK", "CMYK to XYZ", "Lab to CMYK", "CMYK to Lab", "sRGB to CMYK", "CMYK to sRGB"))  
col1, col2 = st.columns(2)
if chon_khong_gian_mau == "sRGB to XYZ": #done
    with col1:
        st.write('### sRGB to XYZ')
        R = st.number_input('Nhập R:')
        G = st.number_input('Nhập G:')
        B = st.number_input('Nhập B:')
        if st.button('Chuyển sang XYZ'):
            R = R/255.0
            G = G/255.0
            B = B/255.0
            RGB = np.array([R, G, B])
            XYZ = colour.sRGB_to_XYZ(RGB)
            X = XYZ[0]*100
            Y = XYZ[1]*100
            Z = XYZ[2]*100
            s = '### X = %.2f, Y = %.2f, Z = %.2f' % (X, Y, Z)
            st.write(s)

elif chon_khong_gian_mau == "XYZ to sRGB": #done
     with col1:
        st.write('### XYZ to sRGB')
        X = st.number_input('Nhập X:')
        Y = st.number_input('Nhập Y:')
        Z = st.number_input('Nhập Z:')
        if st.button('Chuyển sang sRGB'):
            X = X/100
            Y = Y/100
            Z = Z/100
            XYZ = np.array([X, Y, Z])
            RGB = colour.XYZ_to_sRGB(XYZ)
            R = RGB[0]*255
            G = RGB[1]*255
            B = RGB[2]*255
            s = '### R = %.0f, G = %.0f, B = %.0f' % (R, G, B)
            st.write(s)

elif chon_khong_gian_mau == "Lab to XYZ": #done
     with col1:
        st.write('### Lab to XYZ')
        L = st.number_input('Nhập L:')
        a = st.number_input('Nhập a:')
        b = st.number_input('Nhập b:')
        if st.button('Chuyển sang XYZ'):
            Lab = np.array([L, a, b])
            XYZ = colour.Lab_to_XYZ(Lab)
            X = XYZ[0]*100
            Y = XYZ[1]*100
            Z = XYZ[2]*100
            s = '### X = %1f, Y = %1f, Z = %1f' % (X, Y, Z)
            st.write(s)

elif chon_khong_gian_mau == "XYZ to Lab": #done
     with col1:
        st.write('### XYZ to Lab')
        X = st.number_input('Nhập X:')
        Y = st.number_input('Nhập Y:')
        Z = st.number_input('Nhập Z:')
        if st.button('Chuyển sang Lab'):
            X = X/100
            Y = Y/100
            Z = Z/100  
            XYZ = np.array([X, Y, Z])
            Lab = colour.XYZ_to_Lab(XYZ)
            L = round(Lab[0], 2)
            a = round(Lab[1], 2)
            b = round(Lab[2], 2)
            s = '### L = %.2f, a = %.2f, b = %.2f' % (L, a, b)
            st.write(s)

elif chon_khong_gian_mau == "Lab to sRGB": #Done
    with col1:
        st.write('### Lab to sRGB')
        L = st.number_input('Nhập L:')
        a = st.number_input('Nhập a:')
        b = st.number_input('Nhập b:')
        if st.button('Chuyển sang sRGB'):
            Lab = np.array([L, a, b])
            # Chuyển Lab → XYZ → sRGB
            XYZ = colour.Lab_to_XYZ(Lab)
            RGB = colour.XYZ_to_sRGB(XYZ)
            R = RGB[0]*255
            G = RGB[1]*255
            B = RGB[2]*255
            s = '### R = %.1f, G = %.1f, B = %.1f' % (R, G, B)
            st.write(s)
elif chon_khong_gian_mau == "sRGB to Lab": #done
    with col1:
        st.write('### sRGB to Lab')
        R = st.number_input('Nhập R:')
        G = st.number_input('Nhập G:')
        B = st.number_input('Nhập B:')
        if st.button('Chuyển sang Lab'):
            R = R/255.0
            G = G/255.0
            B = B/255.0
            XYZ = colour.Lab_to_XYZ(Lab)
            RGB = colour.XYZ_to_sRGB(XYZ)
            L = round(Lab[0], 2)
            a = round(Lab[1], 2)
            b = round(Lab[2], 2)
            s = '### R = %f, G = %f, B = %f' % (L, a, b)
            st.write(s)

