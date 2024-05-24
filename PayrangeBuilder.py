import streamlit as st
import pandas as pd
import altair as alt

# Ensure session state is initialized
def initialize_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

initialize_session_state()

# Define function to navigate to a different page
def go_to_page(page):
    st.session_state.page = page

# Define main page
def main_page():
    # Title of the web app
    st.title('Pay Range Builder')

    # Description text
    st.markdown("_Struggling with fair and competitive pay? Our Pay Range Builder tool empowers you to build data-driven pay ranges, ensuring you attract top talent, retain your best, and manage compensation with confidence._")

    # Yes/No Question Section
    st.header("What's your approach?")
    yes_no = st.radio("I will use", ('Market rates of jobs to create pay ranges', 'Pay data of existing employees to build pay ranges'))

    if yes_no == 'Market rates of jobs to create pay ranges':
        st.success('Good thought! - It is wise to align with the external market!')
    else:
        st.warning("That's wise - Internal parity ranks high most often!")

    # Continue Button
    if st.button("Let's Continue"):
        go_to_page('upload')

# Define upload page
#def upload_page():
    # File Upload Section
    # st.header('Upload Data')
    # uploaded_file = st.file_uploader("Choose a file", type=['csv'])


import base64

# Define upload page
def upload_page():
    # File Upload Section
    st.header('Upload Data')
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])

    # Provide a sample data template for reference
    sample_data_template = """
    Job,Grade,Market Rate
    Accountant,12,43000
    Payroll Assistant,11,38500
    """

    # Encode the sample data template as bytes
    sample_data_bytes = sample_data_template.encode('utf-8')
    # Base64 encode the bytes to create a downloadable link
    sample_data_b64 = base64.b64encode(sample_data_bytes).decode()

    # Create a downloadable link for the sample data template
    st.markdown("""
    Here is the [Data Template](data:text/csv;base64,{})
    """.format(sample_data_b64), unsafe_allow_html=True)

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.header('Uploaded Data')
        st.write(data)

        # Data Visualization Section
        st.header('Data Visualization')

        if st.checkbox('Show data chart'):
            # Display column selection widgets
            x_column = st.selectbox('Select X-axis data', options=data.columns, index=0)  # Default to the first column
            y_column = st.selectbox('Select Y-axis data', options=data.columns, index=1)  # Default to the second column

            # Create Altair Chart object
            chart = alt.Chart(data[[x_column, y_column]].dropna()).mark_point().encode(
                x=x_column,
                y=y_column,
                tooltip=[x_column, y_column]  # Display selected columns as tooltip
            ).properties(
                width=600,
                height=400
            )

            # Plot Altair chart
            st.altair_chart(chart, use_container_width=True)

    # Add a back button
    if st.button("Back"):
        go_to_page('main')

# Define settings page
def settings_page():
    st.header('Settings')
    st.write("This is the settings page.")

    if st.button("Back"):
        go_to_page('main')

# Define Page 3
def page_3():
    st.header('Page 3')
    st.write("This is Page 3.")

    if st.button("Back"):
        go_to_page('upload')

# Page routing
def run_app():
    if 'page' not in st.session_state:
        st.session_state.page = 'main'
    if st.session_state.page == 'main':
        main_page()
    elif st.session_state.page == 'upload':
        upload_page()
    elif st.session_state.page == 'settings':
        settings_page()
    elif st.session_state.page == 'page_3':
        page_3()
 
# Run the app
if __name__ == "__main__":
    run_app()
