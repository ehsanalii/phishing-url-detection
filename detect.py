import joblib

model = joblib.load("model.pkl")

print("Enter URL features")

length = int(input("URL length: "))
https = int(input("Has HTTPS (1 yes / 0 no): "))
at_symbol = int(input("Contains @ (1 yes / 0 no): "))
dots = int(input("Number of dots: "))

features = [[length,https,at_symbol,dots]]

result = model.predict(features)

if result[0] == 1:
    print("Legitimate Website")
else:
    print("Phishing Website Detected")
