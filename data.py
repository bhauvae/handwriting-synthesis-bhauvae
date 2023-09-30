valid_char = ['9', 'o', 'F', 'D', '6', ',', 'h', 'b', '-', 'g', 'V', '\x00', '"', 'U', 'E', 'p', 'q', 'j', 'Y', 'M', 'k', 'x', 'u', '.', 'a', 'y', 'W', 'H', 'I', '#', 'r', '1', "'", 'S', 'e', '4', 'v', 't', ')', '!', 'w', '0', 'N', 'O', 'R', 'f', ':', 'i', 'P', 'T', ';', 'A', 'n', 'L', 'B', 'z', 'm', ' ', '?', '2', '7', '8', '5', 's', 'C', '3', 'd', 'G', 'J', '(', 'K', 'l', 'c']

text = '''The problem of electronic waste is still increasing, despite efforts from various companies. According to the United Nations, the world produced 53.6 million metric tons of e-waste in 2019, and this amount is projected to increase to 74 million metric tons by 2030. Framework Laptop is a new player in the market that introduced its first product, the Framework Laptop, in 2021. The company differentiates itself from major laptop manufacturers by focusing on creating laptops that are modular, customizable, and  repairable.  Framework  Laptop  prioritizes  creating  a  personalized  and  transparent  customer experience by offering several features that allow customers to customize their laptops based on their specific needs and preferences. Additionally, the company has a transparent pricing model that shows the  cost  of  each  component,  allowing  customers  to  select  components  that  suit  their  budget. Framework Laptop's brand loyalty is due to its unique value proposition, which offers a sustainable and long-lasting alternative to traditional laptops. Its customizable and repairable laptop is designed to decrease electronic waste. Framework Laptop's dedication to open-source hardware and software has built a community of customers and supporters who share the company's values.'''


text.replace('\n', '').replace('\r', '').replace('\t', '')
text.split('\n')
invalid_characters = []
for char in text:
    if char not in valid_char:
        invalid_characters.append(char)
print(invalid_characters)

count = 0
wrapped_text = []
while text:
    i = 1

    while len(text[:i]) < 50 and i < len(text):
        i += 1

    if i < len(text):
        i = text.rfind(" ", 0, i) + 1

    wrapped_text.append(text[:i])
    text = text[i:]



    


