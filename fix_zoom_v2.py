import os
import re

base_dir = '/Users/kirkspencer/Documents/kirkspencersite'
ventures_path = os.path.join(base_dir, 'ventures.html')

with open(ventures_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the previous zoom fix I added (the .top, .main... zoom: 0.5 block)
content = re.sub(r'<style>\s*/\* Zoom everything EXCEPT.*?</style>', '', content, flags=re.DOTALL)

# We want to wrap all content AFTER the background video in a scaled wrapper that stays centered.
# The video is: <video ... src="./assets_archive/assets/background_video.mp4" ...></video>
# We will inject `<div class="scale-wrapper">` right after the video, and `</div>` right before `</body>`.

scale_css = """
<style>
  /* 
   We wrap the entire content in a 200% sized container, and then scale it down by 50%.
   This creates a perfectly centered, 50% zoomed-out layout, while the background video
   remains fully untouched and full-screen in the background! 
  */
  .scale-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    transform: scale(0.5);
    transform-origin: top left;
  }
  
  /* Fix fixed elements inside the scaled wrapper so they behave correctly */
  .scale-wrapper .top, 
  .scale-wrapper .foot, 
  .scale-wrapper .clock,
  .scale-wrapper .grid-overlay,
  .scale-wrapper .baseline-rows {
    position: absolute; /* transforms create a new containing block for fixed elements anyway */
  }
</style>
"""

# Add the CSS
content = content.replace('</head>', scale_css + '</head>')

# Wrap the content
# Find the video end tag
video_end = '</video>'
if video_end in content:
    parts = content.split(video_end, 1)
    content = parts[0] + video_end + '\n<div class="scale-wrapper">\n' + parts[1]
    
    # Close the wrapper before body ends
    content = content.replace('</body>', '\n</div>\n</body>')

with open(ventures_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ventures zoom fixed with scale-wrapper.")
