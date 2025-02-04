class NaiveBayes:
    def __init__(self):
        self.spam_words = {}
        self.ham_words = {}
        self.spam_count = 0
        self.ham_count = 0
        self.total_spam = 0
        self.total_ham = 0
        
    def train(self, data):
        for text, label in data:
            words = text.lower().split()
            if label == "spam":
                self.spam_count += 1
                self.total_spam += len(words)
                for word in words:
                    self.spam_words[word] = self.spam_words.get(word, 0) + 1
            else:
                self.ham_count += 1
                self.total_ham += len(words)
                for word in words:
                    self.ham_words[word] = self.ham_words.get(word, 0) + 1
        
    def predict(self, text):
        words = text.lower().split()
        spam_prob = self.spam_count / (self.spam_count + self.ham_count)
        ham_prob = self.ham_count / (self.spam_count + self.ham_count)
        
        for word in words:
            spam_prob *= (self.spam_words.get(word, 0) + 1) / (self.total_spam + len(self.spam_words))
            ham_prob *= (self.ham_words.get(word, 0) + 1) / (self.total_ham + len(self.ham_words))
        
        return "spam" if spam_prob > ham_prob else "ham"

# Sample training data (text, label)
data = [
    ("Win a free lottery now", "spam"),
    ("Urgent! Claim your prize money", "spam"),
    ("Hello, how are you today?", "ham"),
    ("Let's have a meeting tomorrow", "ham"),
]

nb = NaiveBayes()
nb.train(data)

# Test the model
test_text = "Claim your free prize"
print(f"'{test_text}' is classified as: {nb.predict(test_text)}")
