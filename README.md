# VRED-autoGenerateHTMLOverlay

## Use this script to auto create an HTML Overlay based our your Variant Sets in your scene

Do you want to inprove the Usabilty of your VRED scene? Do you want to give direct access to most important Variant Sets?
You have no idea how to use HTML or pyhton? ;)

This script will help you to automatically create a sceneplate with thumbnails of all your Variant Sets on scene. 
As the Thumbnails are stored in BASE64 Format, the HTML can be inlined in your VPB. In easy words: 
The HTML will be generated and stored with all information in your VRED file.

Enjoy

How to use:
- (optional) Export the Variants of your scene. File - Export Scene Data - Variants
- Remove the Variants from your Variant Set Module that you do not need in your overlay.
- Create a Preview for each Variant Set. Right Click on the Variant Set - Create Preview - Standard Quality
- Paste the Scene in the Script Editor of VRED and press run
- (optional) Export a VRED GO file. The Overlays are included.


Known Limitations: If the Sceneplate Editor is open, the performance is slow. Make sure to close it.
