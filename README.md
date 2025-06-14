# 	**TMJC_Adw1re**
A simple adware project that I decide to give it a try as a way to practice my coding skills and understanding. No I was not threatened by
Tampines Meridian Junior College to make this adware for them.

# **Weaknesses**
- Can be detected by default windows 11 defender if you scan the app
- Has no ofuscation (Too LAZY to use PYARMOR to ofuscate)
- Functions are generic
- No rootkits function
- Code breaks if internet is off (Semi-Immortality traits)
- Persistance is generic, set at generic locations
- May run into errors due to multiple QApplication instances

## **Changelog**
14/06/2025:
+ Semi-Immortal traits
+ Calculator App launches from the 1st app
+ Maintain persistance through Windows Registry Key

## **Functions**
When the app is clicked, there will be a buffer before adwindows pop up. A download process will run, which will download 3 adware.exe into 3 
seperate directories and auto.run them. 3 seperate Windows Registry Keys will also be logged into windows startup. After download finishes,
5 ad-windows pop up alongside a calculator app and the 3 other auto.run instances. NOTE: The downloaded adware have similar functions to main
adware.exe just without the calculator app.

This will create a semi-immortal state, where even if you delete one adware.exe the others will redownload it back. Even if Windows Registry
Key is deleted, it root app aka the adware.exe is not deleted it will re-establish itself back into the registry.

# *Windows Registry Locations:*
- Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

# *Downloaded paths:*
- C:\Users\ (YOUR_USERNAME) \Pictures\Screenshots
- C:\Users\ (YOUR_USERNAME) \Saved Games
- C:\Users\ (YOUR_USERNAME) \Favourites

