# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1/"
    while url:
        response = requests.get(f"{base_url}{url}")
        print(f"Scraping {base_url}{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text" : quote.find(class_="text").get_text(),
                "author" : quote.find(class_="author").get_text(),
                "bio-link" : quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(2)
    return all_quotes

def start_game(all_quotes):
    quote = choice(all_quotes)
    remaining_guesses = 4
    guess = ""

    print(f"Here's a quote : {quote['text']}")
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining : {remaining_guesses}\n")
        
        if guess.lower() == quote["author"].lower():
            break

        remaining_guesses -= 1
        if remaining_guesses == 3:
            response = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born {birth_place} on {birth_date}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's name starts with letter {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_name_initials = quote['author'].split(" ")[-1][0]
            print(f"Here's a hint: The author's last name starts with letter {last_name_initials}")
        else:
            print(f"Sorry... You ran out of guesses... The answer was {quote['author']}")
            
    choice_variable = ""
    while choice_variable.lower() not in ('yes', 'y', 'no', 'n'):
        choice_variable = input("Would you like to play again...? (y/n)")

        if choice_variable.lower() in ('yes', 'y'):
            return start_game(all_quotes)
        elif choice_variable.lower() in ('no', 'n'):
            print("BYE..!")
        else:
            print("Enter a valid input..")

def write_quotes(quotes):
    with open("quotes.csv", "w") as csv_file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()

        for quote in quotes:
            try:
                csv_writer.writerow(quote)
            except:
                pass
            

quotes = scrape_quotes()
write_quotes(quotes)
start_game(quotes)
