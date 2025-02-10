import webbrowser

def open_link(choice):
    links = {
        "1": "https://chatgpt.com",
        "2": "https://quizizz.com/join",
        "3": "https://github.com/zigoo0/webpwn3r",
        "4": "https://github.com/sqlmapproject/sqlmap",
        "5": "https://github.com/rapid7/metasploit-framework",
        "6": "https://github.com/zaproxy/zaproxy"
       
      
    }
    
    if choice in links:
        webbrowser.open(links[choice])
    else:
        print("Pilihan tidak valid!")

def main():
    while True:
        print("\nMenu Link:")
        print("1. AI Tool")
        print("2. Gamification")
        print("3. Scanner Tool")
        print("4. Pentest Tool")
        print("5. Framework Security Tool")
        print("6. Web Scanner")
        print("7. Exit")
        
        choice = input("Pilih nomor: ")
        
        if choice == "7":
            print("Keluar dari program")
            break
        else:
            open_link(choice)

if __name__ == "__main__":
    main()
