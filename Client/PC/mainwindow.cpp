#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtSerialPort/QtSerialPort>
#include <QString>

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    on_BTN_Actualiser_clicked();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_BTN_Haut_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode == 'm')
    {
    serial->write("#COORDONNEE,V,ADD,+10\n\r");
    ui->TermTransmission->setText("#COORDONNEE,V,ADD,+10");
    }
}

void MainWindow::on_BTN_Bas_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode == 'm')
    {
    serial->write("#COORDONNEE,V,ADD,-10\n\r");
    ui->TermTransmission->setText("#COORDONNEE,V,ADD,-10");
    }
}

void MainWindow::on_BTN_Gauche_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode == 'm')
    {
    serial->write("#COORDONNEE,H,ADD,-10\n\r");
    ui->TermTransmission->setText("#COORDONNEE,H,ADD,-10");
    }
}

void MainWindow::on_BTN_Droit_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode == 'm')
    {
    serial->write("#COORDONNEE,H,ADD,+10\n\r");
    ui->TermTransmission->setText("#COORDONNEE,H,ADD,+10");
    }
}

void MainWindow::on_BTN_Centre_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode == 'm')
    {
        serial->write("#COORDONNEE,V,POS,+0\n\r");
        serial->write("#COORDONNEE,H,POS,+0\n\r");
        ui->TermTransmission->setText("#COORDONNEE,H,POS,0");
        ui->TermTransmission->setText("#COORDONNEE,V,POS,0");
    }
}

void MainWindow::on_comboBox_currentIndexChanged(const QString &arg1)
{
    serial->close();
    ui->label_etat_serie->setText("Deconnecté");
    ui->BTN_connecter->setText("Connecter");
}

void MainWindow::on_BTN_connecter_clicked()
{
    if (ui->BTN_connecter->text() == "Connecter")
    {
        serial = new QSerialPort;
        serial->setPortName(ui->comboBox->currentText());

        if (serial->open(QIODevice::ReadWrite))
        {
            serial->setBaudRate(QSerialPort::Baud115200);
            serial->setDataBits(QSerialPort::Data8);
            serial->setFlowControl(QSerialPort::NoFlowControl);
            serial->setParity(QSerialPort::NoParity);

            ui->label_etat_serie->setText("Connecté");
            ui->BTN_connecter->setText("Déconnecter");

            connect(serial,SIGNAL(readyRead()),this,SLOT(SerialRead()));
        }
    }
    else
    {
        serial->close();
        ui->BTN_connecter->setText("Connecter");
        ui->label_etat_serie->setText("Déconnecté");
    }
}

void MainWindow::on_BTN_Manuel_clicked()
{
    if (serial->isOpen() && serial->isWritable() && mode != 'm')
    {
        serial->write("#MODE,MANU\n\r");
        ui->TermTransmission->setText("#MODE,MANU");
        mode = 'm';
        ui->lineEdit_Mode->setText("MANU");
        ui->BTN_Wiimote->setText("Connecter");
    }
}

void MainWindow::on_BTN_Wiimote_clicked()
{
    if (ui->BTN_Wiimote->text() == "Connecter")
    {
        if (serial->isOpen() && serial->isWritable())
        {
            serial->write("#MODE,WII,ON\n\r");
            ui->TermTransmission->setText("#MODE,WII,ON");
            mode = 'w';
            ui->BTN_Wiimote->setText("Deconnecter");
            ui->lineEdit_Mode->setText("WII");
            ui->label_wii->setText("Appuyez sur 1+2");
        }
    }
    else
    {
        if (serial->isOpen() && serial->isWritable())
        {
            serial->write("#MODE,WII,OFF\n\r");
            ui->TermTransmission->setText("#MODE,WII,OFF");
            mode = 'm';
            ui->BTN_Wiimote->setText("Connecter");
            ui->lineEdit_Mode->setText("MANU");
            ui->label_wii->setText("Déconnecté");
        }
    }
}

