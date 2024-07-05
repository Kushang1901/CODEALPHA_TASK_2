import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Define FAQs and responses
faqs = {
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email after purchase.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and Apple Pay
