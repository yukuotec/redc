"""
REDC - Real Estate Data Collector
Main module for Shanghai Xuhui District property data collection
"""

import json
import pandas as pd
from datetime import datetime


class REDC:
    """
    Real Estate Data Collector for Shanghai Xuhui District
    """
    
    def __init__(self):
        self.district = "Shanghai Xuhui"
        self.properties = []
    
    def collect_data(self):
        """
        Collect sample data for Shanghai Xuhui District
        """
        sample_data = [
            {
                "community": "Tianlin Community",
                "address": "Tianlin Road 123, Xuhui District, Shanghai",
                "price": 8500,
                "unit": "monthly_rent",
                "bedrooms": 2,
                "bathrooms": 1,
                "size_sqm": 75,
                "floor": "8/18",
                "orientation": "south",
                "year_built": 2008,
                "transportation": "Metro Line 1 - Caobao Road Station (500m)",
                "property_type": "apartment",
                "last_updated": "2026-02-04"
            },
            {
                "community": "Hengshan Garden",
                "address": "Hengshan Road 45, Xuhui District, Shanghai", 
                "price": 15000,
                "unit": "monthly_rent",
                "bedrooms": 3,
                "bathrooms": 2,
                "size_sqm": 120,
                "floor": "12/20",
                "orientation": "southwest",
                "year_built": 2015,
                "transportation": "Metro Line 1 - Hengshan Road Station (300m)",
                "property_type": "apartment",
                "last_updated": "2026-02-04"
            },
            {
                "community": "Jinjiang Community",
                "address": "Caoxi Road 67, Xuhui District, Shanghai",
                "price": 7200,
                "unit": "monthly_rent",
                "bedrooms": 1,
                "bathrooms": 1,
                "size_sqm": 50,
                "floor": "5/6",
                "orientation": "east",
                "year_built": 2005,
                "transportation": "Metro Line 4 - Caoxi Road Station (400m)",
                "property_type": "apartment", 
                "last_updated": "2026-02-04"
            }
        ]
        
        self.properties = sample_data
        return sample_data
    
    def save_data(self, format_type="both"):
        """
        Save collected data to file
        """
        if not self.properties:
            self.collect_data()
        
        if format_type == "json" or format_type == "both":
            with open('shanghai_xuhui_properties.json', 'w', encoding='utf-8') as f:
                json.dump(self.properties, f, ensure_ascii=False, indent=2)
        
        if format_type == "csv" or format_type == "both":
            df = pd.DataFrame(self.properties)
            df.to_csv('shanghai_xuhui_properties.csv', index=False, encoding='utf-8-sig')
        
        return f"Saved {len(self.properties)} properties to files"
    
    def get_summary(self):
        """
        Get a summary of collected data
        """
        if not self.properties:
            self.collect_data()
        
        total_properties = len(self.properties)
        avg_price = sum(p['price'] for p in self.properties) / len(self.properties) if self.properties else 0
        
        return {
            "district": self.district,
            "total_properties": total_properties,
            "average_price": round(avg_price, 2),
            "date_collected": datetime.now().strftime("%Y-%m-%d")
        }


def main():
    collector = REDC()
    data = collector.collect_data()
    collector.save_data()
    summary = collector.get_summary()
    
    print("REDC - Real Estate Data Collector")
    print(f"District: {summary['district']}")
    print(f"Properties collected: {summary['total_properties']}")
    print(f"Average price: ¥{summary['average_price']}/month")
    print("Files created: shanghai_xuhui_properties.json, shanghai_xuhui_properties.csv")


if __name__ == "__main__":
    main()