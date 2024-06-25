import os
import requests
import streamlit as st
import weaviate
from langchain_community.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatVertexAI
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.memory import ConversationSummaryMemory
from langchain_community.prompts import ChatPromptTemplate
from langchain_community.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Weaviate
from trulens_eval import Feedback, Huggingface, Tru, TruChain
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AIzaSyCr5lA710ZoQxL4WhXYPc740Jg8wfumcmQ"
os.environ["COHERE_API_KEY"] = "3ml84htGhfTvj2TffmAB22xNpj6xN6ZLpCkiXNje"
os.environ["HUGGINGFACE_API_KEY"] = "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"

# Initialize Huggingface and Tru instances
hugs = Huggingface()
tru = Tru()