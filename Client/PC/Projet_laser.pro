#-------------------------------------------------
#
# Project created by QtCreator 2016-03-08T14:44:51
#
#-------------------------------------------------

QT       += core gui
QT       += serialport

CONFIG += c++11

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Projet_laser
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui
