#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QMessageBox"

QString msg="";

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
    bool cb1,cb2,cb3;
    cb1=ui->checkBox->isChecked();
    cb2=ui->checkBox_2->isChecked();
    cb3=ui->checkBox_3->isChecked();

    msg="";
    if(cb1){
        msg+="CB1 marcado,";
    }if(cb2){
        msg+=" CB2 marcado,";
    }if(cb3){
        msg+=" CB3 marcado";
    }
    QMessageBox::information(this,"Checkboxes ",msg);
}
