#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtSerialPort/QtSerialPort>
#include <QMouseEvent>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void on_BTN_Haut_clicked();

    void on_BTN_Bas_clicked();

    void on_BTN_Droit_clicked();

    void on_comboBox_currentIndexChanged(const QString &arg1);

    void on_BTN_connecter_clicked();

    void on_BTN_Gauche_clicked();

    void on_BTN_Centre_clicked();

    void on_BTN_Manuel_clicked();

    void on_BTN_Wiimote_clicked();

    void on_BTN_Carre_clicked();

    void on_BTN_Losange_clicked();

    void on_BTN_Cercle_clicked();

    void on_BTN_Actualiser_clicked();

    void SerialRead();

    void on_BTN_Laser_ON_clicked();

    void on_BTN_Quitter_clicked();

private:
    Ui::MainWindow *ui;
    QSerialPort *serial;
    unsigned char i = 0;
    char mode = 'm';

};

#endif // MAINWINDOW_H
