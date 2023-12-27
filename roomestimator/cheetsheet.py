import streamlit as st

def app():

    easyjet_info = [
        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Airline selection", 
        "Details": "Airline for voucher is based on the Country where the hotel is located (not where the requesting port is)", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Food & Beverage", 
        "Details": "Total cost of breakfast, plus lunch, plus dinner may not exceed £25/€25. - food and beverage claim limit of £25/customer per day", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "GIVE PRIORITY to EZY Crew", 
        "Details": "Before booking any hotel with the Easyjet Crew preference tag, please ensure you liaise with EZY Crewing and wait for their green light", 
        "Date": "08 Jul'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Late Check-Out", 
        "Details": "In case pax are asking for late check out after 13:00 please get authorization from scdo@easyJet.com", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "No Day Rooms", 
        "Details": "As per SCDO, Day rooms are not within disruption policy - Ticket #2011982", 
        "Date": "22 May'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "RATE AUTH > £/€ 500", 
        "Details": "Need authorization from scdo@easyjet.com", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "RATE AUTH < £/€ 500", "Details": "The DP Managers (Dany, Danyel/Jennifer) can authorize a rate up to £/€ 500", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "RATE AUTH (Cap + £/€ 100)", 
        "Details": "The EMEA DM can authorize a rate up to £/€ 100 over the rate cap set in AIR", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Rate Caps", 
        "Details": "All loaded in AIR against each port and will appear when making a voucher (ensure you start the voucher when a room is needed to see the cap prior to booking)", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "ROOM EXTENSIONS", 
        "Details": "Get authorization over 3 nights", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "SLA (Service Level Agreement)", 
        "Details": "1 hour, 1 min - phone, 5 mins - email acknowledgment", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Star Rating", 
        "Details": "Prefer 3* with 24/7 F&B and WiFi (3*, 4*, 2*, 5*)", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "Transport", 
        "Details": "We don't provide transportation to EZY for DP", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "All",
        "Category": "EZY Escalation Group", 
        "Details": "If the GH are not answering the email/phone call during disruption, our escalation is CDO and SCDO. Please do not call any personal number.", 
        "Date": "Data da informação"},

        {"Airline": "EZY", 
        "Country": "All", 
        "Category": "EZY HMT (Hotel Management Team)", 
        "Details": "TAC to assign rooms manually only if those directions are coming via SCDO / CDO in case of IT issues. In case of GH reaching TAC asking to provide X amount of rooms manually, TAC agents to invite GH to contact CDO team for support. No further actions. CDO will check and assist GH.", 
        "Date": "No Info"},

        {"Airline": "EZY", 
        "Country": "FNC", 
        "Category": "DO NOT BOOK - 247 Rooms in FNC", 
        "Details": "247 Rooms to be used as a last resort in FNC per Michela", "Date": "Data da informação"},
        {"Airline": "EZY", "Country": "FNC", "Category": "247 Rooms Fernando", "Details": "Room sourcing - ONLY use in FNC as LAST resort", 
        "Date": "29 Jul'21"},

        {"Airline": "EZY", 
        "Country": "GIB", 
        "Category": "Room sourcing", 
        "Details": "• Hotel Connections to check for hotel accommodation in GIB (not including Campo de Gibraltar, as this is actually in Spain) • If unsuccessful, Hotel Connections to contact Ground Handler to ask for support. Hotel Connections to finalize the transaction and pay for the rooms. • If none of the above can be achieved, then CDO’s will be informed, and will contact the customers to advise there are no rooms available, and they would need to book their own and claim back if required", 
        "Date": "07 Apr'21"},

        {"Airline": "EZY", 
        "Country": "PMI", 
        "Category": "247 Rooms Fernando", 
        "Details": "1st Option. 24 hours phone: +34 (Spain) 677605776 2nd Option. Fernando phone: +34 (Spain) 660382980 3rd Option. Xisco phone: +34 (Spain) 626533522 24 hours email is: info@247rooms.es Fernando’s email address is: Fernando.forteza@247rooms.es Steps to make a reservation: 1. Call 0034 0034 677605776 and ask for availability. 2. If you are told that they will call back in 10 minutes, please do not wait for them but anticipate and call back. They usually reply with an email listing the hotels available to book. 3. Once aware of hotel name, availability and prices please send your booking order inclusive of WEX to info@247rooms.es Do NOT call or email the hotel directly as they might not be able to assist with prices and availability The Hotels’ addresses and phone numbers are only to be used when confirming the bookings to the client. Payment: We send payment directly to Fernando only, never to the hotel. Payment process will be completed once Fernando sends us the link to pay the rooms booked, please use the same WEX(es) created for the initial booking. Commission invoices to be sent to Fernando.forteza@247rooms.es for collection.", 
        "Date": "No Info"}
    ]


        # Obtenha a lista única de companhias aéreas
    airlines = sorted(list(set(entry["Airline"] for entry in easyjet_info)))

    selected_airline = st.selectbox("Select the airline:", airlines)
        
        # Inicialize filtered_info como uma lista vazia
    filtered_info = []

    if selected_airline:
            filtered_info = [entry for entry in easyjet_info if entry["Airline"] == selected_airline]
            # Exiba as informações da EasyJet após a seleção
            st.title("Airline's Rules:")
            st.table(filtered_info)

    # Chame a função do aplicativo
    if __name__ == "__main__":
        app()
