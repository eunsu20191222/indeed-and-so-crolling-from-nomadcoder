import requests
from bs4 import BeautifulSoup

limited = 50 
url = f"https://www.indeed.com/jobs?q=python&limit=50&radius={limited}"

def indeed_pages():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []
 
  for link in links[:-1]:
    pages.append(int(link.string))
    max_page = pages[-1]
  return max_page

def extract_job(html):
  title = html.find("h2", {"class": "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = str(company.string)
  company = company.strip()
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {'title':title, 'company':company, "location": location, "link": f"https://www.indeed.com/viewjob?jk={job_id} "}
  


def indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed page {page}")
    result = requests.get(f"{url}&start={page*limited}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs 


def get_jobs():
  last_indeed_page = indeed_pages()
  jobs = indeed_jobs(last_indeed_page)
  return jobs 