void MainWindow::on_BTN_Carre_clicked()
{
    if (serial->isOpen() && serial->isWritable())
    {
        serial->write("#MODE,CARRE\n\r");
        ui->TermTransmission->setText("#MODE,CARRE");
        mode = 'a';
        ui->lineEdit_Mode->setText("AUTO");
        ui->BTN_Wiimote->setText("Connecter");
    }
}

void MainWindow::on_BTN_Losange_clicked()
{
    if (serial->isOpen() && serial->isWritable())
    {
        serial->write("#MODE,LOSANGE\n\r");
        ui->TermTransmission->setText("#MODE,LOSANGE");
        mode = 'a';
        ui->lineEdit_Mode->setText("AUTO");
        ui->BTN_Wiimote->setText("Connecter");
    }
}

void MainWindow::on_BTN_Cercle_clicked()
{
    if (serial->isOpen() && serial->isWritable())
    {
        serial->write("#MODE,CERCLE\n\r");
        ui->TermTransmission->setText("#MODE,CERCLE");
        mode = 'a';
        ui->lineEdit_Mode->setText("AUTO");
        ui->BTN_Wiimote->setText("Connecter");
    }
}

void MainWindow::on_BTN_Actualiser_clicked()
{
    ui->comboBox->clear();
    QList<QSerialPortInfo> L = QSerialPortInfo::availablePorts();
    for (i = 0; i < L.size();  i++)
    {
        ui->comboBox->addItem(L.at(i).portName());
    }
}

void MainWindow::SerialRead()
{

    QByteArray Data = serial->readLine();

    QString Trame(Data);

    if (serial->isOpen() && Trame.contains("$"))
    {
        serial->write("$\n\r");
        ui->label_etat_serie->setText("Connecté");
        ui->BTN_connecter->setText("Déconnecter");
    }


    if (Trame.contains("#WII")){
        if (Trame.contains("NCONNECTE"))
        {
            ui->label_wii->setText("Déconnecté");
            ui->BTN_Wiimote->setText("Connecter");
            mode = 'w';
        }
        if (Trame.contains(",CONNECTE"))
        {
            ui->label_wii->setText("Connecté");
            ui->BTN_Wiimote->setText("Déconnecter");
            mode = 'w';
        }
    }

    if (Trame.size() >= 16)
    {
        //Format de la chaine des infos : #PARAM,ON/OFF,H,V
        if (Trame.contains("#PARAM")) //Detecte la reception d'une info
        {
            if (Trame.contains("ON")) ui->lineEdit_etat_laser->setText("ON");
            else if(Trame.contains("OFF")) ui->lineEdit_etat_laser->setText("OFF");

            QStringList D = Trame.split(",");

            if (!D[2].isEmpty() && (D[2].startsWith("+") || D[2].startsWith("-")))
                ui->lineEdit_Servo_H->setText(D[2]);
            if (!D[3].isEmpty() && (D[3].startsWith("+") || D[3].startsWith("-")))
                ui->lineEdit_servo_V->setText(D[3]);
        }
    }
    ui->TermReception->setText(Trame);
}

void MainWindow::on_BTN_Laser_ON_clicked()
{
    if (ui->BTN_Laser_ON->text() == "Allumer laser")
    {
        if (serial->isOpen() && serial->isWritable() && mode == 'm')
        {
            serial->write("#LASER,ON\n\r");
            ui->TermTransmission->setText("#LASER,ON");
            ui->lineEdit_etat_laser->setText("ON");
            ui->BTN_Laser_ON->setText("Eteindre laser");
        }
    }
    else
    {
        if (serial->isOpen() && serial->isWritable() && mode == 'm')
        {
            serial->write("#LASER,OFF\n\r");
            ui->TermTransmission->setText("#LASER,OFF");
            ui->lineEdit_etat_laser->setText("OFF");
            ui->BTN_Laser_ON->setText("Allumer laser");
        }
    }
}

void MainWindow::on_BTN_Quitter_clicked()
{
    MainWindow::closeWindow();
}

void MainWindow::closeWindow()
{

    if (serial->isOpen())
    {
        serial->write("#EXIT");
        ui->TermTransmission->setText("#EXIT");
        on_BTN_connecter_clicked();
    }
    MainWindow::close();
}


