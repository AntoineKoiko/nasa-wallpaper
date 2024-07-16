#!/bin/bash

echo -e "Cron job started at $(date)\n"
# This script is used to run the nasa-wallpaper.py script with cron
# It is necessary to set the DBUS_SESSION_BUS_ADDRESS environment variable not present in cron env
# PID=$(pgrep gnome-session)
# export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

# See: https://askubuntu.com/questions/742870/background-not-changing-using-gsettings-from-cron
REAL_UID=$(id --real --user)
PID=$(pgrep --euid $REAL_UID gnome-session | head -n 1)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2- | sed -e "s/\x0//g")

echo -e "DBUS_SESSION variable set to $DBUS_SESSION_BUS_ADDRESS\n"

absolute_path="/home/antoine/delivery/projet_perso/nasa-wallpaper"
venv_path="$absolute_path/.venv/bin/activate"
script_path="$absolute_path/nasa-wallpaper.py"

echo -e "Running script $script_path\n"
source "$venv_path" && python "$script_path"