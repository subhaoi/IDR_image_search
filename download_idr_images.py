
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

links = ['https://idronline.org', 'https://idronline.org/about/work-with-us/', 'https://idronline.org/sectors/rights/', 'https://idronline.org/article/gender/integrating-menstrual-health-and-hygiene-in-the-covid-19-response/', 'https://idronline.org/video/farmers-protest-the-women-at-tikri/', 'https://idronline.org/article/advocacy-government/working-with-the-government-strategies-for-the-social-sector/', 'https://idronline.org/contributor/tanaya-jagtiani/', 'https://idronline.org/philanthropy-needs-to-create-space-for-failure/', 'https://idronline.org/category/themes/advocacy-government/', 'https://idronline.org/category/themes/youth/', 'https://idronline.org/themes/diversity-inclusion/', 'https://idronline.org/contributor/ria-saha/', 'https://idronline.org/contributor/argentina-matavel-piccin/', 'https://idronline.org/contributor/chhavi-arora/', 'https://idronline.org/sectors/health/', 'https://idronline.org/category/themes/philanthropy-csr/', 'https://idronline.org/category/themes/ecosystem-development/', 'https://idronline.org/category/features/a-day-in-the-life-of/', 'https://idronline.org/features/a-day-in-the-life-of/', 'https://idronline.org/category/expertise/board-governance/', 'https://idronline.org/themes/social-business/', 'https://idronline.org/category/sectors/', 'https://idronline.org/contributor/krishna-keshavani/', 'https://idronline.org/category/expertise/monitoring-evaluation/', 'https://idronline.org/events-and-conferences/', 'https://idronline.org/contributor/pranav-kumar-choudhary/', 'https://idronline.org/about/team/', 'https://idronline.org/video/farmacts2020-perspectives-ramesh-panghal-on-the-concerns-of-farmers/', 'https://idronline.org/category/themes/social-justice/', 'https://idronline.org/category/themes/social-business/', 'https://idronline.org/podcasts/', 'https://idronline.org/category/sectors/agriculture/', 'https://idronline.org/idr-interviews-bezwada-wilson/', 'https://idronline.org/expertise/', 'https://idronline.org/contributor/azra-mobin/', 'https://idronline.org/contributor/ravi-bagaria/', 'https://idronline.org/contributor/dr-sanjana-brahmawar-mohan/', 'https://idronline.org/category/themes/gender/', 'https://idronline.org/category/sectors/education/', 'https://idronline.org/sectors/environment/', 'https://idronline.org/features/failure-files/', 'https://idronline.org/themes/gender/', 'https://idronline.org/expertise/technology/', 'https://idronline.org/category/sectors/rights/', 'https://idronline.org/terms-of-use/', 'https://idronline.org/contact/', 'https://idronline.org/category/expertise/leadership-talent/', 'https://idronline.org/features/idr-interviews/', 'https://idronline.org/privacy-policy-2/', 'https://idronline.org/contributor/vk-madhavan/', 'https://idronline.org/ground-up-stories/covid-19-worsens-gender-based-discrimination/', 'https://idronline.org/category/themes/scale/', 'https://idronline.org/sectors/education/', 'https://idronline.org/features/inequality/who-is-looking-out-for-migrant-workers-during-the-covid-19-crisis/', 'https://idronline.org/humour/', 'https://idronline.org/about/philanthropic-partners/', 'https://idronline.org/category/features/ground-up/', 'https://idronline.org/about/23-north/', 'https://idronline.org/about/', 'https://idronline.org/contributor/india-development-review/', 'https://idronline.org/a-social-worker-in-lucknow-supports-families-affected-by-covid-19/', 'https://idronline.org/ground-up-stories/covid-19-is-limiting-access-to-maternal-healthcare-in-rural-bihar/', 'https://idronline.org/category/expertise/technology/', 'https://idronline.org/sectors/water-sanitation/', 'https://idronline.org/contributor/bijal-brahmbhatt/', 'https://idronline.org/news', 'https://idronline.org/category/themes/urban/', 'https://idronline.org/themes/ecosystem-development/', 'https://idronline.org/how-to-develop-leaders-for-social-change-leadership-development-programme/', 'https://idronline.org/category/themes/inequality/', 'https://idronline.org/contributor/dr-pavitra-mohan/', 'https://idronline.org/ground-up-stories/sarkari-loan-but-financial-institutions-bear-the-risk/', 'https://idronline.org/expertise/monitoring-evaluation/', 'https://idronline.org/themes/scale/', 'https://idronline.org/when-ambition-exceeds-ability-in-the-nonprofit-sector/', 'https://idronline.org/category/themes/diversity-inclusion/', 'https://idronline.org/category/expertise/', 'https://idronline.org/article/health/tackling-vaccine-hesitancy-in-rural-rajasthan/', 'https://idronline.org/good-intentions-are-not-enough-to-create-social-change-fellowship/', 'https://idronline.org/category/themes/', 'https://idronline.org/features/health/a-corona-demon-raises-covid-19-awareness-in-andhra-pradesh/', 'https://idronline.org/contributor/rajen-makhijani/', 'https://idronline.org/themes/youth/', 'https://idronline.org/write-for-idr/', 'https://idronline.org/features/health/individual-mental-health-depends-on-collective-well-being/', 'https://idronline.org/ground-up-stories/mending-fences-with-elephants/', 'https://idronline.org/contributor/sree-ramulu/', 'https://idronline.org/contributor/smarinita-shetty/', 'https://idronline.org/article/fundraising-and-communications/understanding-updates-to-section-80g-of-the-income-tax-act/', 'https://idronline.org/category/features/failure-files/', 'https://idronline.org/sectors/livelihoods/', 'https://idronline.org/themes/advocacy-government/', 'https://idronline.org/contributor/itishree-behera/', 'https://idronline.org/contributor/gaurav-singh/', 'https://idronline.org', 'https://idronline.org/features/ground-up/', 'https://idronline.org/category/expertise/programme/', 'https://idronline.org/fellowships/', 'https://idronline.org/print-archive/', 'https://idronline.org/video/do-we-write-off-one-year-wilima-wadhwa-on-learnings-from-aser-2020-and-the-pandemic/', 'https://idronline.org/sectors/', 'https://idronline.org/article/humour/if-shakespeare-was-a-donor-in-the-social-sector/', 'https://idronline.org/article/humour/how-we-spend-our-lives/', 'https://idronline.org/themes/collaboration/', 'https://idronline.org/contributor/world-economic-forum/', 'https://idronline.org/category/themes/collaboration/', 'https://idronline.org/about/board/', 'https://idronline.org/themes/urban/', 'https://idronline.org/', 'https://idronline.org/expertise/board-governance/', 'https://idronline.org/contributor/ritu-jain/', 'https://idronline.org/sectors/agriculture/', 'https://idronline.org/category/sectors/water-sanitation/', 'https://idronline.org/features/centred-self-the-wellbeing-series/', 'https://idronline.org/themes/inequality/', 'https://idronline.org/contributor/shreya-adhikari/', 'https://idronline.org/category/features/idr-interviews/', 'https://idronline.org/category/expertise/fund-raising-communications//', 'https://idronline.org/contributor/poonam-kathuria/', 'https://idronline.org/contributor/rachita-vora/', 'https://idronline.org/features/idr-explains/', 'https://idronline.org/idr-interview-dr-vandana-shiva/', 'https://idronline.org/themes/covid-19/', 'https://idronline.org/category/sectors/livelihoods/', 'https://idronline.org/contributor/gayatri-sahgal/', 'https://idronline.org/how-you-can-support-nonprofits-in-their-covid-19-relief-efforts-in-2021/', 'https://idronline.org/category/sectors/health/', 'https://idronline.org/themes/social-justice/', 'https://idronline.org/idr-interviews-dr-john-oommen/', 'https://idronline.org/themes/', 'https://idronline.org/features/', 'https://idronline.org/video/', 'https://idronline.org/features/perspectives/', 'https://idronline.org/themes/philanthropy-csr/', 'https://idronline.org/category/sectors/environment/', 'https://idronline.org/expertise/programme/', 'https://idronline.org/republishing-guidelines/', 'https://idronline.org/expertise/fundraising-and-communications/', 'https://idronline.org/expertise/leadership-talent/', 'https://idronline.org/about/ethics-statement/']
count = 0

