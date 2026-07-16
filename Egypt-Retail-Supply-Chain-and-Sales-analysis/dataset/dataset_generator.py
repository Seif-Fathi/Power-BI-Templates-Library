"""
Egypt Retail Sales Dataset Generator
====================================

Purpose
-------
Generate a synthetic retail sales dataset for the
Egypt Retail Supply Chain & Sales Analytics Power BI template.

The generated dataset simulates realistic retail transactions across
Egyptian governorates and supports advanced Power BI features such as:

- Time Intelligence
- Dynamic KPI Cards
- Dynamic Ranking
- Field Parameters
- Regional Analysis
- Drillthrough
- Interactive Filtering

Output
------
egypt_retail_sales.csv
"""



import pandas as pd
import numpy as np


# ============================================================
# Configuration
# ============================================================

# Dataset date range
start_date = "2023-01-01"  
end_date = "2026-06-30"
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

np.random.seed(42)  
keep_mask = np.random.rand(len(date_range)) > 0.05
active_dates = date_range[keep_mask]



# ============================================================
# Master Data
# ============================================================

# Customer names
customers = [
    "Ahmed Mansour", "Mohamed Ali", "Tarek Sayed", "Amr Hassan", "Youssef Hussein", 
    "Fatma Ibrahim", "Aya Mahmoud", "Rania Moustafa", "Mona Abdelrahman", "Zainab Soliman",
    "Mustafa Kamal", "Hany Ramzy", "Sherif Anwar", "Nour El-Din", "Mahmoud Saad", 
    "Hazem Emam", "Karim Abdelaziz", "Dina El-Sherbiny", "Hassan El-Raddad", "Maged El-Kedwany",
    "Wael Jassar", "Tamer Hosny", "Amr Diab", "Mohamed Ramadan", "Asma Abulyazeid", 
    "Amina Khalil", "Yasmine Sabri", "Mena Shalaby", "Hend Sabry", "Mona Zaki",
    "Khaled El-Nabawy", "Karim Mahmoud", "Ahmed Helmy", "Eyad Nassar", "Asser Yassin",
    "Amir Karara", "Ahmed Ezz", "Ahmed Mekky", "Mohamed Henedy", "Adel Emam",
    "Nelly Karim", "Ghada Abdelrazek", "Mai Ezz Eldin", "Reem Moustafa", "Tara Emad",
    "Jamila Awad", "Huda El-Mufti", "Mayan El-Sayed", "Sahar El-Sayegh", "Asmaa Galal",
    "Omar Sherif", "Farouk El-Fishawy", "Nour El-Sherif", "Hussein Fahmy", "Mahmoud Yassin"
]

# Customer segments
segments = ["Consumer", "Corporate", "Home Office"]

# Egyptian governorates
governorates = [
    "Cairo", "Giza", "Alexandria", "Qalyubia", "Sharqia", 
    "Dakahlia", "Monufia", "Gharbia", "Kafr El-Sheikh", "Beheira", 
    "Damietta", "Port Said", "Ismailia", "Suez", "North Sinai", 
    "South Sinai", "Beni Suef", "Fayoum", "Minya", "Asyut", 
    "New Valley", "Sohag", "Qena", "Luxor", "Aswan", 
    "Red Sea", "Matrouh"
]

# Governorate -> Cities mapping
governorates_with_cities = {
    "Cairo": ["New Cairo", "Nasr City", "Maadi"],
    "Giza": ["Sheikh Zayed", "6th of October", "Dokki"],
    "Alexandria": ["Smouha", "Miami", "Stanly"],
    "Qalyubia": ["Banha", "Shubra El-Kheima", "Khanka"],
    "Sharqia": ["Zagazig", "10th of Ramadan", "Belbeis"], 
    "Dakahlia": ["Mansoura", "Mit Ghamr", "Talkha"],
    "Monufia": ["Shibin El Kom", "Sadat City", "Menouf"],
    "Gharbia": ["Tanta", "El Mahalla El Kubra", "Zifta"],
    "Kafr El-Sheikh": ["Kafr El-Sheikh City", "Desouk", "Baltim"],
    "Beheira": ["Damanhour", "Kafr El Dawar", "Kom Hamada"], 
    "Damietta": ["Damietta City", "Ras El Bar", "New Damietta"],
    "Port Said": ["Al Sharq", "Al Arab", "Port Fouad"],
    "Ismailia": ["Ismailia City", "Fayed", "Al Qantara"],
    "Suez": ["Arbaeen", "Suez City", "Attaka"],
    "North Sinai": ["Arish", "Sheikh Zuweid", "Rafah"], 
    "South Sinai": ["Sharm El-Sheikh", "Dahab", "Nuweiha"],
    "Beni Suef": ["Beni Suef City", "Nasser", "Biba"],
    "Fayoum": ["Fayoum City", "Sinnuris", "Tamiya"],
    "Minya": ["Minya City", "Mallawi", "Samalut"],
    "Asyut": ["Asyut City", "Dairut", "Fateh"], 
    "New Valley": ["Kharga", "Dakhla", "Farafra"],
    "Sohag": ["Sohag City", "Tahta", "Akhmim"],
    "Qena": ["Qena City", "Nag Hammadi", "Abu Tesht"],
    "Luxor": ["Luxor City", "Esna", "Armant"],
    "Aswan": ["Aswan City", "Kom Ombo", "Edfu"], 
    "Red Sea": ["Hurghada", "Gouna", "Marsa Alam"],
    "Matrouh": ["Marsa Matrouh", "Siwa", "Alamein"]
}

