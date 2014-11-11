# Wall-E
## About
Show random wallpapers under Linux, using photos uploaded by one Google+ user.
Uses the Picasa Web API to fetch, and feh to display the images.

## Setup
1. install
  * python2
  * feh
  * python-configobj
  * google data python lib v1
2. clone the repo
3. add your login details, the user from which to load the photos, and a default wallpaper in the ``config`` file
4. schedule loading the next brackground, e.g. via crontab every 5 minutes
   ```
   */5 * * * *     cd <path-to-cloned-repo>; ./run.py
   ```
5. optionally add an emergency hotkey to display default image and start loading next background, e.g. with i3 window manager
   ```
   bindsym Control+Return exec --no-startup-id "cd <path-to-cloned-repo>; ./emergency-run.sh"
   ```

## Tips
You can use the same account for both user logins that have to be specified in ``config``.
But if you want to control which albums and pictures are used for your background,
consider creating a second Google+ user, and sharing only such pictures that you
want to see as wallpapers with that user. Use the login information for this user for
the first two fields in the config file, and your primary user email for the third field.