for link in links:
    htmldata = urlopen(link)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:
        if "idronline" in item['src']:
            try:
                urllib.request.urlretrieve(item['src'], "static/" + str(count) + "." + item['src'].split(".")[-1])
                count +=1
                print(count)
            except:
                pass
        


from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
  
  
# Set for storing urls with same domain
links_intern = set()
input_url = "https://idronline.org/"
depth = 1
  
# Set for storing urls with different domain
links_extern = set()
  
  
# Method for crawling a url at next level
def level_crawler(input_url):
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc
  
    # Creates beautiful soup object to extract html tags
    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml")
  
    # Access all anchor tags from input 
    # url page and divide them into internal
    # and external categories
    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            is_valid = bool(final_parsed_href.scheme) and bool(
                final_parsed_href.netloc)
            if is_valid:
                if current_url_domain not in href and href not in links_extern:
                    print("Extern - {}".format(href))
                    links_extern.add(href)
                if current_url_domain in href and href not in links_intern:
                    print("Intern - {}".format(href))
                    links_intern.add(href)
                    temp_urls.add(href)
    return temp_urls
  
  
if(depth == 0):
    print("Intern - {}".format(input_url))
elif(depth == 1):
    level_crawler(input_url)
else:
    # We have used a BFS approach
    # considering the structure as
    # a tree. It uses a queue based
    # approach to traverse
    # links upto a particular depth.
    queue = []
    queue.append(input_url)
    for j in range(depth):
        for count in range(len(queue)):
            url = queue.pop(0)
            urls = level_crawler(url)
            for i in urls:
                queue.append(i)