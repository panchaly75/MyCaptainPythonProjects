
print("\tMyCaptain Python project's : 07\t")
print("__________________________________________________________________________________________________________\n")



import requests
from bs4 import BeautifulSoup
import csv

input_page = int(input("Enter max. page detail you want\t:\t"))                 #asking no. of pages you wantto append

for page_no in range(input_page):                                               #loop for iterating page
    url = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_a1bd4f42-0266-460d-8a23-4cdb526a2358_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=34WHNYFH5V2Y&page="+str(page_no +1)
    hdr = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"

    req = requests.get(url, hdr)                                                #to get info from internet
    content = req.content

    soup = BeautifulSoup(content, "html.parser")                                #info from net convert into readable form

    all_laptop = soup.find_all("div" , {"class" : "_1AtVbE col-12-12"})         #get info for all laptop present on laptop card list

    for lptp in all_laptop:                                                     #loop for each laptop present into the all_laptop list 
        try:
            laptop_name = lptp.find("div" , {"class" : "_4rR01T"}).get_text()
            laptops = laptop_name.split(" - ")

            laptop_price = lptp.find("div" , {"class" : "_30jeq3 _1_WHN1"}).get_text()
            laptop_price = laptop_price.replace("₹", "")
            laptop_price = laptop_price.replace(",", "")

            laptops.append(laptop_price)
            print(laptops)
            with open("popular_laptops.csv","a", newline="") as csv_file:
                writer = csv.writer(csv_file)

                if csv_file.tell()==0:
                    writer.writerow(["Laptop Name", "Laptop Spec's","Price"])

                writer.writerow(laptops)
        except AttributeError:
            pass
