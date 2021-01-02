#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDesktopServices>
#include <QUrl>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QString link="http://www.google.com.br";
    QDesktopServices::openUrl(QUrl(link));
}

void MainWindow::on_pushButton_2_clicked()
{
    QString python="file:///usr/bin/idle-python3.8";
    QDesktopServices::openUrl(QUrl(python));
}
