#
# Copyright (C) 2024 by Rishav
# RishavMusicBot - Rebranded & Restyled
#

HELP_1 = """🎛️ **<u>Admin Commands:</u>**

📌 **c** = channel play prefix

⏸️ /pause or /cpause — Pause the music.
▶️ /resume or /cresume — Resume paused music.
🔇 /mute or /cmute — Mute the music.
🔊 /unmute or /cunmute — Unmute the music.
⏭️ /skip or /cskip — Skip current track.
⏹️ /stop or /cstop — Stop and clear queue.
🔀 /shuffle or /cshuffle — Shuffle the queue.
⏩ /seek or /cseek — Forward seek by duration.
⏪ /seekback or /cseekback — Backward seek.
🔄 /restart — Restart bot for your chat.

━━━━━━━━━━━━━━━━━━━━━━
🔢 **<u>Specific Skip:</u>**
/skip [Number] — Skip to a specific track in queue.
Example: `/skip 3` skips to the 3rd track.

━━━━━━━━━━━━━━━━━━━━━━
🔁 **<u>Loop Play:</u>**
/loop [enable/disable] or [1-10]
Loops the current track 1-10 times. Default: 10.

━━━━━━━━━━━━━━━━━━━━━━
👥 **<u>Auth Users:</u>**
Auth Users can use admin commands without being an admin.

/auth [Username] — Add user to AUTH LIST.
/unauth [Username] — Remove user from AUTH LIST.
/authusers — View AUTH LIST."""


HELP_2 = """🎵 **<u>Play Commands:</u>**

Available: `play`, `vplay`, `cplay`
ForcePlay: `playforce`, `vplayforce`, `cplayforce`

📌 **c** = channel play | **v** = video | **force** = skip queue

▶️ /play or /vplay or /cplay
— Play a song or stream a live link on voice chat.

⚡ /playforce or /vplayforce or /cplayforce
— **Force Play:** Instantly plays searched track, skipping current.

📡 /channelplay [username/id or Disable]
— Connect a channel and stream from your group.

━━━━━━━━━━━━━━━━━━━━━━
💾 **<u>Server Playlists:</u>**
/playlist — View your saved playlists.
/deleteplaylist — Delete a saved track.
/play — Start playing your saved playlist."""


HELP_3 = """🤖 **<u>Bot Commands:</u>**

📊 /stats — Get Top 10 Global Stats, Top Users, Top Chats, etc.

🛡️ /sudolist — Check Sudo Users of **Rishav Music**

🎤 /lyrics [Music Name] — Search lyrics for any track online.

🎵 /song [Track Name or YT Link] — Download track as MP3/MP4.

🎛️ /player — Open an interactive Playing Panel.

📌 **c** = channel play

📋 /queue or /cqueue — View the current music queue."""


HELP_4 = """⚙️ **<u>Extra Commands:</u>**
/start — Start Rishav Music Bot.
/help — Open Commands Help Menu.
/ping — Ping bot & check RAM, CPU stats.

━━━━━━━━━━━━━━━━━━━━━━
🔧 **<u>Group Settings:</u>**
/settings — Open full group settings panel.

🔗 **Settings Options:**

1️⃣ **Audio Quality** — Set stream audio quality.
2️⃣ **Video Quality** — Set stream video quality.
3️⃣ **Auth Users** — Toggle admin commands: Everyone or Admins Only.
4️⃣ **Clean Mode** — Auto-delete bot messages after 5 mins.
5️⃣ **Command Clean** — Auto-delete played commands instantly.
6️⃣ **Play Settings** — Full play mode configuration.

━━━━━━━━━━━━━━━━━━━━━━
🎮 **<u>Playmode Options:</u>**
/playmode — Open play settings panel.

1️⃣ **Search Mode** [Direct/Inline]
2️⃣ **Admin Commands** [Everyone/Admins]
3️⃣ **Play Type** [Everyone/Admins]"""

HELP_5 = """👑 **<u>SUDO USER MANAGEMENT:</u>**
/addsudo [Username or Reply]
/delsudo [Username or Reply]

━━━━━━━━━━━━━━━━━━━━━━
🌐 **<u>HEROKU:</u>**
/usage — Check Dyno Usage.
/get_var — Get a config var.
/del_var — Delete a config var.
/set_var [Name] [Value] — Set or update a var.

━━━━━━━━━━━━━━━━━━━━━━
🤖 **<u>BOT CONTROL:</u>**
/reboot — Reboot the bot.
/update — Update the bot.
/speedtest — Check server speed.
/maintenance [enable/disable]
/logger [enable/disable] — Log searched queries.
/get_log [Lines] — Get bot logs from Heroku or VPS.
/autoend [enable/disable] — Auto-end stream after 3 mins.

━━━━━━━━━━━━━━━━━━━━━━
📊 **<u>STATS:</u>**
/activevoice — Active voice chats.
/activevideo — Active video calls.
/stats — Bot statistics.

━━━━━━━━━━━━━━━━━━━━━━
⛔ **<u>BLACKLIST CHAT:</u>**
/blacklistchat [ID] — Blacklist a chat.
/whitelistchat [ID] — Whitelist a chat.
/blacklistedchat — View all blacklisted chats.

━━━━━━━━━━━━━━━━━━━━━━
🚫 **<u>BLOCK USERS:</u>**
/block [Username/Reply] — Block a user.
/unblock [Username/Reply] — Unblock a user.
/blockedusers — View blocked users.

━━━━━━━━━━━━━━━━━━━━━━
🔨 **<u>GBAN:</u>**
/gban [Username/Reply] — Ban user from all served chats.
/ungban [Username/Reply] — Remove from gban list.
/gbannedusers — View gbanned users.

━━━━━━━━━━━━━━━━━━━━━━
🎥 **<u>VIDEO CALLS:</u>**
/set_video_limit [Number] — Max chats for video calls. Default: 3.
/videomode [download/m3u8] — Set video stream mode.

━━━━━━━━━━━━━━━━━━━━━━
🔐 **<u>PRIVATE BOT MODE:</u>**
/authorize [CHAT_ID] — Allow a chat to use the bot.
/unauthorize [CHAT_ID] — Disallow a chat.
/authorized — Check all allowed chats.

━━━━━━━━━━━━━━━━━━━━━━
📢 **<u>BROADCAST:</u>**
/broadcast [Message or Reply] — Broadcast to served chats.

**Options:**
`-pin` — Pin message
`-pinloud` — Pin with loud notification
`-user` — Broadcast to users
`-assistant` — Broadcast from assistant account
`-nobot` — Skip bot broadcast

**Example:** `/broadcast -user -assistant -pin Hello!`
"""
