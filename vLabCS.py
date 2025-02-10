import webbrowser

def open_link(choice):
    links = {
        "1": "https://chatgpt.com",
        "2": "https://quizizz.com/join",
        "3": "https://github.com/zigoo0/webpwn3r",
        "4": "https://github.com/sqlmapproject/sqlmap",
        "5": "https://github.com/rapid7/metasploit-framework",
        "6": "https://github.com/zaproxy/zaproxy",
        "7": "https://quizizz.com/join"
      
    }
    
    if choice in links:
        webbrowser.open(links[choice])
    else:
        print("Pilihan tidak valid!")

def main():
    while True:
        print("\nMenu Tautan Web:")
        print("1. AI")
        print("2. Gamifikasi")
        print("3. Scanner Tools")
        print("4. Pentest Tools")
        print("5. Framework Security Tools")
        print("6. Web Scanner")
        print("7. Gamifikasi")
        print("8. Keluar")
        
        choice = input("Pilih nomor situs web yang ingin dibuka: ")
        
        if choice == "4":
            print("Keluar dari program.")
            break
        else:
            open_link(choice)

if __name__ == "__main__":
    main()
