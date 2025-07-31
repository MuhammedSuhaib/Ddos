# Show List of Connected Wifi devices
Run these in `cmd` as admin 

To Show List of connected devices
```bash
netsh wlan show profiles
```

To remove each with name:

```bash
netsh wlan delete profile name="PROFILE_NAME"
```

Or delete all at once:

```bash
netsh wlan delete profile name=*
```

That’ll clear all Wi-Fi networks saved on your PC.
