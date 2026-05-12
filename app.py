import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# ============================
# EMBEDDED DATABASES
# ============================

# Cars Database
cars_data = [
    ["make", "model", "tank_capacity_l", "l_100km_highway", "l_100km_city", "curb_weight_kg", "max_payload_kg", "min_octane"],
    ["Aston Martin", "DBX", 85, 13.0, 15.5, 2245, 775, 91],
    ["Aston Martin", "Vantage", 73, 9.5, 13.5, 1650, 300, 98],
    ["Audi", "A4", 54, 6.5, 8.5, 1550, 500, 91],
    ["Audi", "A6", 65, 7.0, 9.5, 1700, 550, 91],
    ["Audi", "Q2", 55, 6.8, 9.0, 1300, 500, 91],
    ["Audi", "Q5", 65, 7.5, 9.8, 1800, 550, 91],
    ["Audi", "Q7", 85, 9.5, 12.0, 2100, 700, 91],
    ["Audi", "RS Q8", 85, 12.5, 16.0, 2250, 650, 98],
    ["Audi", "RS7", 72, 11.5, 15.0, 2050, 500, 98],
    ["BMW", "2 Series", 50, 6.5, 8.5, 1450, 450, 91],
    ["BMW", "3 Series Gran Limousine", 55, 6.8, 9.0, 1600, 500, 91],
    ["BMW", "5 Series", 65, 7.0, 9.5, 1700, 550, 91],
    ["BMW", "7 Series", 78, 8.5, 11.5, 1950, 600, 91],
    ["BMW", "8 Series", 78, 9.0, 12.0, 1850, 450, 98],
    ["BMW", "M2", 52, 9.0, 12.5, 1600, 400, 98],
    ["BMW", "M4 Competition", 59, 9.5, 13.0, 1700, 400, 98],
    ["BMW", "X1", 55, 7.0, 9.0, 1550, 500, 91],
    ["BMW", "X3", 65, 8.0, 10.5, 1800, 550, 91],
    ["BMW", "X5", 85, 9.5, 12.5, 2150, 700, 91],
    ["BMW", "X5 M", 85, 13.5, 17.0, 2350, 650, 98],
    ["BMW", "X6", 85, 10.0, 13.0, 2200, 650, 91],
    ["BMW", "X7", 85, 10.5, 13.5, 2400, 750, 91],
    ["BMW", "Z4", 52, 7.5, 10.5, 1450, 300, 91],
    ["Bajaj", "Qute (RE60)", 8, 3.5, 4.5, 400, 300, 87],
    ["Bentley", "Bentayga", 85, 12.0, 16.5, 2650, 700, 98],
    ["Bentley", "Continental", 90, 11.5, 15.0, 2300, 400, 98],
    ["Bentley", "Flying Spur", 90, 12.0, 15.5, 2450, 450, 98],
    ["Changan", "CS75", 58, 8.0, 10.5, 1600, 550, 91],
    ["Citroen", "C3", 40, 5.5, 7.5, 1000, 400, 87],
    ["Citroen", "C5 Aircross", 55, 6.8, 9.0, 1600, 550, 91],
    ["Compass", "Trailhawk", 60, 9.0, 12.0, 1700, 500, 87],
    ["Datsun", "GO", 35, 5.0, 6.5, 800, 400, 87],
    ["Datsun", "GO Plus", 35, 5.2, 6.8, 850, 400, 87],
    ["Datsun", "redi-GO", 28, 4.8, 6.2, 750, 350, 87],
    ["Ferrari", "812", 92, 15.0, 20.0, 1600, 300, 98],
    ["Ferrari", "F8 Tributo", 78, 13.5, 18.0, 1450, 250, 98],
    ["Ferrari", "Portofino", 80, 12.5, 17.0, 1650, 300, 98],
    ["Ferrari", "Roma", 91, 11.5, 15.5, 1550, 300, 98],
    ["Force", "Gurkha", 63, 10.0, 12.5, 2200, 800, 0],
    ["Honda", "Amaze", 35, 5.5, 7.0, 950, 400, 91],
    ["Honda", "City", 40, 5.8, 7.5, 1100, 450, 91],
    ["Honda", "City 4th Generation", 40, 6.0, 7.8, 1080, 450, 91],
    ["Honda", "City Hybrid", 40, 4.5, 5.5, 1150, 400, 91],
    ["Honda", "Civic", 47, 6.5, 8.5, 1300, 400, 91],
    ["Honda", "Jazz", 40, 5.5, 7.2, 1050, 400, 91],
    ["Honda", "WR-V", 40, 6.0, 8.0, 1100, 450, 91],
    ["Hyundai", "Accent", 45, 6.2, 8.2, 1100, 450, 91],
    ["Hyundai", "Alcazar", 50, 8.5, 11.0, 1650, 550, 91],
    ["Hyundai", "Aura", 37, 5.5, 7.0, 950, 400, 87],
    ["Hyundai", "Creta", 50, 7.0, 9.5, 1300, 500, 91],
    ["Hyundai", "Elantra", 50, 6.5, 8.5, 1250, 450, 91],
    ["Hyundai", "Santro", 37, 5.2, 6.8, 850, 350, 87],
    ["Hyundai", "Tucson", 54, 8.0, 10.5, 1600, 550, 91],
    ["Hyundai", "Venue", 45, 6.5, 8.5, 1100, 450, 91],
    ["Hyundai", "Verna", 45, 6.0, 8.0, 1150, 450, 91],
    ["Hyundai", "Xcent Prime", 37, 5.5, 7.2, 950, 400, 87],
    ["Hyundai", "i20", 40, 5.8, 7.5, 1000, 400, 91],
    ["Isuzu", "D-Max", 76, 8.0, 10.0, 1900, 1000, 0],
    ["Isuzu", "MU-X", 80, 8.5, 11.0, 2100, 800, 0],
    ["Jaguar", "F-Pace", 82, 9.0, 12.0, 1900, 600, 91],
    ["Jaguar", "F-TYPE", 70, 9.5, 13.5, 1650, 300, 98],
    ["Jaguar", "XE", 60, 7.0, 9.5, 1600, 450, 91],
    ["Jaguar", "XF", 70, 7.5, 10.0, 1750, 500, 91],
    ["Jeep", "Meridian", 70, 8.0, 10.5, 2200, 700, 0],
    ["Jeep", "Wrangler", 85, 10.5, 14.0, 2000, 600, 87],
    ["Jetour", "T2", 65, 8.5, 11.0, 1650, 550, 91],
    ["Kia", "Pegas", 45, 6.0, 8.0, 1080, 450, 91],
    ["Kia", "Seltos", 50, 7.0, 9.5, 1300, 500, 91],
    ["Kia", "Sonet", 45, 6.5, 8.5, 1100, 450, 91],
    ["Kia", "Sportage", 54, 7.5, 9.8, 1500, 500, 91],
    ["Lamborghini", "Aventador", 90, 18.0, 25.0, 1650, 300, 98],
    ["Lamborghini", "Huracan EVO", 80, 15.0, 20.0, 1450, 250, 98],
    ["Lamborghini", "Urus", 85, 13.0, 16.5, 2200, 700, 98],
    ["Land Rover", "Defender", 90, 10.5, 13.5, 2200, 800, 91],
    ["Land Rover", "Discovery Sport", 70, 8.5, 11.0, 1850, 650, 91],
    ["Land Rover", "Range Rover", 105, 11.0, 14.5, 2350, 800, 98],
    ["Land Rover", "Range Rover Sport", 90, 10.5, 13.5, 2200, 750, 98],
    ["Land Rover", "Range Rover Velar", 82, 9.5, 12.5, 1950, 650, 91],
    ["Lexus", "ES", 50, 5.5, 6.5, 1700, 450, 91],
    ["Lexus", "LC 500h", 82, 7.5, 9.5, 1950, 300, 98],
    ["Lexus", "LS", 82, 7.8, 10.0, 2350, 500, 91],
    ["Lexus", "LX", 93, 14.0, 18.0, 2700, 700, 91],
    ["Lexus", "NX", 55, 6.5, 7.5, 1750, 500, 91],
    ["Lexus", "RX", 65, 7.0, 8.5, 2000, 550, 91],
    ["MG", "5", 50, 6.8, 9.0, 1250, 450, 91],
    ["MG", "Astor", 50, 7.5, 10.0, 1400, 500, 91],
    ["MG", "Gloster", 75, 9.0, 11.5, 2500, 800, 0],
    ["MG", "Hector", 60, 8.5, 11.0, 1600, 550, 91],
    ["MG", "Hector Plus", 60, 8.8, 11.5, 1650, 550, 91],
    ["Mahindra", "Alturas G4", 70, 9.0, 11.5, 2150, 700, 0],
    ["Mahindra", "Bolero", 60, 9.5, 12.0, 1800, 700, 0],
    ["Mahindra", "Bolero Camper", 57, 10.0, 13.0, 1850, 800, 0],
    ["Mahindra", "Bolero Neo", 50, 8.5, 11.0, 1650, 600, 0],
    ["Mahindra", "Bolero PikUp ExtraLong", 57, 9.0, 12.0, 1800, 1200, 0],
    ["Mahindra", "KUV 100 NXT", 35, 6.0, 8.0, 1100, 400, 87],
    ["Mahindra", "Marazzo", 45, 7.5, 9.5, 1650, 600, 0],
    ["Mahindra", "Scorpio Classic", 60, 9.0, 12.0, 1900, 700, 0],
    ["Mahindra", "Scorpio-N", 57, 10.0, 13.0, 2000, 700, 91],
    ["Mahindra", "Thar", 57, 9.5, 12.5, 1750, 600, 91],
    ["Mahindra", "XUV300", 42, 7.0, 9.0, 1300, 500, 91],
    ["Mahindra", "XUV700", 60, 8.5, 11.0, 1800, 650, 91],
    ["Maruti", "Alto 800", 32, 4.8, 6.2, 730, 350, 87],
    ["Maruti", "Alto 800 tour", 32, 5.0, 6.5, 750, 350, 87],
    ["Maruti", "Alto K10", 32, 4.9, 6.4, 780, 350, 87],
    ["Maruti", "Baleno", 37, 5.2, 6.8, 920, 400, 91],
    ["Maruti", "Brezza", 48, 6.5, 8.5, 1150, 450, 91],
    ["Maruti", "Celerio", 32, 4.8, 6.5, 820, 350, 87],
    ["Maruti", "Ciaz", 43, 5.8, 7.5, 1050, 450, 91],
    ["Maruti", "Dzire", 37, 5.5, 7.0, 950, 400, 91],
    ["Maruti", "Eeco", 40, 6.5, 8.0, 930, 700, 87],
    ["Maruti", "Ertiga", 45, 6.8, 9.0, 1200, 500, 91],
    ["Maruti", "Ignis", 32, 5.5, 7.2, 850, 400, 87],
    ["Maruti", "S-Cross", 45, 6.5, 8.5, 1150, 450, 91],
    ["Maruti", "S-Presso", 27, 5.0, 6.5, 800, 350, 87],
    ["Maruti", "Swift", 37, 5.2, 6.8, 920, 400, 91],
    ["Maruti", "Swift Dzire Tour", 37, 5.5, 7.0, 950, 400, 91],
    ["Maruti", "XL6", 45, 6.8, 9.0, 1250, 500, 91],
    ["Maserati", "Ghibli", 80, 11.0, 15.0, 1800, 450, 98],
    ["Maserati", "GranCabrio", 86, 13.5, 18.0, 1850, 300, 98],
    ["Maserati", "GranTurismo", 86, 13.0, 17.5, 1700, 300, 98],
    ["Maserati", "Levante", 80, 12.0, 15.5, 2100, 600, 98],
    ["Maserati", "Quattroporte", 80, 11.5, 15.0, 1900, 450, 98],
    ["Mclaren", "GT", 72, 11.0, 14.5, 1450, 300, 98],
    ["Mercedes-Benz", "A-Class Limousine", 50, 6.5, 8.5, 1450, 450, 91],
    ["Mercedes-Benz", "AMG A 35", 51, 8.5, 11.0, 1550, 400, 98],
    ["Mercedes-Benz", "AMG A 45 S", 51, 9.0, 12.0, 1600, 400, 98],
    ["Mercedes-Benz", "AMG C 43", 66, 9.5, 12.5, 1750, 450, 98],
    ["Mercedes-Benz", "AMG G 63", 100, 15.0, 18.5, 2550, 700, 98],
    ["Mercedes-Benz", "AMG GLC 43", 66, 10.0, 13.0, 1900, 550, 98],
    ["Mercedes-Benz", "AMG GLE 53", 85, 11.5, 14.5, 2300, 650, 98],
    ["Mercedes-Benz", "AMG GLE 63 S", 85, 13.0, 16.5, 2350, 650, 98],
    ["Mercedes-Benz", "AMG GT", 70, 11.0, 14.0, 1650, 300, 98],
    ["Mercedes-Benz", "C-Class", 66, 7.0, 9.5, 1600, 500, 91],
    ["Mercedes-Benz", "CLS", 80, 8.0, 11.0, 1800, 500, 91],
    ["Mercedes-Benz", "E-Class", 66, 7.5, 10.0, 1750, 550, 91],
    ["Mercedes-Benz", "G-Class", 100, 14.0, 17.5, 2450, 700, 98],
    ["Mercedes-Benz", "GLA", 50, 7.0, 9.0, 1450, 500, 91],
    ["Mercedes-Benz", "GLC", 66, 8.0, 10.5, 1800, 550, 91],
    ["Mercedes-Benz", "GLC Coupe", 66, 8.5, 11.0, 1850, 500, 91],
    ["Mercedes-Benz", "GLE", 85, 9.5, 12.5, 2150, 650, 91],
    ["Mercedes-Benz", "GLS", 85, 10.5, 13.5, 2350, 700, 91],
    ["Mercedes-Benz", "Maybach S-Class", 76, 9.0, 12.0, 2300, 500, 98],
    ["Mercedes-Benz", "S-Class", 76, 8.5, 11.5, 2100, 550, 98],
    ["Mercedes-Benz", "V-Class", 70, 9.5, 12.0, 2200, 800, 91],
    ["Mini", "Cooper 3 DOOR", 44, 6.0, 8.0, 1250, 400, 91],
    ["Mini", "Cooper Convertible", 44, 6.5, 8.5, 1300, 350, 91],
    ["Mini", "Cooper Countryman", 51, 7.0, 9.0, 1450, 500, 91],
    ["Mitsubishi", "Pajero", 88, 12.0, 15.0, 2300, 650, 91],
    ["Nissan", "Altima", 68, 7.0, 9.5, 1450, 450, 91],
    ["Nissan", "GT-R", 74, 11.5, 15.0, 1750, 300, 98],
    ["Nissan", "Kicks", 50, 7.0, 9.5, 1200, 450, 91],
    ["Nissan", "Magnite", 40, 6.5, 8.5, 1000, 400, 91],
    ["Nissan", "Patrol", 140, 11.5, 16.0, 2800, 700, 95],
    ["Nissan", "Sunny", 41, 6.0, 8.0, 1050, 450, 91],
    ["Nissan", "X-Trail", 55, 7.5, 9.5, 1550, 500, 91],
    ["Porsche", "911", 64, 9.5, 13.0, 1550, 300, 98],
    ["Porsche", "Cayenne", 90, 10.5, 13.5, 2050, 700, 98],
    ["Porsche", "Cayenne Coupe", 90, 11.0, 14.0, 2100, 650, 98],
    ["Porsche", "Macan", 75, 9.5, 12.5, 1900, 600, 98],
    ["Porsche", "Panamera", 90, 9.0, 12.0, 1950, 500, 98],
    ["Renault", "KWID", 28, 5.0, 6.5, 800, 350, 87],
    ["Renault", "Kiger", 40, 6.0, 8.0, 1050, 400, 91],
    ["Renault", "Triber", 40, 6.2, 8.2, 950, 450, 91],
    ["Rolls Royce", "Dawn", 80, 15.0, 20.0, 2450, 400, 98],
    ["Rolls Royce", "Wraith", 82, 14.5, 19.0, 2400, 400, 98],
    ["Rolls-Royce", "Cullinan", 100, 15.5, 19.5, 2750, 800, 98],
    ["Rolls-Royce", "Ghost", 82, 13.5, 18.0, 2450, 500, 98],
    ["Skoda", "Kodiaq", 76, 8.0, 10.5, 1700, 600, 91],
    ["Skoda", "Kushaq", 50, 6.8, 9.0, 1250, 450, 91],
    ["Skoda", "Octavia", 50, 6.5, 8.5, 1350, 500, 91],
    ["Skoda", "Slavia", 45, 6.2, 8.2, 1200, 450, 91],
    ["Skoda", "Superb", 66, 7.0, 9.5, 1500, 550, 91],
    ["Suzuki", "Alto", 32, 4.5, 6.0, 750, 300, 87],
    ["Suzuki", "Swift", 37, 5.2, 7.0, 920, 400, 91],
    ["Tata", "Altroz", 37, 5.5, 7.5, 1050, 400, 91],
    ["Tata", "Harrier", 50, 7.0, 9.5, 1700, 600, 0],
    ["Tata", "Nexon", 44, 6.5, 8.5, 1250, 450, 91],
    ["Tata", "Punch", 37, 6.0, 8.0, 1000, 400, 91],
    ["Tata", "Tiago", 35, 5.2, 7.0, 950, 350, 91],
    ["Tata", "Tiago NRG", 35, 5.5, 7.2, 980, 350, 91],
    ["Tata", "Tigor", 35, 5.8, 7.5, 1000, 400, 91],
    ["Tata", "Yodha Pickup", 45, 8.0, 10.5, 1700, 1200, 0],
    ["Toyota", "Camry", 50, 5.0, 6.0, 1650, 450, 91],
    ["Toyota", "Corolla", 50, 6.0, 8.0, 1300, 450, 91],
    ["Toyota", "Corolla Cross", 45, 5.0, 6.5, 1450, 450, 91],
    ["Toyota", "Fortuner", 80, 8.5, 11.0, 2100, 700, 0],
    ["Toyota", "Glanza", 37, 5.5, 7.2, 950, 400, 91],
    ["Toyota", "Hilux", 80, 8.0, 10.0, 1950, 1000, 0],
    ["Toyota", "Innova Crysta", 65, 9.0, 12.0, 1850, 700, 91],
    ["Toyota", "Land Cruiser", 90, 9.5, 12.0, 2650, 850, 0],
    ["Toyota", "Land Cruiser", 93, 12.5, 15.5, 2600, 800, 91],
    ["Toyota", "Prado", 87, 11.0, 14.0, 2400, 700, 91],
    ["Toyota", "Rush", 45, 7.0, 9.5, 1150, 450, 91],
    ["Toyota", "Vellfire", 65, 7.0, 9.0, 2200, 600, 91],
    ["Toyota", "Yaris", 42, 5.5, 7.5, 1050, 400, 91],
    ["Volkswagen", "Taigun", 50, 6.8, 9.0, 1250, 500, 91],
    ["Volkswagen", "Tiguan", 60, 8.0, 10.5, 1650, 550, 91],
    ["Volkswagen", "Vento", 55, 6.5, 8.5, 1150, 450, 91],
    ["Volkswagen", "Virtus", 45, 6.2, 8.2, 1100, 450, 91],
    ["Volvo", "S60", 60, 6.0, 7.5, 1750, 500, 91],
    ["Volvo", "S90", 70, 6.5, 8.0, 1850, 500, 91],
    ["Volvo", "XC40", 54, 7.5, 9.5, 1650, 500, 91],
    ["Volvo", "XC60", 70, 7.0, 8.5, 1900, 600, 91],
    ["Volvo", "XC90", 70, 8.0, 10.0, 2150, 700, 91],
]

