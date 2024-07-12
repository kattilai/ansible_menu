#!/usr/bin/env bash

_SCREENTITLE="Ansible menu --- KESZ Condsulting Kft. (c)2024"
_DOMAIN="kesz.hu"

#dialog --backtitle "HEHE" --msgbox "Helo" 0 0
#dialog --backtitle "HEHE"  --title "IP cím bekérése" --yesno "Kérem adja meg a VM IP címét." 12 45 
#dialog --backtitle "HEHE"  --title "IP cím bekérése" --prgbox "ls -lha /" 12 66
#dialog --backtitle "HEHE"  --title "IP cím bekérése" --textbox testfile 12 45 

_DESTIPADDRESS() {
	_WINDOWMSG="Kérem adja meg a módosítani kivánt szerver IP címét."
	_TITLE="Kérem host IP címét."
	_DESTIP=$(dialog --backtitle "$_SCREENTITLE"  --title "IP cím bekérése" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)
}



NEWNETWORK() {
	_WINDOWMSG="Kérem adja meg a network címét."
	_NETWORK=$(dialog --backtitle "$_SCREENTITLE"  --title "$_TITLE" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)
	_WINDOWMSG="Kérem adja meg a host netmask-át."
	_NETMASK=$(dialog --backtitle "$_SCREENTITLE"  --title "$_TITLE" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)

	_WINDOWMSG="Kérem adja meg a hálózat broadcast címét."
	_BROADCAST=$(dialog --backtitle "$_SCREENTITLE"  --title "$_TITLE" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)
}
NEWIPDATAS() {
	_TITLE="A host új IP adatainak megadása"
	_WINDOWMSG="Kérem adja meg a host új IP címét."
	_NEWIP=$(dialog --backtitle "$_SCREENTITLE"  --title "$_TITLE" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)

}
NEWDNS() {
	_TITLE="A DNS név beállítása"
	_WINDOWM10SG="Kérem adja meg a host DNS nevét."
	_NEWDNS=$(dialog --backtitle "$_SCREENTITLE"  --title "$_TITLE" --inputbox "$_WINDOWMSG" 12 45 --output-fd 1)
	_FQDNS=$_NEWDNS"."$_DOMAIN
}
SELECTPACKAGES() {
	_TITLE="Ansible scriptek"
	_WINDOWMSG="Kérem válassza ki a futtatni kivánt Ansible scripteket."
	_SPACKAGES=$(dialog --backtitle "$SCREENTITLE"  --title "$_TITLE" --buildlist "$WINDOWMSG" 30 50 15 f1 "D_one" on f2 "D_two" off f3 "D_three" off --output-fd 1)
}
DATACHECK() {
	echo "test"
}

DESTIPADDRESS
NEWIPDATAS
NEWDNS
SELECTPACKAGES
clear
echo $_DESTIP
echo $_NEWIP
echo $_NETWORK
echo $_NETMASK
echo $_BROADCAST
echo $_NEWDNS
echo $_FQDNS 
echo $_SPACKAGES
