import streamlit as st

def app():
    st.title("Welcome to TAC Assistant")
    st.subheader("Choose one of the options in the menu.")
    st.write("If you have any issue you want to report fill up the form below:")

    name = st.text_input("Your Name")
    ticket_number = st.number_input("Ticket Number", step=1)
    airline = st.selectbox("Airline", ("EZY", "WizzAir", "BA", "AA", "EY", "EK", "VY", "Other"))
    date_issue = st.date_input("Date of the Issue")
    time_issue = st.time_input("Time of the Issue in UTC")
    text_input = st.text_area("Additional Comment", "")

    # Submit Button
    if st.button("Submit"):
        st.write(f"Name: {name}")
        st.write(f"Ticket Number: {int(ticket_number)}")  # Convert to integer for display
        st.write(f"Airline: {airline}")
        st.write(f"Date of the Issue: {date_issue}")
        st.write(f"Time of the Issue in UTC: {time_issue}")
        st.write(f"Describe here what happened: {text_input}")

# Call the app function
if __name__ == "__main__":
    app()