# Cities Database
cities_data = [
    ["city_ascii", "lat", "lng"],
    ["Dubai", 25.276987, 55.296249],
    ["Abu Dhabi", 24.466667, 54.366669],
    ["Fujairah", 25.1164, 56.3414],
    ["Jebel Ali", 25.038015, 55.11755],
    ["Sharjah", 25.3342, 55.41221],
    ["Al Ain", 24.2075, 55.74472],
    ["Ras Al Khaimah", 25.78953, 55.9432],
    ["Khor Fakkan", 25.3314, 56.355],
    ["Muscat", 23.589682, 58.373386],
    ["Salalah", 17.01505, 54.09237],
    ["Sohar", 24.348633, 56.695282],
    ["Duqm", 19.639482, 57.67791],
    ["Sur", 22.5667, 59.5667],
    ["Khasab", 26.164438, 56.242641],
    ["Nizwa", 22.9333, 57.5333],
    ["Buraimi", 24.254164, 55.802567],
    ["Riyadh", 24.713552, 46.675297],
    ["Dammam", 26.43442, 50.10326],
    ["Jubail", 27.0, 49.65],
    ["Al Khobar", 26.27944, 50.20833],
    ["Dhahran", 26.236355, 50.0326],
    ["Hofuf", 25.377, 49.587],
    ["Khafji", 28.4333, 48.4833],
    ["Jeddah", 21.49012, 39.18624],
    ["Yanbu", 24.08954, 38.0618],
    ["Medina", 24.46861, 39.61417],
    ["Mecca", 21.42251, 39.826168],
    ["Tabuk", 28.3998, 36.57151],
    ["Kuwait City", 29.378586, 47.990341],
    ["Al Ahmadi", 29.07694, 48.08389],
    ["Jahra", 29.336573, 47.675529],
    ["Salmiya", 29.3333, 48.0667],
    ["Doha", 25.285447, 51.53104],
    ["Al Khor", 25.6839, 51.5089],
    ["Mesaieed", 24.9833, 51.6167],
    ["Al Wakrah", 24.9, 51.55],
    ["Baghdad", 33.3153, 44.3661],
    ["Basra", 30.5081, 47.7835],
    ["Erbil", 36.191113, 44.009167],
    ["Mosul", 36.34, 43.13],
    ["Kirkuk", 35.4667, 44.3167],
    ["Najaf", 31.99, 44.34],
    ["Tehran", 35.69439, 51.42151],
    ["Bandar Abbas", 27.1865, 56.2808],
    ["Jask", 25.64, 57.77],
    ["Chabahar", 25.2919, 60.643],
    ["Bushehr", 28.97, 50.84],
    ["Shiraz", 29.61031, 52.53113],
    ["Isfahan", 32.65246, 51.67462],
    ["Mashhad", 36.29807, 59.60567],
    ["Karachi", 24.8608, 67.0104],
    ["Islamabad", 33.72148, 73.04329],
    ["Lahore", 31.558, 74.35071],
    ["Gwadar", 25.126389, 62.322498],
    ["Quetta", 30.18414, 67.00141],
    ["Hyderabad", 25.39689, 68.37718],
]

