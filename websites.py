
class Websites():
    
    websites = []
    
    def add_website(website, websites):
        if website not in websites:
            websites.append(website)
        
    def remove_website(website, websites):
        websites.remove(website)