import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("Data Extractor Project")
    print("======================")
    print("Select data source to display:")
    print("1. API (Weather)")
    print("2. Manual (CSV)")
    print("3. Sensor (Simulated)")
    print("4. Web Scraping")
    print("5. Excel File")
    print("6. CSV File")
    print("7. Text/Log File")
    print("8. JSON File")
    print("9. SQL Database")
    print("10. Image")
    print("11. Sound")
    print("12. IoT Simulation")
    print("13. Data Stream")
    
    choice = input("Enter choice (1-13): ")
    
    if choice == '1':
        from API import apiretrieve
        apiretrieve.fetch_weather_data()
    elif choice == '2':
        from Manual import manualretrive
        manualretrive.read_manual_data()
    elif choice == '3':
        from Sensor import sensorretrive
        sensorretrive.generate_sensor_data()
    elif choice == '4':
        from web_scrapping import scrapingcode
        scrapingcode.scrape_data()
    elif choice == '5':
        from Files import excel_retrieve
        excel_retrieve.read_excel_data()
    elif choice == '6':
        from Files import csv_retrieve
        csv_retrieve.read_csv_data()
    elif choice == '7':
        from Files import text_retrieve
        text_retrieve.read_text_data()
    elif choice == '8':
        from Files import json_retrieve
        json_retrieve.read_json_data()
    elif choice == '9':
        from Database import sql_retrieve
        sql_retrieve.read_sql_data()
    elif choice == '10':
        from Multimedia import image_retrieve
        image_retrieve.show_image()
    elif choice == '11':
        from Multimedia import sound_retrieve
        sound_retrieve.play_sound()
    elif choice == '12':
        from IoT_Streaming import iot_retrieve
        iot_retrieve.simulate_iot_device()
    elif choice == '13':
        from IoT_Streaming import stream_retrieve
        stream_retrieve.process_stream()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    # Fix for import issues when running from root
    sys.path.append(os.path.join(os.path.dirname(__file__), "Data Collection"))
    main()
