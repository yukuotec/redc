#!/usr/bin/env python3
"""
REDC - Real Estate Data Collector
Entry point for Shanghai Xuhui District property data collection
"""

from redc.core import REDC


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