# https://www.webfx.com/tools/emoji-cheat-sheet/

import emoji

print(emoji.emojize(":thumbs_up:"))
print(emoji.emojize(":star:"))

print(emoji.emojize(":thumbs_up: :star:"))

print(emoji.emojize("Sample text with emoji :star:"))

print(emoji.demojize("Sample text with emoji ⭐"))

print(emoji.emojize("One heart :red_heart:"))

print(emoji.emojize("Different heart :red_heart:",variant="emoji_type"))
