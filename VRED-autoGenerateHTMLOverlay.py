'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
Scripted by Simon Nagel

How to use:
- (optional) Export the Variants of your scene. File - Export Scene Data - Variants
- Remove the Variants from your Variant Set Module that you do not need in your overlay.
- Create a Preview for each Variant Set. Right Click on the Variant Set - Create Preview - Standard Quality
- Paste the Scene in the Script Editor of VRED and press run
- (optional) Export a VRED GO file. The Overlays are included.

'''
  



varSets = getVariantSets()

renderWindowSize = 1080
thumbnailSize = (renderWindowSize-8)/len(varSets)
fontSize = thumbnailSize/10

arrayButton =  []
arrayJsFunc =  []
arrayVarSet =  []
    
for i in range(len(varSets)):
    currentVarSet = varSets[i]
    varSetName = currentVarSet
    varSetPreviewBla = base64.b64encode(getVariantSetPreview(currentVarSet))
    varSetPreview = str(varSetPreviewBla)
    varSetPreview = varSetPreview[2:]
    varSetPreview = varSetPreview[:-1]


    jsFuncName = "f"+str(i)+"()"
    jsFuncPart1 = 'function '+jsFuncName+'{vred.executePython("value=selectVariantSet('
    jsFuncPart2 = varSetName
    jsFuncPart3 = ')"); };'
    jsFunc = jsFuncPart1+"'"+jsFuncPart2+"'"+jsFuncPart3
    button = '<button type="button" id="VP1" class="button1" onclick="'+jsFuncName+'" style="background-size: 100%; border-style: none; width: '+str(thumbnailSize+(thumbnailSize/32))+'px; height: '+str(thumbnailSize)+'px; color:white; font-size:'+str(fontSize)+'px; font-family: sans-serif; text-shadow: 1px 1px #000000; background-image: url(data:image/png;base64,'+str(varSetPreview)+');">'+varSetName+'</button><br>'

    arrayButton.append(button)
    arrayJsFunc.append(jsFunc)

buttons = ''.join(arrayButton)
jsFuncs = ''.join(arrayJsFunc)
varSetss =''.join(arrayVarSet)

url = '<html>\n<body>\n<div>\n'+buttons+' \n</div> \n<script>\n'+jsFuncs+'\n</script>\n</body>\n</html>'

#add URL to sceneplate
allSceneplates = vrSceneplateService.getAllSceneplates()

allSceneplates = vrSceneplateService.getAllSceneplates()

sceneplateToDelete = []
del sceneplateToDelete[:]


for i in range(len(allSceneplates)):
    sceneplateName = allSceneplates[i].getName()
    print sceneplateName[0:18]
    if sceneplateName[0:18] == "HTMLVariantOverlay":
         sceneplateToDelete.append(allSceneplates[i])

vrSceneplateService.removeNodes(sceneplateToDelete)

sceneplate = vrSceneplateService.createNode(vrSceneplateService.getRootNode(), vrSceneplateTypes.NodeType.Frontplate, "HTMLVariantOverlay")
sceneplate.setWidth(1920)
sceneplate.setHeight(1080)
sceneplate.setContentType(vrSceneplateTypes.ContentType.Web)
sceneplate.setSize(1)


sceneplate.setUrl(url)
vrSceneplateService.reloadWebPage([sceneplate])