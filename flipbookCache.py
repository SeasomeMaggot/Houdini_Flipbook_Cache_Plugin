import hou
import toolutils
import re

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(844, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setIndent(12)

        self.horizontalLayout_5.addWidget(self.label)

        self.AddButton = QPushButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")

        self.horizontalLayout_5.addWidget(self.AddButton)

        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout_5.addWidget(self.refreshButton)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_S = QLineEdit(self.centralwidget)
        self.lineEdit_S.setObjectName(u"lineEdit_S")
        self.lineEdit_S.setEnabled(True)
        self.lineEdit_S.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_S)

        self.lineEdit_E = QLineEdit(self.centralwidget)
        self.lineEdit_E.setObjectName(u"lineEdit_E")
        self.lineEdit_E.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_E)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.sepText = QLineEdit(self.groupBox)
        self.sepText.setObjectName(u"sepText")
        self.sepText.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.sepText)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.bracketL = QLineEdit(self.groupBox)
        self.bracketL.setObjectName(u"bracketL")
        self.bracketL.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.bracketL)

        self.bracketR = QLineEdit(self.groupBox)
        self.bracketR.setObjectName(u"bracketR")
        self.bracketR.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.bracketR)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.cacheModeButton = QCheckBox(self.centralwidget)
        self.cacheModeButton.setObjectName(u"cacheModeButton")

        self.horizontalLayout_3.addWidget(self.cacheModeButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.fileCacheGroup = QGroupBox(self.centralwidget)
        self.fileCacheGroup.setObjectName(u"fileCacheGroup")
        self.horizontalLayout_2 = QHBoxLayout(self.fileCacheGroup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 25, 9, 9)
        self.lineEdit = QLineEdit(self.fileCacheGroup)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.fileCacheGroup)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_Index = QLineEdit(self.fileCacheGroup)
        self.lineEdit_Index.setObjectName(u"lineEdit_Index")
        self.lineEdit_Index.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_Index)

        self.formatBox = QComboBox(self.fileCacheGroup)
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.formatBox)

        self.horizontalLayout_2.setStretch(0, 19)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_2.addWidget(self.fileCacheGroup)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")

        self.verticalLayout.addWidget(self.createButton)

        self.renderButton = QPushButton(self.centralwidget)
        self.renderButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.renderButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    #!!!  ^^^  setupUi from Qt Designer

        self.createButton.clicked.connect(self.funcWork)
        self.refreshButton.clicked.connect(self.updateLabel)
        self.AddButton.clicked.connect(self.addChanList)
        self.renderButton.clicked.connect(self.renderMPlay)

        self.cacheModeButton.stateChanged.connect(self._handleCheckboxStateChange)
        self.lineEdit.setDisabled(True)
        self.lineEdit_Index.setDisabled(True)
        self.formatBox.setDisabled(True)

    def _handleCheckboxStateChange(self, state):
        self.lineEdit.setEnabled(state == QtCore.Qt.Checked)
        self.lineEdit_Index.setEnabled(state == QtCore.Qt.Checked)
        self.formatBox.setEnabled(state == QtCore.Qt.Checked)
        if state != QtCore.Qt.Checked:
            self.lineEdit.setEnabled(QtCore.Qt.Unchecked)
            self.lineEdit_Index.setEnabled(QtCore.Qt.Unchecked)
            self.formatBox.setEnabled(QtCore.Qt.Unchecked)
    #!!! ^^^  UI connection

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flipbook Cache", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please copy a parameter", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Frame Range", None))
        self.lineEdit_S.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$RFSTART", None))
        self.lineEdit_E.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$RFEND", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters List", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Separator", None))
        self.sepText.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vector Bracket", None))
        self.bracketL.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.bracketR.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"support float, int, and expression value", None))
        self.cacheModeButton.setText(
            QCoreApplication.translate("MainWindow", u"Create Cache File  (Select a parent node before hit the button)",
                                       None))
        self.fileCacheGroup.setTitle(QCoreApplication.translate("MainWindow", u"Cache Path", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"$HIP/testGeo/$OS", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$HIP/testGeo/$OS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u".ParmVal.", None))
        self.lineEdit_Index.setText(QCoreApplication.translate("MainWindow", u"$F", None))
        self.lineEdit_Index.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$F4", None))
        self.formatBox.setItemText(0, QCoreApplication.translate("MainWindow", u".bgeo.sc", None))
        self.formatBox.setItemText(1, QCoreApplication.translate("MainWindow", u".bgeo", None))
        self.formatBox.setItemText(2, QCoreApplication.translate("MainWindow", u".vdb", None))

        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create Flipbook", None))
        self.renderButton.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        #  ^^^ from Qt Designer


        self.updateLabel()
        #  ^^^ updating Label

    def updateLabel(self):
        del self.channelList[:]
        UIchanPath = ""
        chanPath = self.expChanList()
        for chanExp in chanPath:
            self.channelList.append(chanExp)
        for chanLine in chanPath:
            UIchanPath += chanLine + "\n"
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Target Channel: \n" + UIchanPath, None))

    def addChanList(self):
        UIchanPath = ""
        chanPath = self.expChanList()
        print(self.channelList)
        setCP = set(chanPath)
        setCL = set(self.channelList)
        if not setCP.issubset(setCL):
            for chanItem in chanPath:
                if chanItem not in self.channelList:
                    self.channelList.append(chanItem)

        print(self.channelList)
        for chanLine in self.channelList:
            UIchanPath += chanLine + "\n"
        self.label.setText(
                QCoreApplication.translate("MainWindow", "Target Channel: \n" + UIchanPath, None))

    #  ^^^ selected node only mode for non-geo node type


    # retranslateUi

    #!!! ^^^ UI
    #-----------------------------------------------------------------------------------
    channelList = []
    # initialize a list to store all the channels

    def expChanList(self):
        if hou.parmClipboardContents() == ():
            raise hou.Error("Copy the parameter first!!!")
        else:
            chanPath = []
            for n in hou.parmClipboardContents():
                CP = n['path']
                chanPath.append(CP)
                # get channel path from Parm clipboard
        return chanPath

    def getHouVal(self):
        chanPath = self.channelList
        parmName = []
        nodeName = []
        for CP in chanPath:
            PN = CP.split("/")[-1]
            parmName.append(PN)
            # get parm Name and add them into list
            removeName = "/" + PN
            NN = CP.replace(removeName, "")
            nodeName.append(NN)
            # get Node name from the Parm channel path

        hipFileName = hou.hipFile.path().split("/")[-1]
        hipPath = hou.hipFile.path().replace(hipFileName, "")
        # get $HIP path
        return chanPath, parmName, nodeName, hipPath

    def getInputValue(self):
        InputValueTest = self.textEdit.toPlainText()
        if InputValueTest == '':
            QMessageBox.about(self.centralwidget, "Horrible Error!",
                              "Add at least one value in the Parameter List!!!")
            # check if value input exists
        else:
            braL = self.bracketL.text()
            if braL == "":
                braL = "<"
            braR = self.bracketR.text()
            if braR == "":
                braR = ">"
            sepName = self.sepText.text()  # get separator from UI input
            if sepName == "":
                sepName = ","

            if braL in InputValueTest and braR in InputValueTest:
                vecList = []
                partVal = InputValueTest.split(braL)
                for fullVal in partVal:
                    if fullVal == "":
                        pass
                    else:
                        vecList.append(fullVal.split(braR))
                for n in vecList:
                    try:
                        n.remove(sepName)
                    except:
                        n.remove('')
                InputValue = vecList
                # get vector input list
                # if len(InputValue[0].split(self.sepText.text())) != len(self.channelList):
                #     QMessageBox.about(self.centralwidget, "Horrible Error!",
                #                       "Input vector length does not match channel quantity!!!")

            else:
                InputValue = InputValueTest.split(sepName)
            # get non-vector input list

            return InputValue
            #  ^^^ get values from UI input

    def getFormat(self):
        index = self.formatBox.currentIndex()
        cacheFormat = self.formatBox.itemText(index)
        return cacheFormat
    # get cache format from UI import

    def getPath(self):
        path = self.lineEdit.text()
        if path != '':
            return str(path) + "."
        else:
            return "$HIP/testGeo/$OS."
        # get path from UI input

    def getFrameRange(self):
        if self.lineEdit_S.text() != '':
            startF = int(self.lineEdit_S.text())
            endF = int(self.lineEdit_E.text())
        else:
            startF = int(hou.expandString("$RFSTART"))
            endF = int(hou.expandString("$RFEND"))
        return startF,endF
    # get frame range from UI input

    #!!!  ^^^   function for getting all input value from Houdini and UI
    #------------------------------------------------------------------------------------------------------------------
    def makeRender(self, num, getInputValue):
        if isinstance(getInputValue, list):
            inputValue = getInputValue[0].split(self.sepText.text())
        chanPath = self.getHouVal()[0]
        parmName = self.getHouVal()[1]
        nodeName = self.getHouVal()[2]
        if len(getInputValue) != len(chanPath):
            QMessageBox.about(self.centralwidget, "Horrible Error!",
                              "Vector length MUST match channel length!!!")
        for n in range(len(chanPath)):  # loop the input value to node parm
            try:
                hou.node(nodeName[n]).parm(parmName[n]).deleteAllKeyframes()
                hou.node(nodeName[n]).setParms({parmName[n]: inputValue[n]})  # set Parm
            except:
                hou.node(nodeName[n]).parm(parmName[n]).deleteAllKeyframes()
                hou.node(nodeName[n]).setParmExpressions({parmName[n]: inputValue[n]})  # set Expr

        try:
            hou.selectedNodes()[0].type().name()
            if hou.selectedNodes()[0].type().name() == "ifd": # check if render node is selected
                renderNode = hou.selectedNodes()[0]
                renderNode.parm("renderpreview").pressButton() # render to MPlay
            elif hou.selectedNodes()[0].type().name() == "arnold":
                renderNode = hou.selectedNodes()[0]
                renderNode.setParms({"ar_picture":"ip",})
                renderNode.parm("execute").pressButton()
            else:
                QMessageBox.about(self.centralwidget, "Horrible Error!",
                                  "Only support Mantra or Arnold node!!!")
        except:
            QMessageBox.about(self.centralwidget, "Horrible Error!",
                      "Only support Mantra or Arnold node!!!")

    def makeFilpbook(self,num,getInputValue):
        def changeVar(inputValue):
            if isinstance(getInputValue,list):
                inputValue = getInputValue[0].split(self.sepText.text())
            chanPath = self.getHouVal()[0]
            parmName = self.getHouVal()[1]
            nodeName = self.getHouVal()[2]

            if len(getInputValue) != len(chanPath):
                QMessageBox.about(self.centralwidget, "Horrible Error!",
                                  "Vector length MUST match channel length!!!")

            startF = self.getFrameRange()[0]
            endF = self.getFrameRange()[1]

            for n in range(len(chanPath)):# loop the input value to node parm
                try:
                    hou.node(nodeName[n]).parm(parmName[n]).deleteAllKeyframes()
                    hou.node(nodeName[n]).setParms({parmName[n]: inputValue[n]})  # set Parm
                except:
                    hou.node(nodeName[n]).parm(parmName[n]).deleteAllKeyframes()
                    hou.node(nodeName[n]).setParmExpressions({parmName[n]: inputValue[n]})  # set Expr
            return chanPath,parmName,startF,endF
        funcVar = changeVar(getInputValue)

        flipbookSettingStash = toolutils.sceneViewer().flipbookSettings().stash()
        flipbookSettingStash.sessionLabel(funcVar[1][0] + str(num))
        flipbookSettingStash.frameRange((funcVar[2], funcVar[3]))
        toolutils.sceneViewer().flipbook(settings = flipbookSettingStash)


    def renderMPlay(self):
        InputValue = self.getInputValue()
        if InputValue is not None:
            for num, inputValue in enumerate(InputValue):
                self.makeRender(num,inputValue)
    #!!!  ^^^  Render image

    def noCache(self):
        InputValue = self.getInputValue()
        if InputValue is not None:
            for num, inputValue in enumerate(InputValue):
                self.makeFilpbook(num,inputValue)
    #!!!  ^^^  create flipbook without caching

    def createCache(self):
        InputValue = self.getInputValue()
        cacheFormat = self.getFormat()
        startF = self.getFrameRange()[0]
        endF = self.getFrameRange()[1]

        parmName = self.getHouVal()[1][0]
        nodeName = self.getHouVal()[2][0]

        versionNum = ".v001"
        #!!!  ^^^ get all the value from UI

        try:
            selectedNode = hou.selectedNodes()[0]
        except:
            selectedNode = None

        if InputValue is not None:
            for num, inputValueList in enumerate(InputValue):
                if isinstance(inputValueList,list): # check if input is vector
                    inputValue = ""
                    for k in inputValueList:
                        inputValue += k # convert list input values to string
                    inputValue = inputValue.replace(",","_")
                else:
                    inputValue = inputValueList

                index = self.lineEdit_Index.text()
                RelPath = self.getPath()

                if len(hou.selectedNodes()) != 1:
                    QMessageBox.about(self.centralwidget, "Horrible Error!",
                                      "Select ONE node as cache node's parent!!!")
                    break

                displayNode = hou.selectedNodes()[0].parent().displayNode()
                try: #  test if input value is expression
                    # float(inputValue)
                    relPath = RelPath + "IS" + str(inputValue) + "." + index + cacheFormat
                    FileNode = hou.node(selectedNode.parent().path() + "/FC" + nodeName.replace("/","").replace("obj","") + "."  + parmName + "." + str(inputValue) + versionNum) # get previous file cache node
                    if FileNode is None:# check if file cache Nodes are existed && create file cache node
                        fileNode = selectedNode.parent().createNode("filecache", "FC" + nodeName.replace("/","").replace("obj","") + "." + parmName + "." + str(inputValue) + versionNum) # create file cache node
                        # check if file cache Nodes are existed && create file cache node
                        fileNode.setParms({"file": relPath})
                        # fileNode.parm("f1").deleteAllKeyframes()
                        # fileNode.parm("f2").deleteAllKeyframes()
                        # fileNode.setParms({"f1": startF, "f2": endF})
                    else:
                        fileNode = FileNode # use existed file cache node
                        fileNode.setParms({"file": relPath})
                        # fileNode.parm("f1").deleteAllKeyframes()
                        # fileNode.parm("f2").deleteAllKeyframes()
                        # fileNode.setParms({"f1": startF, "f2": endF})
                except: # change node names if input value is expression
                    expValue = "Expr" + str(num)
                    relPath = RelPath + "IS" + expValue + "." + index + cacheFormat
                    FileNode = hou.node(
                        selectedNode.parent().path() + "/FC" + nodeName.replace("/", "").replace("obj",
                                                                                                                 "") + "." + parmName + "." + str(
                            expValue) + versionNum)  # get previous file cache node
                    if FileNode is None: # check if file cache Nodes are existed && create file cache node
                        fileNode = selectedNode.parent().createNode("filecache","FC" + nodeName.replace("/", "").replace("obj","") + "." + parmName + "." + str(expValue) + versionNum)
                        # create file cache node
                        fileNode.setParms({"file": relPath})
                        # fileNode.parm("f1").deleteAllKeyframes()
                        # fileNode.parm("f2").deleteAllKeyframes()
                        # fileNode.setParms({"f1": startF, "f2": endF})
                    else:
                        fileNode = FileNode # use existed file cache node
                        fileNode.setParms({"file": relPath})

                        # fileNode.parm("f1").deleteAllKeyframes()
                        # fileNode.parm("f2").deleteAllKeyframes()
                        # fileNode.setParms({"f1": startF, "f2": endF})
                        # set file cache node frame range

                if len(hou.selectedNodes()) != 1:
                    QMessageBox.about(self.centralwidget, "Horrible Error!",
                                      "Select ONE node as cache node's parent!!!")
                    break
                else:
                    childPath = selectedNode.outputs() # get output node of the selected node
                    if len(selectedNode.inputs()) < 2: # check if the selected node has no more than one I/O
                        for child in childPath:
                            inIndex = child.inputs().index(selectedNode) # finger out the index of input connects to the selected Node
                            hou.node(child.path()).setInput(inIndex,fileNode)  # connect all output nodes of selected node to file cache node

                        hou.node(fileNode.path()).setInput(0, selectedNode) # connect file cache node to selected node
                        fileNode.moveToGoodPosition()
                        fileNode.setParms({"filemode": 2}) # set file cache node to write mode

                        self.makeFilpbook(num,inputValueList)
                        displayNode.setDisplayFlag(1)  # set display flag back to output node for the next round of loop
                        fileNode.setParms({"filemode": 0})  # set file cache node to AUTO mode

                        for child in childPath:
                            inIndex = child.inputs().index(fileNode) # finger out the index of input which connects the file node
                            hou.node(child.path()).setInput(inIndex,selectedNode)  # connect all output nodes back to selected node

                        hou.node(fileNode.path()).setInput(0,None)  # break file cache node connection
                    else:
                        QMessageBox.about(self.centralwidget, "Horrible Error!",
                                          "Select a node with only ONE input !!!")
                        break
                #!!!  ^^^  create flipbooks based on the file cache node after selected node

    def funcWork(self):
        if self.cacheModeButton.isChecked() is True:
            self.createCache()
        else:
            self.noCache()

# ^^^ Main Function
#-----------------------------------------------------------------------------------------------------------------

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

mainw = MainWindow()
mainw.setWindowFlags(Qt.WindowStaysOnTopHint)
mainw.show()
