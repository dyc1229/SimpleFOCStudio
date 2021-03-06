#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from gui.sharedcomponets import GUIToolKit
from gui.configureConnectionDialog import ConfigureSerailConnectionDialog

class ConnectionControlGroupBox(QtWidgets.QGroupBox):

    def __init__(self, parent=None,simpleFocConn=None):
        """Constructor for ToolsWidget"""
        super().__init__(parent)

        self.device = simpleFocConn

        self.setObjectName("generalControlGroupBox")
        self.setTitle("Connection control")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("generalControlHL")

        self.connectDisconnectButton = QtWidgets.QPushButton(self)
        self.connectDisconnectButton.setIcon(GUIToolKit.getIconByName("connect"))
        self.connectDisconnectButton.setObjectName("connectDeviceButton")
        self.connectDisconnectButton.setText("Connect")
        self.connectDisconnectButton.clicked.connect(self.connectDisconnectDeviceAction)

        self.horizontalLayout.addWidget(self.connectDisconnectButton)

        self.configureDeviceButton = QtWidgets.QPushButton(self)
        self.configureDeviceButton.setIcon(GUIToolKit.getIconByName("configure"))
        self.configureDeviceButton.setObjectName("configureDeviceButton")
        self.configureDeviceButton.setText("Configure")
        self.configureDeviceButton.clicked.connect(self.configureDeviceAction)
        self.horizontalLayout.addWidget(self.configureDeviceButton)

    def connectDisconnectDeviceAction(self):

        if self.device.isConnected:
            self.device.disConnect()
            self.connectDisconnectButton.setIcon(
                GUIToolKit.getIconByName("connect"))
            self.connectDisconnectButton.setText("Connect")

        else:
            hasBeenConnected  = self.device.connect()
            if hasBeenConnected:
                self.connectDisconnectButton.setIcon(
                    GUIToolKit.getIconByName("disconnect"))
                self.connectDisconnectButton.setText("Disconnect")


    def configureDeviceAction(self):
        dialog = ConfigureSerailConnectionDialog(self.device)
        result = dialog.exec_()
        if result:
            deviceConfig = dialog.getConfigValues()
            self.device.configureDevice(deviceConfig)