# Create DataFrames
cars_df = pd.DataFrame(cars_data[1:], columns=cars_data[0])
cities_df = pd.DataFrame(cities_data[1:], columns=cities_data[0])

# --- Helper ---
def clean_numeric(val):
    try:
        return float(str(val).split()[0])
    except:
        return None

# Clean numeric columns
for col in ["tank_capacity_l", "l_100km_highway", "l_100km_city",
            "curb_weight_kg", "max_payload_kg"]:
    cars_df[col] = cars_df[col].apply(clean_numeric)

cars_df["min_octane"] = pd.to_numeric(cars_df["min_octane"], errors="coerce")

st.set_page_config(page_title="Strategic Fuel Intelligence", layout="wide")

# --- Sidebar ---
st.sidebar.header("⚙️ Trip Parameters")

start_city = st.sidebar.selectbox("Start City", sorted(cities_df["city_ascii"].unique()))
end_city = st.sidebar.selectbox("End City", sorted(cities_df["city_ascii"].unique()))

car_make = st.sidebar.selectbox("Car Make", sorted(cars_df["make"].unique()))

car_models = sorted(cars_df[cars_df["make"] == car_make]["model"].unique())
car_model = st.sidebar.selectbox("Car Model", car_models)

extra_weight = st.sidebar.number_input("Extra Payload (kg)", min_value=0, step=50, value=0)
traffic_multiplier = st.sidebar.slider("Traffic / Checkpoint Multiplier", 1.0, 2.0, 1.2)
climate_hot = st.sidebar.checkbox("Extreme Heat (≥40°C) + AC")

