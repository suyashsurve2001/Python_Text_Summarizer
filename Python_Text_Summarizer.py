import streamlit as st
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

st.title("Text Summarizer")
st.subheader("This App summarizes text using NLTK library")

# User input text
text = st.text_area("Enter Text Here:")

a=str(text)
c=a.split()
b=len(c)


if st.button("Summarize"):
    # Tokenize words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.casefold() not in stop_words]
    
    # Create frequency table
    freq_table = {}
    for word in words:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
    
    # Assign scores to each sentence
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq_table[word]
                else:
                    sentence_scores[sentence] = freq_table[word]
    
    # Get average score
    sum_scores = 0
    for score in sentence_scores.values():
        sum_scores += score
    avg_score = sum_scores / len(sentence_scores)
    
    # Generate summary
    summary = ""
    for sentence in sentences:
        if sentence in sentence_scores and sentence_scores[sentence] >= 1.2 * avg_score:
            summary += " " + sentence
    
    # Display summary
    st.subheader("Summary:")
    st.write(summary)
    
    X=str(summary)
    Y=X.split()
    Z=len(Y)
    
    # creating space
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    
    # Display metric
    col1, col2= st.columns(2)    
    st.markdown("""
    <style>
    div[data-testid="metric-container"] {    
    border: 3px solid rgba(00, 00, 00, 0.90);
    padding: 5% 5% 5% 10%;
    border-radius: 10px;    
    overflow-wrap: break-word;    
    }

    /* breakline for metric text         */
    div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
    overflow-wrap: break-word;
    white-space: break-spaces;        
    }
    </style>
    """
    , unsafe_allow_html=True)
    col1.metric("Befor Summary words count",b)
    col2.metric("After Summary words count",Z)
    
    
    
    

    
    
    


       