# Sales representatives
salespeople = ['Ahmed Ragab', 'Karim Salah', 'Sara Amin', 'Mina Youssef', 'Noha Mahmoud' , 'Youssef Khaled' , 'Amr Salah']


# ============================================================
# Product Catalog
# ============================================================

# Product hierarchy and base prices
products = {
    "Technology": {"Phones": 1500, "Accessories": 350, "Copiers": 5000, "Machines": 5500},
    "Furniture": {"Chairs": 850, "Tables": 4500, "Bookcases": 2000, "Furnishings": 150},
    "Office Supplies": {"Paper": 50, "Binders": 80, "Storage": 280, "Art": 60},
    "Home Appliances": {"Refrigerators": 12000, "Microwaves": 3500, "Blenders": 800, "Air Conditioners": 16000},
    "Clothing & Apparel": {"Shirts": 400, "Pants": 600, "Shoes": 1200, "Jackets": 1800},
    "Sports & Outdoors": {"Fitness Equipment": 3000, "Sportswear": 500, "Bicycles": 4500, "Camping Gear": 1500}
}



# ============================================================
# Transaction Generation
# ============================================================
data_list = []

for i, current_date in enumerate(active_dates):
    transactions_per_day = np.random.randint(1, 4)
    
    for t in range(transactions_per_day):
        # -----------------------------
        # Order Information
        # -----------------------------

        
        order_id = f"EG-{current_date.year}-{1000 + i + t}"
        ship_days = np.random.randint(0, 7)
        ship_date = current_date + pd.Timedelta(days=ship_days)
        
        ship_mode = "Same Day" if ship_days == 0 else ("First Class" if ship_days == 1 else ("Second Class" if ship_days <= 3 else "Standard Class"))
        
        
        
        # -----------------------------
        # Customer Information
        # -----------------------------
        customer = np.random.choice(customers)
        segment = np.random.choice(segments)


        # -----------------------------
        # Geographic Information
        # -----------------------------
        gov = np.random.choice(list(governorates_with_cities.keys())) 
        city = np.random.choice(governorates_with_cities[gov])       

        
        # -----------------------------
        # Sales Representative
        # -----------------------------
        sales_person = np.random.choice(salespeople)


        
        # -----------------------------
        # Product Information
        # -----------------------------
        category = np.random.choice(list(products.keys()))
        sub_category = np.random.choice(list(products[category].keys()))
        product_id = f"{category[:3].upper()}-{sub_category[:2].upper()}-{np.random.randint(100, 999)}"
        
        base_price = products[category][sub_category]
        unit_price = round(base_price * np.random.uniform(0.9, 1.1), 2)
        quantity = np.random.randint(1, 11)



        # -----------------------------
        # Business Growth Simulation
        # -----------------------------
        # Introduce gradual yearly growth so the dashboard
        # produces meaningful Year-over-Year insights.
        if current_date.year == 2023:
            growth_factor = 1.0
        elif current_date.year == 2024:
            growth_factor = 1.2
        elif current_date.year == 2025:
            growth_factor = 1.4
        else:
            growth_factor = 1.6
        
        discount_rate = np.random.choice([0.0, 0.05, 0.10, 0.15], p=[0.6, 0.2, 0.1, 0.1]) 
        
        sales_before_discount = quantity * unit_price * growth_factor
        discount_amount = round(sales_before_discount * discount_rate, 2)
        sales = round(sales_before_discount - discount_amount, 2)



        # -----------------------------
        # Cost & Profit Simulation
        # -----------------------------
        cost = round(sales * np.random.uniform(0.65, 0.80), 2) 
        profit = round(sales - cost, 2)
        
        revenue = sales

        # Approximately 5% of orders are returned
        returned = "Yes" if np.random.rand() < 0.05 else "No"  


        # -----------------------------
        # Store Transaction
        # -----------------------------
        data_list.append([
            order_id, current_date.strftime("%Y-%m-%d"), ship_date.strftime("%Y-%m-%d"),
            ship_days, ship_mode, customer, segment, "Egypt", gov, city, sales_person,
            product_id, category, sub_category, quantity, unit_price, discount_rate,
            sales, cost, revenue, profit, returned
        ])


# ============================================================
# Export Dataset
# ============================================================
columns = ["Order ID", "Order Date", "Ship Date", "Shipping Days", "Ship Mode", "Customer Name", 
           "Segment", "Country", "Governorate", 'city', 'sales_person', "Product ID", "Category", "Sub-Category", 
           "Quantity", "Unit Price", "Discount", "Sales", "Cost", "Revenue", "Profit", "Returned"]


df = pd.DataFrame(data_list, columns=columns)
df.to_csv("egypt_retail_sales.csv", index=False)

print("=" * 50)
print("Egypt Retail Sales Dataset Generated Successfully")
print(f"Rows Generated : {len(df):,}")
print(f"Date Range     : {start_date} → {end_date}")
print("Output File    : egypt_retail_sales.csv")
print("=" * 50)