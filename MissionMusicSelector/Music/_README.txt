MissionMusicSelector -- custom Mech Lab music
============================================

Drop audio files in this folder, then pick one in
    Settings > Audio > MECH LAB THEME

Supported: .ogg  .wav  .mp3
  .ogg and .wav are decoded by Unity directly and are the safest choice.
  .mp3 relies on Unity's MPEG support; if a file fails to load it is
  reported in MissionMusicSelector.log -- convert it to .ogg and retry.

Subfolders are scanned too. The dropdown shows each file name without its
extension. The selected track loops for as long as you are in the Mech Bay,
and the game's own Mech Bay music is silenced while it plays.

Volume follows the in-game MUSIC and MASTER VOLUME sliders.

New files are picked up when the game starts. To rescan without restarting,
reopen the Settings > Audio panel.
