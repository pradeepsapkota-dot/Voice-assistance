@echo off
echo --- Luffy Device Manager ---

:: 1. Clear old connections
adb disconnect

:: 2. Wait for USB Authorization
echo Please check your phone screen. 
echo If a popup appears, check "Always allow" and click OK.
adb wait-for-device
echo Device Authorized!

:: 3. Switch to Wireless Mode
echo Restarting ADB in Wireless Mode...
adb tcpip 5555
echo Waiting for ADB service to restart...
timeout 5

:: 4. Find ONLY the IPv4 address
:: The space after "inet " is CRITICAL to ignore IPv6
echo Searching for IPv4 address...
FOR /F "tokens=2" %%G IN ('adb shell ip addr show wlan0 ^| findstr /c:"inet "') DO set ipfull=%%G

:: 5. Strip the /24 prefix (e.g., 192.168.1.5/24 -> 192.168.1.5)
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G

:: 6. Check if we actually got a valid IP
if "%ip%"=="" (
    echo [ERROR] Could not find IPv4. 
    echo Checking secondary interface...
    FOR /F "tokens=2" %%G IN ('adb shell ip addr show eth0 ^| findstr /c:"inet "') DO set ipfull=%%G
    FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G
)

if "%ip%"=="" (
    echo [FATAL ERROR] No IP found. Ensure Wi-Fi is ON.
    pause
    exit /b
)

:: 7. Final Connection
echo Connecting to %ip%...
adb connect %ip%:5555

echo.
echo ------------------------------------------
echo Status:
adb devices
echo ------------------------------------------
echo You can now unplug the USB cable.
timeout 5