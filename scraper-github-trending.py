import requests
from bs4 import BeautifulSoup
import csv
# Collect the github pagepage = requests.get('https://github.com/trending')
page = requests.get('https://github.com/trending');
soup = BeautifulSoup(page.text, 'html.parser');
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")
repo_list = repo.find_all(class_="Box-row");
print(len(repo_list));
file_name = "github_trending_today.csv";
f = csv.writer(open(file_name, 'w', newline=''));
f.writerow(['Developer', 'Repo Name', 'Number of Stars']);

for repo in repo_list:
    full_repo_name = repo.find(class_="h3").find('a').text.split('/');
    developer = full_repo_name[0].strip();
    repo_name = full_repo_name[1].strip();
    stars = repo.find(class_='octicon octicon-star').parent.text.strip();
    print('developer', developer);
    print('repo name', repo_name);
    print('stars', stars);
    print('------------------------------------------');
    f.writerow([developer, repo_name, stars]);
