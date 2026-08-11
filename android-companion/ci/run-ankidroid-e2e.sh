#!/usr/bin/env bash
set -euo pipefail

adb install -r AnkiDroid-2.24.0.apk
adb root
adb wait-for-device

anki_data=/data/user/0/com.ichi2.anki
anki_uid=$(adb shell stat -c %u "$anki_data" | tr -d '\r')
test -n "$anki_uid"

adb shell mkdir -p "$anki_data/shared_prefs" "$anki_data/files/AnkiDroid"
printf '%s\n' \
  '<?xml version="1.0" encoding="utf-8" standalone="yes" ?>' \
  '<map>' \
  '  <string name="deckPath">/data/user/0/com.ichi2.anki/files/AnkiDroid</string>' \
  '</map>' \
  | adb shell "cat > $anki_data/shared_prefs/com.ichi2.anki_preferences.xml"
adb shell chown -R "$anki_uid:$anki_uid" "$anki_data"
adb shell restorecon -R "$anki_data"

adb install -r app/build/outputs/apk/debug/app-debug.apk
adb install -r app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk
adb shell pm grant \
  com.sodrius.nebli.companion \
  com.ichi2.anki.permission.READ_WRITE_DATABASE
adb shell am instrument -w -r \
  com.sodrius.nebli.companion.test/androidx.test.runner.AndroidJUnitRunner
