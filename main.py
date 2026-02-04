#!/usr/bin/env python3
"""
REDC - Real Estate Data Collector
Entry point for Shanghai Xuhui District property data collection
"""

from redc.core import REDC


def main():
    collector = REDC()
    data = collector.attempt_real_data_collection()
    collector.save_data()
    summary = collector.get_summary()
    
    print("\nREDC - Real Estate Data Collector")
    print(f"District: {summary['district']}")
    print(f"Properties collected: {summary['total_properties']}")
    print(f"Average price: ¥{summary['average_price']}/month")
    print(f"Data source: {summary['data_source']}")
    print("Files created: shanghai_xuhui_properties.json, shanghai_xuhui_properties.csv")
    
    if not collector.is_real_data:
        print("\n⚠ NOTE: This is SAMPLE (FAKE) data for testing purposes.")
        print("Real data collection would occur when anti-bot measures are addressed.")


if __name__ == "__main__":
    main()