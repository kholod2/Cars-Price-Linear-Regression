from requests_html import HTMLSession 
import csv
session = HTMLSession()

with open('new.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['car name','price','engine_capacity','cylinder','horse_power','top_speed','seats','brand','country'])

    count = 1
    links = [['ksa',82],['egypt',34],['bahrain',69],['qatar',71],['oman',69],['kuwait',71],['uae',96]]
    for link in links : 
        for x in range(1,link[1]):
            url = session.get(f"https://{link[0]}.yallamotor.com/new-cars/search?page={x}&sort=price_asc")

            cars = url.html.xpath("/html/body/div[6]/div/div[1]",first=True)

            for car in cars.absolute_links:
                print(car)
                url = session.get(car)
                try:
                    name = url.html.find("h1.font24",first=True).text
                except:
                    name = None


                try:
                    # price = url.html.find("span.font28",first=True).text
                    get_price = url.html.find('div.p24t')[0].text
                    price = get_price.split('\n')[5]
                except:
                    price = None

                features = url.html.find("div.border-unset")
                if len(features) > 0 :
                    data = features[0].text
                    data_split = data.split('\n')
                    # print(data_split)

                    try:
                        engine_capacity = data_split[1]
                    except:
                        engine_capacity = None

                    try:
                        cylinder = data_split[3]
                    except: 
                        cylinder = None
                    try:
                        horse_power = data_split[13]
                    except:
                        horse_power = None
                    try:
                        top_speed = data_split[19]
                    except:
                        top_speed = None
                    try:
                        seats = data_split[21]
                    except:
                        seats = None
                    try:
                        brand = car.split('/')[4]

                    except:                
                        brand = None




                    if None not in (name,engine_capacity,cylinder,horse_power,top_speed,seats,brand):
                        writer.writerow([name,price,engine_capacity,cylinder,horse_power,top_speed,seats,brand,link[0]])
                        count += 1
                    else:
                        print(count)
            

                    

print('Done')