# --- Safe Data Retrieval ---
start_df = cities_df[cities_df["city_ascii"] == start_city]
end_df = cities_df[cities_df["city_ascii"] == end_city]
car_df = cars_df[(cars_df["make"] == car_make) & (cars_df["model"] == car_model)]

if start_df.empty or end_df.empty:
    st.error("❌ Sorry! Selected car not found in database.")
    st.stop()

if car_df.empty:
    st.error("❌ Sorry! Selected car not found in database.")
    st.stop()

start_coords = start_df[["lat", "lng"]].iloc[0].values
end_coords = end_df[["lat", "lng"]].iloc[0].values
car_row = car_df.iloc[0]

tank_capacity = float(car_row["tank_capacity_l"])
l_100km_highway = float(car_row["l_100km_highway"])

if pd.isna(tank_capacity) or pd.isna(l_100km_highway) or tank_capacity <= 0 or l_100km_highway <= 0:
    st.error("❌ Sorry! Invalid or missing car specifications.")
    st.stop()

# --- Calculations ---
base_distance = geodesic(start_coords, end_coords).km
road_distance = base_distance * 1.3

fuel = (road_distance / 100) * l_100km_highway
fuel *= traffic_multiplier
if climate_hot:
    fuel *= 1.15
fuel *= (1 + 0.015 * (extra_weight // 50))
fuel *= 1.15  # crisis reserve

# --- Dashboard ---
st.title("⛽ Fuel Route Planner")

col1, col2, col3 = st.columns(3)
col1.metric("Road Distance (km)", f"{road_distance:.1f}")
col2.metric("Fuel Required (L)", f"{fuel:.1f}")
col3.metric("Tank Capacity (L)", f"{tank_capacity:.1f}")

progress = fuel / tank_capacity
st.progress(min(progress, 1.0))

if fuel > tank_capacity:
    st.error(f"⚠️ Fuel required exceeds tank capacity ({tank_capacity:.1f} L). Consider refuelling along the way.")
elif progress > 0.85:
    st.warning("⚠️ Fuel usage is near tank limit. Consider reducing payload or route risk.")
else:
    st.success("✅ Fuel capacity sufficient for this trip.")

# Map
st.map(pd.DataFrame([
    {"lat": start_coords[0], "lon": start_coords[1]},
    {"lat": end_coords[0], "lon": end_coords[1]}
]))