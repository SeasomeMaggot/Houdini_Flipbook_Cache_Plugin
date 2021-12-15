# Houdini Flipbook Cache Plugin

---------------------------------------------------------------
#This tool can automatic create multiple flipbooks based on changes of one or more parameters in Houdini.

#To install, just copy the script to a new tool on the shelf in Houdini.

#Copy and parameter before click the tool button.

#This tool support multipule parameter channels. Use vector input for multi channels. Make sure the length of vector inputs matchs the channel quantity. 

#You can choose to generate file cache nodes. 

#This tool can also create multi MPlay preview renders based on change of one or more parameters, currently this function supports Mantra and Arnold.

#Select Channel:

#To use it, you first need to copy the parameter of a channel, then, you hit the shelf tool button, and the UI will open. You can add other parameter by copy parameter of other channels and hit “Add” button. If you want to get rid of current parameter, just copy new parameter channel and hit “Refresh” button.

#Input Value and Create Flipbooks:

#You can input any type of value, int, float, or expression. You can set your own value separator. If you want to wedge multiple parameter channels, you should use “< >” bracket for you value list, and you can set your own bracket in case you have expression with “<” or “>” inside. Then you can hit the “Create Flipbook” to generate flipbooks.

#Cache to Disk:

#If you want to create cache while generating flipbooks, check the “Create File Cache” combo box, and select a node where you want to get the cache file, then hit the “Create Flipbook” to generate flipbooks. The file cache nodes will be separate from the node tree after flipbook finished, the node names are the parameter names plus values, you can change the file path and names, but it’s not recommended.

#Here is a video instruction in Chinese: https://vimeo.com/599835387

#bilibili instruction: https://www.bilibili.com/video/bv1Py4y1V7SP

----------------------------------------------------------------------------------------------------------------------
#Update Houdini 19: since Houdini 19 cancel file mode parm in file cache node, I use file node as a subsitution for creating flipbook with caching.
