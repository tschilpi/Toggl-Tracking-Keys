# **Global Hotkeys for Toggl**

This application allows users to set global hotkeys for the Toggl time tracking service, making it easy to start and stop projects using custom key combinations.
The app can be executed by running Code\run_program.py. It will run via localhost.

**Application structure:**
1.     streamlit.py is responsible for managing the main application logic, rendering the user interface, and handling user interactions using Streamlit.
2.     record_hotkeys.py takes care of recording hotkeys, processing them, and returning both virtual key values and key names.
3.     check_hotkeys.py continuously monitors the recorded hotkeys and, upon detecting a keypress, triggers the corresponding API calls.
4.     main_test.py manages the API logic, ensuring seamless communication with the external service.


Streamlit Functions:
1. initialize_session_state(): Initializes Streamlit session state with default values for various application settings.
2. get_project_lists(): Retrieves project lists, IDs, and a mapping between IDs and project names.
3. main(): Main application function that displays the user interface and handles user interactions.
4. record_hotkey(index): Records a hotkey for a given index and updates the session state with the new hotkey value.
5. display_record_hotkey_buttons(): Displays hotkey record buttons for each hotkey slot.
6. change_state(): Handles activation and deactivation of hotkeys.

Structure of the main file:
1. Initialize session state and connect to Toggl API (if not already connected).
2. Define main application function that handles user interactions and displays the interface.
3. Display hotkey record buttons and project selection dropdowns.
4. Handle edge cases for hotkey and project selection.
5. Provide a button to activate/deactivate hotkeys and control their state.

Authentication Flow:
1. Prompt the user to enter the name of the environment variable containing their Toggl API key.
2. Upon successful authentication, start the main application and display the interface.