import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("A_MIA_R3 GUI")

    Text {
        id: filelabel
        x: 42
        y: 45
        text: qsTr("Video File:")
        font.pixelSize: 16
    }
}
