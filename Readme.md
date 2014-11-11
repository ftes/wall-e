# Wall-E
## About
Show random wallpapers under Linux, using photos uploaded by one Google+ user.
Uses the Picasa Web API to fetch, and feh to display the images.

## Setup
1. clone the repo
2. add your login details, the user from which to load the photos, and a default wallpaper in the ``config`` file
3. schedule loading the next brackground, e.g. via crontab every 5 minutes
   ```
   */5 * * * *     cd <path-to-cloned-repo>; ./run.py
   ```
4. optionally add an emergency hotkey to display default image and start loading next background, e.g. with i3 window manager
   ```
   bindsym Control+Return exec --no-startup-id "cd <path-to-cloned-repo>; ./emergency-run.sh"
   ```
