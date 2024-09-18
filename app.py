import streamlit as st

st.title("Tågbiljett kalkylator")
st.header("Välkommen!")
st.subheader("Skriv in din ålder för att veta vad en biljett kostar för dig.")

if st.button("Klicka här för mer info"):
    st.info("""
    ### Prisöversikt:
    - **Barn (under 18 år):** 130 kr
    - **Vuxen (18-64 år):** 230 kr
    - **Pensionär (65+ år):** 100 kr
    """)

age_input = st.text_input("Hur gammal är du?")

# Button to calculate the ticket price
if st.button("Beräkna biljettpris"):
    if age_input:

        age = int(age_input)

        if age < 18:
            st.write(f"Du är {age} år gammal och din biljett kostar 130 kr.")
        elif 18 <= age <= 64:
            st.write(f"Du är {age} år gammal och din biljett kostar 230 kr.")
        else:
            st.write(f"Du är {age} år gammal och din biljett kostar 100 kr.")

    else:
        st.write("Var god och ange din ålder.")
