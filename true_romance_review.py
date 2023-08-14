import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

# Send a GET request to the web page
url = "https://www.empireonline.com/movies/reviews/true-romance-review/"
response = requests.get(url)

# Extract the HTML content
html_content = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the text from the HTML elements
text = soup.get_text()

# Remove punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

cleaned_text = remove_punctuation(text)

# Tokenize the text
tokens = word_tokenize(cleaned_text)

# Remove stopwords
stopwords = set(stopwords.words('english'))
filtered_tokens = [token.lower() for token in tokens if token.lower() not in stopwords]

#print(cleaned_text)

# Calculate the frequency distribution
freq_dist = FreqDist(cleaned_text)

# Print the most common words
print("Most Common Words:")
for word, frequency in freq_dist.most_common(10):
   print(f"{word}: {frequency}")
