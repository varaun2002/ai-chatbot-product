import gradio as gr
import pandas as pd
import re

# Load the dataset from an Excel file
df = pd.read_excel(excel-path)

# Define the AI chatbot function
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
            response += f"{row['Product']}\n"
            response += f"Price: {row['Price']}\n"
            response += f"Description: {row['Description']}\n\n"
    else:
        response = "No products found matching your query."
    
    return response

# Create the Gradio interface
iface = gr.Interface(fn=chatbot, inputs="text", outputs="text")

# Start the interface
iface.launch(share=True)
