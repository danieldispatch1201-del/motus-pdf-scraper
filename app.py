
import streamlit as st
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
from io import BytesIO
from urllib.parse import urljoin

st.set_page_config(page_title="PDF Scraper", page_icon="📄")

st.title("📄 MOTUS PDF SCRAPER")
st.write("Find and download PDF files from websites.")

url = st.text_input("Enter Website URL")

if st.button("Find PDF Files"):
    if url:
        try:
            response = requests.get(url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            pdf_links = []

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])

                if full_url.lower().split("?")[0].endswith(".pdf"):
                    pdf_links.append(full_url)

            if pdf_links:
                st.success(f"Found {len(pdf_links)} PDF files!")

                for pdf in pdf_links:
                    st.markdown(f"[📄 Open PDF]({pdf})")
            else:
                st.warning("No PDF files found.")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a website URL.")
