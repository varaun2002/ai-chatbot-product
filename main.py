import streamlit as st
import re
import pandas as pd

def process_text(input_text):
    return len(input_text)\

df=pd.read_excel("../AIChatbotProduct/pricelist.xlsx")    

def chatbot(product_query):
    # Filter the dataset based on the user query
    if not re.search('[a-zA-Z0-9]', product_query):
        return "Please provide a valid query."
    
    results = df[df["Product"].str.contains(product_query, case=False) |
                 df["Price"].astype(str).str.contains(product_query, case=False) |
                 df["Description"].str.contains(product_query, case=False)]
    
    if len(results) > 0:
        # Generate a response based on the product information
        response = f"We found {len(results)} products matching your query:\n\n"
        for idx, row in results.iterrows():
            response += f"{row['Product']}\n\n"
            response += f"Price: {row['Price']}\n\n"
            response += f"Description: {row['Description']}\n\n"
    else:
        response = "No products found matching your query."
    
    return response


def main():
    st.title("Text Processing App")
    
    # Text input
    input_text = st.text_input("Enter text")
    
    # Submit button
    if st.button("Submit"):
        # Call the process_text function
        result = chatbot(input_text)


        # Display the result
        st.write("result: ", result)

    st.dataframe(df)

if __name__ == "__main__":
    main()
