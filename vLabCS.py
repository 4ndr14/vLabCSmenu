import webbrowser

def open_link(choice):
    links = {
        "1": "https://chatgpt.com",
        "2": "https://github.com/sqlmapproject/sqlmap",
        "3": "https://quizizz.com/join"
      
    }
    
    if choice in links:
        webbrowser.open(links[choice])
    else:
        print("Pilihan tidak valid!")

def main():
    while True:
        print("\nMenu Tautan Web:")
        print("1. AI")
        print("2. Tools Pentest")
        print("3. Gamifikasi")
        print("4. Keluar")
        
        choice = input("Pilih nomor situs web yang ingin dibuka: ")
        
        if choice == "4":
            print("Keluar dari program.")
            break
        else:
            open_link(choice)

if __name__ == "__main__":
    main()
