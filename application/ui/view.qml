import QtQuick 1.1

Rectangle {
    width: 800
    height: 480
    color: Qt.rgba(0.2,0.2,0.2,1)

    Rectangle {
        x: 60;
        y: 20;
        width: 283;
        height: 59;
        color: Qt.rgba(0.2,0.2,0.2,1)
        Image {   
            source: "img/logo.png"
        }
    }

    Text {
        font.family: "Helvetica";
        text: "CP200 LED COLOR VIEWER"
        color: Qt.rgba(1,1,1,1)
        font.pointSize: 12
        x: 550
        y: 440
    }

    Text {
        id: illuminant
        text: backend.illuminant
        color: "darkcyan"
        font.family: "Helvetica";
        font.pointSize: 56
        x: 120
        y: 100
        width: 200
        horizontalAlignment: Text.AlignRight
    }
    Text {
        id: power
        text: backend.power
        color: "darkcyan"
        font.family: "Helvetica";
        font.pointSize: 48
        x: 120
        y: 170
        width: 200
        horizontalAlignment: Text.AlignRight
    }

    Rectangle {
        id: onOffStatus
        width: 40
        height: 40
        x: 80
        y: 320
        color: backend.onOffStatus
        radius: 20
    }

    Rectangle {
        id: onoff
        width: 120
        height: 120
        x: 200
        y: 280
        color: Qt.rgba(0.4,0.4,0.4,1)
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.onoff()
            }
        }
    }

    Text {
        text: "ILLUMINANT"
        color: Qt.rgba(1,1,1,1)
        font.pointSize: 16
        font.family: "Helvetica";
        x: 400
        y: 240
    }

    Text {
        text: "POWER"
        color: Qt.rgba(1,1,1,1)
        font.pointSize: 16
        font.family: "Helvetica";
        x: 620
        y: 240
    }

    Rectangle {
        id: illuminantUp
        width: 120
        height: 120
        x: 400
        y: 100
        color: Qt.rgba(0.4,0.4,0.4,1)
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.upIlluminant()
            }
        }
        
    }

    Rectangle {
        id: powerUp
        width: 120
        height: 120
        x: 600
        y: 100
        color: Qt.rgba(0.4,0.4,0.4,1)
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.upPower()
            }
        }
    }

    Rectangle {
        id: illuminantDown
        width: 120
        height: 120
        x: 400
        y: 280
        color: Qt.rgba(0.4,0.4,0.4,1)
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.downIlluminant()
            }
        }
    }

    Rectangle {
        id: powerDown
        width: 120
        height: 120
        x: 600
        y: 280
        color: Qt.rgba(0.4,0.4,0.4,1)
        radius: 15
        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.downPower()
            }
        }
    }
}