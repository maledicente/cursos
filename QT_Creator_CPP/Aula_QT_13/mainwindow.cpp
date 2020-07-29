#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QMessageBox"

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
    QString username = ui->lineEdit->text();
    QString senha = ui->lineEdit_2->text();

    if(username == "curso" && senha == "123"){
        QMessageBox::information(this, "Login", "OK");
    }else{
        QMessageBox::warning(this, "Login","Username ou login incorretos");
    }

}
