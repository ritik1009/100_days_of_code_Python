from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
print(soup.title)

story_data = soup.select("td .title a")
#print(story_data)
story_text = []
story_url = []
#article_upvote = soup.find_all(name="span",class_="score").getText()
for story in story_data:
    if 'https' in story.get("href"):
        #print("\n story :-",story)
        story_text.append(story.text)
        story_url.append(story.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score') if score]
print(len(article_upvotes))
#print(story_text[17])
#print(story_url[18])


largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(story_text[largest_index])


'''with open("website.html",encoding="utf-8")as file:
    contents = file.read()
soup = BeautifulSoup(contents,"html.parser")

# use find_all function to get all the element of the specific tag
paragraph = soup.find_all(name='p')

# print the title string
print(soup.title.string)

# get all the Text from the list of paragraph data that we got
for tag in paragraph:
    print(tag.getText())

all_anchor_tags = soup.find_all(name='a')
# getting all the links from the anchor tags using the get
# we caan get any attribute data using the get('name_of_the_tags')
for tags in all_anchor_tags:
    print(tags.get('href'))

# finding the specific element using the id and find method

heading = soup.find(name='h1', id="name")
print("\n Hedaing ",heading.text)

# finding the specific element using the class and find method

sub_heading = soup.find(name='h3', class_="heading")
print("\n  Sub Hedaing ",sub_heading.text)

# finding the element using the selector that is the elemnt inside other element

company_url = soup.select_one(selector="p a")
print("\n Company Url",company_url)

# getting the id element using the select_one
# as we are trying to get the data using the id we need to add the #
name = soup.select_one("#name")
print("\n Name:-",name)

# getting the class element using the select_one
# as we are trying to get the data using the id we need to add the .
headings = soup.select_one(".heading")
print("\n Name:-",headings)'''