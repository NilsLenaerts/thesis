adb shell "su -c cp /data/data/com.android.chrome/app_chrome/Default/History /sdcard/tmp/History"
adb pull /sdcard/tmp/History
sqlitebrowser History
